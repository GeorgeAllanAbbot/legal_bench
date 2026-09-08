# Legal Bench v3.1 数据集

本目录保存完整的 CourtListener 英文案例数据、结构化标注、Registry 和数据质量报告。
核心发布物是 `dataset/legal_rag_dataset_v3.db.zst.part-*`，恢复后得到一个同时包含案例元数据、
Opinion 文书正文、检索 chunks、Matter Type 和分析特征的 SQLite 数据库。

## 目录

| 路径 | 内容 |
|---|---|
| `dataset/` | 完整 SQLite 数据库分片、Schema、字段目录和覆盖率报告 |
| `registry/` | 冻结的 Practice Area、Matter Type、Legal Issue 和 Feature Registry |
| `docs/` | 标注结构、字段含义和 Matter Type→Feature 包含关系 |

## 数据层级

```text
Court (`dim_court`)
  └─ Case / Opinion Cluster (`case_record`)
       ├─ Opinion document (`opinion_record`)
       │    └─ Retrieval chunk (`search_document`)
       ├─ Practice Area (`case_practice_area_v3`)
       ├─ Matter Type (`case_matter_type_v3`)
       │    └─ Matter occurrence (`matter_type_annotation_v1_1`)
       │         └─ Feature values (`matter_type_feature_value_v1_1`)
       └─ Legal Issue (`case_legal_issue_v3`)
```

- **Practice Area** 是宽泛法律领域。
- **Matter Type** 是具体案件、请求、争议或程序类型，是统计和选择 Feature Pack 的主要分类。
- **Legal Issue** 是法院实际处理的较窄法律问题，不是案件类型，且不是每个案例都必须有。
- **Feature** 是 Matter Type 下可从当前 Opinion 直接提取的事实、金额、日期、主体和结果。

## 主要覆盖率

| 项目 | 数量 | 覆盖率 |
|---|---:|---:|
| Cases | 20,000 | 100% |
| Opinions（正文非空） | 21,261 | 100% |
| Usable opinions | 21,189 | 99.66% |
| Retrieval chunks | 94,314 | - |
| Case name / court / decision date | 20,000 | 100% |
| Matter Type | 20,000 cases | 100% |
| Practice Area | 18,206 cases | 91.03% |
| Retained Legal Issue | 11,864 cases | 59.32% |
| Accepted Matter Type Feature job | 12,712 cases | 63.56% |

完整分布见 `dataset/COVERAGE_REPORT.json`。Matter Type 的 100% 是模型辅助 projection 覆盖率，
不表示 100% 人工 Gold 准确率。Legal Issue 为空表示没有保留达到裁判证据门槛的 canonical issue，
不表示案件不存在法律问题。

## 数据来源

基础数据来自 Free Law Project 的 CourtListener bulk data `2026-06-30` 快照：

- Opinion Clusters：案例聚合、案名、日期、引证和关联信息；
- Opinions：Opinion 类型和 HTML/plain-text 文书正文；
- Courts：法院名称、司法辖区和法院元数据；
- Dockets：docket 标识及关联元数据。

官方来源：

- [CourtListener Bulk Legal Data](https://www.courtlistener.com/help/api/bulk-data/)
- [CourtListener project, Free Law Project](https://free.law/projects/courtlistener/)
- [CourtListener REST API](https://www.courtlistener.com/help/api/rest/)

本数据集不是 CourtListener 官方 Benchmark。`raw_json` 和 `provenance_json` 用于保留来源追踪；
使用和再发布应同时遵守原始记录对应的法律、许可与 CourtListener 使用条件。

## 构建方法

- 时间范围：1970–2025；约 13% 为 2000 年前案例，保留趋势研究能力，主体仍为 21 世纪案例。
- 抽样单位：Opinion Cluster；一个 case 可以对应多个 Opinion document。
- 文本选择：从 CourtListener HTML/plain-text 候选中生成 `preferred_text`，保留来源字段。
- 最低文本门槛：构建阶段要求案例存在可检索正文；72 份附属 Opinion 未达到 usable 阈值但正文非空。
- Chunking：约 800 tokens，overlap 120；优先 majority-like/unknown opinion group。
- 法院标准化：由 `court_id`、CourtListener jurisdiction code 和法院名称联合映射。
- v3 标注：规则候选、模型辅助抽取、确定性 validator、失败重试和少量人工复核。

## 分类体系参考

本项目使用自己的实用型 closed registry，没有直接复制任何单一外部 taxonomy：

- [U.S. Courts Civil Cover Sheet / Nature of Suit](https://www.uscourts.gov/forms-rules/forms/civil-cover-sheet)：
  用于参考美国联邦民事案件类型表达；
- [SALI LMSS](https://github.com/sali-legal/LMSS)：用于术语标准化和未来可选映射参考；
- CourtListener 的 court、docket、opinion type 和案件正文：用于来源元数据和当前案件证据；
- 律师可理解的 Practice Area 与具体 Matter Type 边界：由本项目 Registry 明确定义。

SALI/PACER 参考不等于本项目标签，也不参与普通查询。外部映射应作为独立兼容层处理。

## 使用方法

恢复数据库：

```bash
./scripts/restore_integrated_db.sh
```

Python 只读查询：

```python
import sqlite3

db = sqlite3.connect("file:data/dataset/legal_rag_dataset_v3.db?mode=ro", uri=True)
rows = db.execute("""
    SELECT c.case_id, c.case_name, c.decision_year, c.court_level, m.matter_type
    FROM case_record AS c
    JOIN case_matter_type_v3 AS m USING (case_id)
    WHERE m.matter_type = ? AND c.decision_year BETWEEN ? AND ?
    ORDER BY c.decision_year, c.case_id
""", ("breach_of_contract", 2010, 2020)).fetchall()
```

读取 Opinion 正文：

```sql
SELECT c.case_id, c.case_name, o.opinion_id, o.opinion_type, o.preferred_text
FROM case_record AS c
JOIN opinion_record AS o ON o.cluster_id = c.cluster_id
WHERE c.case_id = 'cluster_4708120';
```

按数值 Feature 筛选：

```sql
SELECT DISTINCT f.case_id, c.case_name, f.value_number, f.unit
FROM matter_type_feature_value_v1_1 AS f
JOIN case_record AS c USING (case_id)
WHERE f.matter_type = 'breach_of_contract'
  AND f.feature_key = 'amount_awarded_usd'
  AND f.value_status = 'present'
  AND f.value_number >= 100000;
```

## 重要限制

- `citations_json` 在本快照中全部为空，不适合直接做 citation-network benchmark。
- `not_mentioned` 表示 Opinion 未提供信息，不得当作 `0`、`false` 或否定裁判。
- Feature 中 `present` 才表示有当前案件 evidence 支持；应保留单位，不能静默换算。
- `case_features` 是 v2 规则弱特征；v3 统计优先使用规范化 v3 表。
- Opinion 正文可能包含页眉、引证格式、编辑说明和 OCR/排版噪声。
- 本项目标注属于 Silver 研究数据，不构成法律意见。

字段级说明见 `dataset/FIELD_DICTIONARY_zh.md`，全部 Feature 与 Matter Type 的包含关系见
`docs/MATTER_TYPE_FEATURE_REFERENCE_zh.md`。
