# Legal Bench 查询数据

`descriptive_query/` 发布 120 条英文描述型法律分析题，用于比较 BM25、Dense、Hybrid、Reranker
及其他 RAG 方法能否找回正确案例集合，并生成正确的统计答案。

Query 与数据库通过 `case_id`、`document_id` 关联。题面与答案分开发布，避免测试集泄漏。

## 子目录

- `descriptive_query/`：正式 Benchmark v6。

## 任务类型

| Family | 数量 | 答案形式 | 例子 |
|---|---:|---|---|
| `count` | 40 | 整数 | 满足案件类型、年份与法律语义条件的案例有多少件 |
| `proportion` | 40 | numerator、denominator、percentage | 目标案例占指定总体的比例 |
| `comparison` | 40 | winner/tie、各组数量 | 哪个法院层级、辖区或时间组最多 |

其中 36 条为纯结构化 `sql` Query，84 条为结构化过滤加 Opinion 语义判断的 `hybrid` Query。

## 现实需求参考

Query 的统计维度参考以下机构公开的司法统计实践：

- [U.S. Courts Caseload Statistics Data Tables](https://www.uscourts.gov/statistics-reports/caseload-statistics-data-tables)：
  按法院、司法辖区、Nature of Suit、案件结果和时间统计；
- [Federal Judicial Center Integrated Database](https://www.fjc.gov/research/federal-court-cases-fjc-integrated-database-1979-present)：
  支持跨年度联邦民事、刑事、破产与上诉案件分析；
- [NCSC State Court Guide to Statistical Reporting](https://www.courtstatistics.org/__data/assets/pdf_file/0031/88735/State-Court-Guide-to-Statistical-Reporting.pdf)：
  州法院案件类别、状态和 disposition 统计；
- [BJS State Court Processing Statistics](https://bjs.ojp.gov/data-collection/state-court-processing-statistics-scps-and-national-pretrial-reporting-program-nprp)：
  刑事案件从起诉到裁判、结果和量刑的分析。

这些来源只证明 Query 类型具有现实研究意义，不提供本 Benchmark 的答案。Ground Truth 只来自
冻结数据库和本项目 qrels。

## 使用方法

公开评测只向系统提供 `queries_public.json`。运行结束后，由评测器读取 `qrels_private.json`。

```python
import json

queries = json.load(open("query/descriptive_query/queries_public.json"))
qrels = {x["id"]: x for x in json.load(open("query/descriptive_query/qrels_private.json"))}
```

检索任务以去重后的 `case_id` 排名为准；生成任务分别使用整数 exact match、比例数值容差或
comparison winner/tie 匹配。不得把 `unjudged` 当作负例。

完整字段说明、指标和 Evidence/Answer 关系见 `descriptive_query/README_zh.md` 与
`descriptive_query/FIELD_DICTIONARY_zh.md`。
