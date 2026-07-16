# CourtListener Phase1 数据集说明与使用方案

## 1. 这是什么

Phase1 是一个面向法律检索、RAG、分析性搜索和可复现实验的稳定数据接口。它从
CourtListener 的 Opinion Cluster / opinion bulk data 派生而来：一个 `case_id` 对应一个
案件聚类，一条或多条 `documents` 记录对应该案件下的 opinion 文书。

当前版本包含：

| 项目 | 数量 / 范围 |
|---|---:|
| 案件聚类 (`cases`) | 20,000 |
| opinion 文书 (`documents`) | 21,755 |
| 具有至少 350 字符正文的案件 | 20,000 (100%) |
| 年份 | 1900-2026 |
| docket timeline (`docket_entries`) | 0 |
| 联邦法院案件 | 6,134 |
| 州法院案件 | 12,048 |
| 行政机构 / 专门法院类案件 | 640 |
| 其他或无法稳定映射的法院 | 1,178 |

推荐将 `phase1/legal_cases.db` 视为下游实验的只读 source，而将索引、运行结果、人工
修订和 benchmark 标签写入项目外部目录。原始主库
`../legal_cases_20k.db` 保留不动，用于重建与追溯。

## 2. 适合和不适合的用途

适合：

- 英文判例 / 裁判文书语义检索与案例引用。
- 以案件为单位的法律主题、法院层级、年份与结果分布分析。
- RAG 的检索、重排、回答和引用可追溯性实验。
- 按法院或时间切分的 retrieval / RAG benchmark。
- 人工复核弱标签、构建 query relevance judgement 或 gold answer。

不适合直接作为：

- 完整诉讼卷宗。当前 `docket_entries` 为空，不能据此推断案件没有 docket history。
- complaint、discovery、证据材料或全部附件的集合。
- 权威的人工法律分类、法律意见或实时法律数据库。
- 统计意义上的全美国法院随机样本。法院、年代和可公开获得文书的覆盖明显不均匀。

## 3. 数据层次与关联关系

```text
cases: 一个 Opinion Cluster / 可检索案件
  |
  +-- documents: 一个或多个 opinion 文书
  |
  +-- case_features: 可查询的弱标签与抽取依据
  |
  `-- docket_entries: 预留的 RECAP 时间线接口（当前为空）
