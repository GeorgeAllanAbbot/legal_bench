# 英文法律描述型 Benchmark v6

本 Benchmark 基于冻结的 CourtListener 20k 数据集，共包含 120 条描述型法律统计 Query。

## 两类任务

每条 Query 被拆分为两个独立任务：

1. **Case-set Retrieval（案例集合检索）**：找出同时满足结构化条件和语义条件的案例。
2. **Answer Generation（答案生成）**：根据相关案例集合输出数量、比例或比较结果。

两类任务必须分开评测。聚合答案正确，不代表检索出的案例证据正确。

## 三态 Qrels

- `positive`：经过裁决的相关案例，相关度为 2。
- `negative`：经过明确裁决的 hard negative，相关度为 0。
- `unjudged`：由多种检索方法形成、但尚未裁决的候选，不得默认视为负例。

SQL Query 标记为 `exhaustive_structured_projection`。Hybrid Query 标记为 `partial_pool`，因为目前没有穷举审查全部 20,000 篇 opinion 的语义相关性。

## Evidence 规模与指标

- `small`：不超过 50 个正例，使用 Recall@50、Recall@100。
- `medium`：51–200 个正例，使用 Recall@100、Recall@500。
- `large`：超过 200 个正例，使用 Recall@500、Recall@1000 和答案准确率。

所有规模继续报告 Precision@10 与 nDCG@10。相关案例超过 100 时，不应仅使用 Recall@100 判断 Query 质量。

## 冻结划分

- Development：60 条
- Validation：30 条
- Test：30 条

划分按 Query family、SQL/Hybrid 类型、难度和 evidence 规模进行确定性分层。后续调试不得依据 Test 结果修改 Test Query 或 qrels。

## 文件

- `benchmark_full.json`：完整研究数据。
- `queries_public.json`：不含答案和 qrels 的公开 Query。
- `qrels_private.json`：答案、三态 qrels 和任务定义。
- `splits.json`：冻结的 Query 划分。
- `quality_report.json`：确定性质量检查与分布报告。
- `manifest.json`：文件校验和、版本来源、随机种子和冻结状态。

## Query 质量与限制

- 没有完全重复的题面，也没有 positive evidence 为空的 Query。
- 每条 Query 组合 2–4 个约束维度；120 条中有 80 条使用 3–4 个维度。
- 当前覆盖 16 类 Matter Type 组合，不代表源数据库中的所有 Matter Type。
- 显式负例分布不均：SQL Query 有 522 个，Hybrid Query 只有 22 个。因此
  `judged precision` 只是稀疏已判断池上的条件精度，不能作为普通检索 precision 报告。
  应优先报告 Recall、nDCG、bpref，并同时报告 judged rate。

当前版本属于 Silver 研究标注，不是人工 Gold 标签，也不构成法律意见。
