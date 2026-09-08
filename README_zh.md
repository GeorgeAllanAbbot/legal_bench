# Legal Bench v3.1

Legal Bench v3.1 是一个面向法律检索、RAG 和法律统计分析的英文美国判例研究数据集。
发布版本只保留两个主要入口：

```text
legal_bench/
├── data/                         # 数据库、Opinion 正文、标注、Registry 与数据说明
├── query/
│   └── descriptive_query/        # 120 条描述型 Query、答案、Evidence 与说明
├── scripts/                      # 恢复和校验脚本
├── README.md
├── README_zh.md
└── manifest.json
```

## 1. 数据库

`data/dataset/` 发布一个完整 SQLite 数据库，包含：

- 20,000 个 CourtListener Opinion Cluster 案例；
- 21,261 份非空 Opinion 文书正文，其中 21,189 份达到 usable-text 标准；
- 440 个法院和规范化 court level / jurisdiction；
- 94,314 个检索 chunks；
- 20,000 案例的 Matter Type projection；
- Practice Area、保留的 Legal Issue 和 Matter Type analytical features；
- 原始字段与 provenance，用于回溯 CourtListener 来源。

数据库由 4 个小于 GitHub 单文件限制的 Zstandard 分片发布。恢复：

```bash
./scripts/restore_integrated_db.sh
```

数据库字段、关系、覆盖率、来源和调用方式见 [data/README_zh.md](data/README_zh.md)。

## 2. 描述型 Benchmark

`query/descriptive_query/` 包含 120 条英文 Query：

- Count 40 条；
- Proportion 40 条；
- Comparison 40 条；
- SQL 36 条，Hybrid 84 条；
- 固定拆分为 dev 60、validation 30、test 30。

公开题面位于 `queries_public.json`；答案和 qrels 位于 `qrels_private.json`，评测前不得提供给
被测系统。详细说明见 [query/README_zh.md](query/README_zh.md)。

## 数据来源与参考

案例和文书来自 CourtListener `2026-06-30` bulk snapshot。CourtListener 是 Free Law Project
维护的开放法律数据库。本项目使用 Opinion Clusters、Opinions、Courts 和 Dockets 四类导出。

- [CourtListener Bulk Legal Data](https://www.courtlistener.com/help/api/bulk-data/)
- [Free Law Project: CourtListener](https://free.law/projects/courtlistener/)

分类设计参考 U.S. Courts Nature of Suit 的案件类型表达和 SALI LMSS 的术语标准化思想，但使用
本项目自己的实用型 closed registry。Query 设计参考 U.S. Courts、FJC、NCSC 和 BJS 的司法统计
维度。外部参考不提供本 Benchmark 的答案。

## 版本与质量边界

- Dataset release：v3.1；Taxonomy projection：v3.3.0。
- Practice Area / Matter Type Registry：v3.2.0。
- Simplified Legal Issue Registry：v3.1-simplified。
- Matter Type Feature：v1.1。
- Descriptive Benchmark：v6，Silver qrels。

Matter Type 覆盖率 100% 表示每案至少有一个模型辅助 projection，不代表人工 Gold 准确率。
Hybrid Query 的 evidence 是 partial pool；`unjudged` 不得按负例处理。本数据集不构成法律意见。

执行完整校验：

```bash
python3 scripts/verify_release.py
```
