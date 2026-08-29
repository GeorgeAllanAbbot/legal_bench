
# 标注数据结构

## 1. Case Taxonomy

每个案例对应一条 JSON 对象。

- `case_id`、`case_name`：稳定关联键和案例名称。
- `annotation_status`：整条 projection 的状态。
- `practice_area`：主要/次要法律领域、置信度和证据。
- `matter_types`：具体案件或程序类型、置信度和证据。
- `legal_issues`：当前法院处理的法律问题，包含 mention 与 adjudication 两类置信度。
- `unmapped_matter_types`、`unmapped_legal_issues`：不在冻结 canonical Registry 中但被保留的概念。
- `needs_review`、`review_applied`、`review_status`：审核状态。
- `moved_legal_issues`、`legal_issue_simplification`：Legal Issue 简化处理的 lineage。

Matter Type 与 Legal Issue 有意分开。例如 `breach_of_contract` 可以表示案件是什么争议，而管辖权或证据问题可能才是该 opinion 实际裁判的 Legal Issue。

## 2. Matter Type Features

每个 `case_id × matter_type_id` 标注任务对应一条 JSON 对象。

- `job_id`：唯一复合键。
- `case_id`、`case_name`：关联 taxonomy 与原始语料。
- `matter_type_ids`：本任务适用的 Matter Type。
- `annotation_source`、`annotation_status`：模型/复核来源和最终状态。
- `review_history`、`human_review`：审核轨迹。
- `matter_type_feature_annotations`：Matter Type 对象与 feature 值。

Feature 定义、类型、单位、允许值和 Matter Type 包含关系见 `matter_type_feature_registry_v1_1.json`。双语 feature 参考表中的“有效数”表示状态不等于 `not_mentioned` 的 feature instance 数量，不一定等于唯一案例数。

## 证据与缺失值

标注流程输出的证据文本会被保留。缺失值或 `not_mentioned` 表示 opinion 没有提供足够依据，不能解释为 0、false 或否定性的法律裁判。

## 版本

- 发布包：v3 annotation-only release。
- Practice Area 与 Matter Type Registry：v3.2.0。
- 简化 Legal Issue Registry：v3.1-simplified。
- Matter Type feature Registry/数据：v1.1。