```

`cases.full_text` 是当前检索与 RAG 的案例级正文。`documents.text` 是更接近原始
opinion 粒度的正文。两者不要混用：

- 做案件级搜索、案例去重、趋势分析时，用 `cases`。
- 做细粒度 passage retrieval、opinion-type 过滤或多意见比较时，用 `documents`。
- 结果引用、案件类型、程序和 outcome 回查时，用 `case_id` 关联 `case_features`。

## 4. 核心表和字段

### `cases`

| 字段 | 含义 | 推荐用途 |
|---|---|---|
| `case_id` | Phase1 稳定主键，如 `cluster:9643459` | 全部关联、引用与去重键 |
| `cluster_id` / `docket_id` | CourtListener 来源标识，允许为空 | 来源回查 |
| `case_name` | 规范化案件名 | 展示和生成引用 |
| `court_id` / `court_name` | 法院原始标识与展示名称 | 精确法院筛选 |
| `court_type` | `federal`、`state`、`administrative`、`other` | 粗粒度约束 |
| `court_level` | 八级枚举，见下文 | 层级约束和切分 |
| `jurisdiction` | 当前统一为 `US` | 预留跨辖区扩展 |
| `date_filed` / `year_filed` | 日期与整数年份 | 时间约束、时间切分 |
| `precedential_status` / `citation` | 来源元数据 | 引用质量控制 |
| `absolute_url` | CourtListener 定位 URL | 人工核验 |
| `full_text` | 本地可检索正文，长度至少 350 字符 | 主要检索语料 |
| `raw_json` / `provenance_json` | 原始记录与构建来源 | 审计和重建 |

### `documents`

`document_id` 是文档主键，`case_id` 是外键。`document_type`、`title`、`text`、
`pdf_url`、`author`、`opinion_type`、`page_count` 与来源字段构成 opinion 级接口。

`opinion_type` 规范为：`majority`、`lead`、`concurrence`、`dissent`、`order`、
`unknown`。当前分布为 majority 9,289、lead 9,033、order 2,399、dissent 601、
concurrence 400、unknown 33。做“法院的 holding”类任务时，应优先使用 majority/lead，
不要无差别混入 dissent 或 concurrence。

### `case_features`

| 字段 | 含义 | 注意事项 |
|---|---|---|
| `case_type_weak` | 至多两个值的 JSON 数组 | 弱标签，不是人工 gold label |
| `procedural_stage_current` | 一个当前阶段 | 例如 `appeal`、`summary_judgment` |
| `procedural_stage_history` | 历史阶段 JSON 数组 | 不应与 current 混淆 |
| `outcome_keyword` | 结果 JSON 数组 | 优先来源于 disposition/结尾，但仍需复核 |
| `classification_evidence` | 规则命中、法条与上下文 | 用于解释与人工检查 |

`case_type_weak` 允许：`tax`、`criminal`、`civil_rights`、`contract`、`commercial`、
`property`、`immigration`、`labor`、`bankruptcy`、`administrative`、`family`、
`intellectual_property`、`other`。当前 `other` 为 10,824，不意味着正文或元数据缺失，
而表示当前规则不足以稳定归类；不要在分析中把它当成一个同质法律主题。

## 5. 法院与时间约束

### 固定枚举

`court_type`：

```text
federal | state | administrative | other
```

`court_level`：

```text
federal_supreme | federal_circuit | federal_district |
state_supreme | state_appellate | state_trial |
administrative | other
```

数据库在 `(court_type, court_level, year_filed)` 上建立了 `idx_cases_constraints` 联合
索引。优先使用这些字段做范围过滤，再进行全文、BM25 或 dense ranking。`court_type`
和 `court_level` 是根据 CourtListener court id/name 归一化的启发式字段；对于会影响
法律结论的研究，应同时保留 `court_name` 并抽样复核。

SQL 示例，检索 2018-2026 年的联邦巡回法院 immigration 案例：

```sql
SELECT c.case_id, c.case_name, c.court_name, c.date_filed,
       f.case_type_weak, f.outcome_keyword
FROM cases AS c
JOIN case_features AS f USING (case_id)
WHERE c.court_type = 'federal'
  AND c.court_level = 'federal_circuit'
  AND c.year_filed BETWEEN 2018 AND 2026
  AND f.case_type_weak LIKE '%immigration%'
ORDER BY c.year_filed DESC, c.case_id
LIMIT 50;
```

注意 SQLite 中 `case_type_weak` 与 `outcome_keyword` 是 JSON 文本。若需要精确统计，
使用 `json_each`，不要只依赖 `LIKE`：

```sql
SELECT value AS case_type, COUNT(*) AS n
FROM case_features, json_each(case_type_weak)
GROUP BY value
ORDER BY n DESC;
```

## 6. 建议的使用方案

### 方案 A：探索与统计

适用于主题分布、法院层级比较、年份趋势和抽样检查。

1. 先用 `court_type`、`court_level`、`year_filed` 固定分析范围。
2. 再通过 `case_type_weak`、`procedural_stage_current`、`outcome_keyword` 形成候选集合。
3. 对每个结论输出 `case_id`、法院、年份、样本量和 SQL。
4. 对 `other`、低频法院和 outcome 做随机人工复核。

建议不要将原始计数直接解释为法院间的真实发案率；它反映的是本数据集的收录与文书可得性。

### 方案 B：法律检索与 RAG

当前 `rag_baselines/` 可直接以 Phase1 数据库构建 index。默认每案最多一个 1,000-token
chunk，overlap 200；这是基线设置，不是唯一合理的 chunk 策略。

```bash
python3 rag_baselines/scripts/build_index.py \
  --config rag_baselines/configs/default.yaml

