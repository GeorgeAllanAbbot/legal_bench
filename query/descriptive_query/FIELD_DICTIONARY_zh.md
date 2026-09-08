# 描述型 Query 字段说明

## 发布文件

| 文件 | 是否公开给被测系统 | 内容 |
|---|---|---|
| `queries_public.json` | 是 | 题面、instruction、任务类型、难度、split 和公开评测元数据 |
| `qrels_private.json` | 否 | Ground Truth、positive/negative/unjudged qrels 和答案派生方式 |
| `benchmark_full.json` | 否 | 构建、审计和复现实验所需的完整内部对象 |
| `splits.json` | 可公开 ID | 固定的 dev/validation/test Query ID |
| `quality_report.json` | 是 | 完整性、分布和确定性校验结果 |
| `authority_sources.json` | 是 | Query 现实用途的外部依据，不是答案来源 |
| `manifest.json` | 是 | 版本、随机种子、上游文件和 SHA256 |

## 公开 Query 字段

| 字段 | 类型 | 含义 |
|---|---|---|
| `id` | string | 唯一 Query ID，例如 `legal_en_descriptive_001` |
| `query` | string | 提供给检索/RAG 系统的英文自然语言问题 |
| `instruction` | string | 答案格式要求；例如只输出整数、百分比或组名 |
| `query_family` | enum | `count`、`proportion` 或 `comparison` |
| `type` | enum | `sql` 表示完整结构化投影；`hybrid` 表示结构化加语义条件 |
| `difficulty` | enum | 当前为 `medium` 或 `complex`，由约束数量和语义条件决定 |
| `split` | enum | `dev`、`validation`、`test`；test 必须冻结 |
| `evidence_size_bucket` | enum | `small` ≤50；`medium` 51–200；`large` >200 positive cases |
| `recommended_metrics` | string[] | 根据 evidence 规模建议使用的检索/答案指标 |
| `constraint_dimensions` | string[] | Query 使用的年份、法院、Matter Type、语义条件等维度名称 |

## 私有 Qrels 字段

| 字段 | 类型 | 含义 |
|---|---|---|
| `id` | string | 与公开 Query 一一对应 |
| `split` | enum | 冗余保存以便独立评测 |
| `qrel_confidence` | enum | 当前为 `silver`，表示模型辅助并经规则/抽检校验 |
| `qrel_states.positive` | object | `case_id → 2`；已判定相关案例 |
| `qrel_states.negative` | object | `case_id → 0`；已明确判定的不相关 hard negatives |
| `qrel_states.unjudged` | string[] | 检索池中尚未裁决的案例，不能按负例处理 |
| `benchmark_tasks.retrieval.target` | string | 当前固定为 `case_set` |
| `positive_case_ids` | string[] | 与 positive qrels 相同的案例集合 |
| `positive_document_ids` | string[] | 支持判断的 Opinion/document ID |
| `hard_negative_case_ids` | string[] | 明确负例，用于 bpref 或 hard-negative 分析 |
| `unjudged_pool_case_ids` | string[] | 未判断 pool |
| `qrel_completeness` | enum | SQL 为 `exhaustive_structured_projection`；Hybrid 为 `partial_pool` |
| `benchmark_tasks.answer.answer_type` | enum | `integer`、`percentage` 或 `argmax_group` |
| `ground_truth` | integer/object | 最终统计答案 |
| `derivation` | object/string | Ground Truth 的 SQL/分组/分母派生说明 |
| `evaluation` | enum | `exact_match` 或 `numeric_tolerance` |
| `population_provenance` | string/null | 比例题分母所用冻结 projection 来源 |

## 完整对象附加字段

`benchmark_full.json` 还包含：

- `structured_filters`、`sql`、`sql_parameters`：结构化候选范围和可复现 SQL；
- `semantic_condition`：概念定义、required elements、exclusions、candidate phrases 和裁判规则；
- `answer`、`answer_derivation`：统计答案及派生过程；
- `evidence`、`evidence_documents`、`evidence_details`：案例、文书和支持片段；
- `query_ir`、`logical_axes`、`logic_mode`：机器可执行 Query 表示；
- `authority_basis`、`research_rationale`、`research_value`：现实需求依据；
- `snapshot`：数据库、Matter Type projection 和 qrel 版本；
- `evidence_audit`、`validation_errors`：审计结果。

## Evidence 与 Ground Truth

```text
Structured population
  + optional semantic condition
  -> positive case set (Evidence)
  -> count / numerator / group counts
  -> Ground Truth Answer
```

计数题的答案等于 positive case 数；比例题 numerator 等于 positive case 数，denominator 来自指定
总体；比较题把 positive cases 分组后选择最大组。一个案例可对应多个 document，但 case-level
检索指标中只能计一次。

## 推荐指标

- Case Retrieval：Recall@K、nDCG@K、bpref；同时报告 ranking depth 和 judged rate。
- Count：整数 exact match。
- Proportion：numerator/denominator exact match，percentage 使用预设数值容差。
- Comparison：winner/tie 与各组数量匹配。

`judged_precision` 只基于已判断案例；由于 Hybrid hard negatives 较少，不能当作普通 precision。
