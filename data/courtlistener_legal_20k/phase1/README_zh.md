# CourtListener Legal Dataset Phase 1

本目录是面向检索、RAG 和 benchmark 的稳定 Phase 1 数据接口。源数据库中的实验性
分类列没有带入本数据库。

## 文件

- `legal_cases.db`：权威 SQLite 数据库。
- `cases.jsonl`：案件基础信息及本地全文。
- `documents.jsonl`：独立 opinion 文档。
- `case_features.jsonl`：弱案件类型、程序阶段、结果和分类证据。
- `dataset_quality_report.json`：缺失率及法院、年份、类型分布。
- `phase1_validation_report.json`：字段完整率、分类分布和随机 20 条样例。
- `SCHEMA.sql`：数据库结构快照。
- `DATASET_GUIDE_zh.md`：数据边界、字段语义、SQL/RAG/benchmark 使用方案与限制。

## 表关系

```text
cases (case_id)
  |-- documents (case_id)
  |-- docket_entries (case_id)
  `-- case_features (case_id)
```

`docket_entries` 当前为空，因为该 20k 数据集来自 opinion-led bulk data，并非每个
Opinion Cluster 都有关联的 RECAP timeline。表被正式保留，后续可增量补充。

## 规范

- `court_type` 使用 `federal`、`state`、`administrative`、`other`，用于粗粒度约束。
- `court_level` 使用八级固定枚举，可与 `court_type`、`year_filed` 组合筛选。
- `jurisdiction` 当前统一为 `US`。
- `opinion_type` 使用 majority、lead、concurrence、dissent、order、unknown。
- `case_type_weak` 是最多两个值的 JSON 数组。
- `procedural_stage_current` 只能表示一个当前阶段。
- `procedural_stage_history` 与 `outcome_keyword` 是 JSON 数组。
- `classification_evidence` 保存自动抽取依据及上下文。
- 所有 case 的 `full_text` 长度至少为 350 字符。

旧的 `legal_domain`、`case_category` 和 `case_subcategory` 不存在于 Phase 1 数据库。

完整说明见 [DATASET_GUIDE_zh.md](DATASET_GUIDE_zh.md)。