python3 rag_baselines/scripts/run_baseline.py \
  --query "What are common outcomes in immigration appeals?" \
  --baseline hybrid_rerank \
  --court-type federal \
  --court-level federal_circuit \
  --year-from 2018 \
  --year-to 2026 \
  --rag
```

结果 JSON 会保存 query、constraints、排名案例、分数、prompt context、模型回答、
token usage 和 latency。RAG 输出应要求模型只引用提供的案例；生成回答是研究辅助，
不能代替律师核验或原文阅读。

推荐 baseline 对照顺序：

1. `raw_llm`：没有语料，测量模型先验能力。
2. `bm25`：词面检索下限。
3. `dense`：当前环境若无 sentence-transformers，会退回 TF-IDF cosine，报告中应记录 backend。
4. `hybrid`：BM25 和 dense 归一化加权。
5. `bm25_rerank`、`dense_rerank`、`hybrid_rerank`：比较重排增益。
6. 在 `hybrid_rerank` 固定后，运行 `query_rewrite`、`hyde`、`crag`。

### 方案 C：构建 benchmark

建议用不可重叠的 case-level split，避免同一案件的多个 opinion 或相邻片段同时出现在训练
和测试集合。

1. 明确任务：known-item retrieval、case ranking、grounded QA、outcome extraction 或 analytical search。
2. 以 `case_id` 为去重与分割单位；文档与 chunk 必须跟随所属 `case_id`。
3. 优先使用年份切分，例如 1900-2018 开发、2019-2022 验证、2023-2026 测试；同时报告各法院
   和领域分布，避免时间切分造成单一法院偏差。
4. 由人工为 query 标注 relevant / partially relevant / not relevant，并记录对应 `case_id`、
   文书段落和理由。
5. Retrieval 报告 Recall@k、MRR、nDCG；生成报告 citation precision、citation coverage、
   groundedness 与人工正确性。
6. 任何模型推理输出必须另存，禁止覆盖 `case_features` 的弱标签。

### 方案 D：人工复核与标签修订

人工复核文件应以 `case_id` 为主键，至少保存：

```json
{
  "case_id": "cluster:9643459",
  "reviewer": "reviewer_id",
  "reviewed_at": "2026-07-16",
  "field": "case_type_weak",
  "original_value": ["other"],
  "corrected_value": ["administrative"],
  "rationale": "Social Security administrative review.",
  "evidence_location": "opening paragraphs"
}
```

修订标签应写入新的 review/annotation 数据集，不要直接覆写 Phase1 数据库；这样才可比较
规则标签、模型标签与人工标签。

## 7. 质量、偏差与安全边界

- 正文、案名、法院、日期在 Phase1 中均无缺失；这不等于事实、holding、法条或 outcome 全部可被可靠自动抽取。
- 文本可能有页眉、脚注、扫描/OCR 噪声、引文和历史案件描述。不能通过全文出现的 `reversed`、
  `dismissed` 等词直接判断本案 disposition。
- `outcome_keyword`、程序阶段和案件类型均是弱标签。统计、训练和评测需保留不确定性，并抽样审计。
- 同一 `case_id` 可有多条 opinion。做 holding 检索时，优先过滤 majority/lead；做观点分歧研究时，
  保留 concurrence/dissent 并在结果中明确其 opinion type。
- 法律研究和生成回答必须回链到 `absolute_url`、`citation`、`case_id` 和必要的原文片段。

## 8. 可复现性清单

一次实验至少记录：

```text
dataset path and rebuild version
SQL / query text
court_type, court_level, year range constraints
case_id-level split definition
chunk size, overlap, max chunks per case
retriever, embedding backend/model, reranker
LLM model, prompt template, temperature
metrics and exact result JSON paths
```

这使后续 FlashRAG、Analytical Search 或 agentic retrieval 能共享同一语料边界，并能区分
检索改进、生成改进和数据切分差异。
