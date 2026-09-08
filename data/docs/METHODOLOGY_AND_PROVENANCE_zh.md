# 构建方法、数据来源与 Provenance

## 1. 直接数据来源

发布数据库的案例元数据和 Opinion 正文直接来源于 CourtListener `2026-06-30` bulk snapshot：

| Bulk export | 本项目用途 | 主要落表 |
|---|---|---|
| `opinion-clusters` | Case/cluster、案名、日期、docket/court 关联 | `case_record` |
| `opinions` | Opinion 类型、作者、HTML/plain text、引证关系 | `opinion_record` |
| `courts` | 法院名称、辖区代码、层级和地域 | `dim_court` |
| `dockets` | Docket 标识、案名和关联信息 | `case_record` |

CourtListener 由 Free Law Project 维护。官方说明：

- https://www.courtlistener.com/help/api/bulk-data/
- https://free.law/projects/courtlistener/
- https://www.courtlistener.com/help/api/rest/

`raw_json` 保留 bulk row；`provenance_json` 标记来源文件/表。规范化字段可以服务查询，原始字段
用于审计。数据使用者仍应根据具体来源记录评估版权、许可和司法辖区要求。

## 2. 抽样范围

- 目标：20,000 个具有可检索 Opinion 正文的 Opinion Clusters。
- 年份：1970–2025。
- 决定性随机种子和加权时间桶用于保留约 13% 的 20 世纪尾部，同时让 21 世纪占主体。
- 抽样单位是 cluster，不是独立 Opinion；因此 20,000 cases 对应 21,261 opinions。
- 数据不是美国全部案件的概率样本，不能直接推断全国真实 filing rate 或 prevalence。

`decision_year` 是 Opinion/cluster 的裁判年份，不是 filing year。Benchmark 的时间问题必须按该
语义解释。

## 3. 文本处理

构建器在 CourtListener 提供的 HTML/plain-text 候选中选择 `preferred_text`，清理 HTML 和空白，
同时保留来源文本。正文非空 21,261 份，其中 21,189 份达到 usable-text 质量阈值。

检索 chunk 约为 800 tokens、overlap 120；默认主要从 `majority_like` 和 `unknown` Opinion group
生成。`chunk_token_count` 是构建器估算值。正文仍可能保留页码、页眉、编辑注、引证格式和 OCR
噪声。

## 4. 法院标准化

`jurisdiction_type` 与 `court_level` 综合使用 CourtListener court ID、jurisdiction code、法院名称和
court metadata。规范化值适合过滤，但 `jurisdiction_raw`、`raw_json` 仍是最终溯源依据。

## 5. Taxonomy 与 Feature 标注

体系回答不同问题：

1. Practice Area：宽泛执业领域；
2. Matter Type：具体案件/争议/程序类型；
3. Legal Issue：当前法院实际处理的较窄法律问题；
4. Matter Type Feature：当前 Opinion 明确支持的事实、金额、日期、主体和结果。

Matter Type projection 最终覆盖 20,000 cases。Feature jobs 的 annotation source 分布保存在数据库，
主要初标模型为 `gpt-5.4-mini`，并使用 `gpt-5.4-review`、`gpt-5.5-review`、`gpt-5.6-review` 和少量
人工复核处理失败/高风险记录。模型输出经过 JSON schema、evidence scope、closed enum、数值单位、
actor/polarity 和 cross-layer contradiction 等确定性检查。

标注属于 Silver research annotation。置信度来自流程，不是经大规模人工 Gold 校准的概率。

## 6. 分类设计参考

| 参考 | 实际作用 | 不应误解为 |
|---|---|---|
| U.S. Courts Nature of Suit / Civil Cover Sheet | 联邦民事案件类型表达与边界参考 | 本项目 Matter Type 的直接复制 |
| SALI LMSS | 术语规范化和未来外部映射参考 | 普通查询必需字段或 Gold ontology |
| CourtListener metadata/text | 法院、文书和当前案件 evidence | 自动正确的法律分类 |
| 项目 Registry | 最终 canonical ID、定义、include/exclude 和 Feature membership | 通用美国法院官方标准 |

参考链接：

- https://www.uscourts.gov/forms-rules/forms/civil-cover-sheet
- https://github.com/sali-legal/LMSS

## 7. Query 设计参考

描述型 Query 的计数、比例和比较维度参考 U.S. Courts、FJC、NCSC 和 BJS 的司法统计实践；这些
机构不提供本 Benchmark 答案。具体来源记录在 `query/descriptive_query/authority_sources.json`。

## 8. 已知限制

- `citations_json` 全部为空；citation-network 研究需要补充独立来源。
- Practice Area 覆盖 91.03%，Legal Issue 覆盖 59.32%；二者不应强行补全。
- Matter Type 100% 是 projection coverage，不是 Gold accuracy。
- Feature 只对选定 Matter Type/案件运行；未运行与 `not_mentioned` 的语义不同。
- Hybrid Benchmark qrels 是 partial pool，可能存在未发现的相关案例。
- 采样、CourtListener 收录范围和 Opinion 可得性都会影响年份与法院分布。

## 9. 可复现与引用

根 `manifest.json` 记录所有发布文件的 SHA256。数据库内部
`annotation_registry_snapshot` 保存 Registry 内容与校验和，`annotation_release` 保存版本链路。
研究报告至少应注明：Legal Bench v3.1、CourtListener snapshot 2026-06-30、数据库 SHA256、使用的
Query split 和 Benchmark v6。
