
# 面向 RAG 的查询准备

该标注发布包为后续查询层准备两条通道。

## 结构化通道

下列 canonical 字段可用于精确过滤、计数、分组和排序：

- taxonomy：`practice_area.primary`、`matter_types[].id`、`legal_issues[].issue_id`；
- 审计字段：`annotation_status`、`needs_review`、置信度阈值；
- 分析特征：`feature_key`、状态、标准化值、单位和证据；
- 与 CourtListener 原始库关联后：法院、法院层级、辖区和年份。

通常只有状态不等于 `not_mentioned` 的值才能满足 feature 条件。缺失表示未知，不表示否定或数值 0。

## 语义通道

案件事实、当事人主张、holding 和法律推理应从单独维护的 opinion chunk 语料中检索。可在 BM25/向量检索前后应用结构化约束，并要求最终回答引用案例名称和来源。

## 推荐 Query IR

```json
{
  "intent": "count_cases | find_cases | aggregate | compare | explain",
  "semantic_query": "可选的自然语言检索内容",
  "filters": [
    {"field": "matter_type", "operator": "in", "value": ["foreclosure_mortgage"]},
    {"field": "feature.amount_awarded_usd", "operator": "gt", "value": 100000}
  ],
  "group_by": ["year"],
  "sort": [{"field": "feature.amount_awarded_usd", "direction": "desc"}],
  "limit": 20
}
```

## 仿照中文数据的英文问题类型

1. **数量统计**："How many foreclosure cases awarded attorney fees over $50,000?"
2. **组合条件查找**："Find asylum cases in which detention duration was mentioned."
3. **结果分布**："What is the distribution of current-court dispositions in sentencing appeals?"
4. **年份趋势**："How did reported damages awards in employment discrimination cases change by year?"
5. **类型对比**："Compare median settlement amounts for product liability and medical malpractice cases."
6. **结构化约束 + RAG**："In duty-to-defend cases, explain when courts found that the insurer owed a defense."

前五类可以主要依靠标注字段过滤和聚合；第六类必须把筛选出的 case ID 与原始 opinion 文本关联，再执行检索和生成。

## 查询约束

- 未提及金额不能按 0 处理。
- Legal Issue 不能替代 Matter Type。
- 请求的救济、下级法院结果和当前法院 disposition 必须分开。
- 保留币种和单位，非美元数值不得静默换算。
- 高置信度统计应排除或单独报告待审核记录。
