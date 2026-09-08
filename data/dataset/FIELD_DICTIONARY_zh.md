# SQLite 字段字典

本文件解释业务语义；`FIELD_CATALOG.json` 是从发布数据库 `PRAGMA` 自动生成的完整机器可读目录，
包含每个字段的 SQLite 类型、顺序、默认值、非空约束、主键位置、外键和索引。

## 通用约定

- `*_json`：以 JSON 文本存储的数组或对象，读取后再 `json.loads()`；空数组通常为 `[]`。
- `case_id`：本项目案例主键，格式为 `cluster_<CourtListener cluster id>`。
- `cluster_id`：CourtListener Opinion Cluster 原始标识，用于关联 case 与 opinion。
- `opinion_id`：CourtListener Opinion 标识；一个 cluster 可以有多份 opinion。
- `document_id`：本项目生成的检索 chunk 标识，不等于 opinion ID。
- `confidence`：0–1 的模型/规则置信度，不是概率校准后的正确率。
- `raw_json`：来源记录；`provenance_json`：来源文件和处理链路。

## `dim_court`：法院维表

| 字段 | 含义 |
|---|---|
| `court_id` | CourtListener 法院主键 |
| `court_name`, `court_name_short` | 法院全名和简称 |
| `jurisdiction_raw` | CourtListener 原始 jurisdiction code/value |
| `jurisdiction_type` | 规范化辖区：`federal`、`state`、`administrative`、`other` |
| `court_level` | 法院层级，如 `federal_appellate`、`federal_district`、`state_supreme`、`state_appellate` |
| `circuit` | 联邦巡回区；不适用时为空 |
| `state_code` | 两位州/地区代码；不适用时为空 |
| `is_active` | CourtListener 记录的法院是否仍活跃 |
| `start_date`, `end_date` | 法院存续时间元数据 |
| `raw_json`, `provenance_json` | 原始法院记录和来源追踪 |

## `case_record`：案例/Opinion Cluster

| 字段 | 含义 |
|---|---|
| `case_id` | 本项目案例主键 |
| `cluster_id` | CourtListener Opinion Cluster ID，唯一 |
| `docket_id`, `docket_number` | Docket 关联标识和展示编号 |
| `court_id` | 外键到 `dim_court` |
| `case_name` | 规范化案例名称 |
| `case_name_docket` | Docket 来源的备选案名 |
| `decision_date`, `decision_year` | Opinion/cluster 裁判日期与派生年份；Benchmark 时间筛选使用该年份 |
| `citations_json` | 引证数组；本快照全部为空，不能用于 citation benchmark |
| `publication_status_raw` | CourtListener 原始发布状态 |
| `precedential_status` | 规范化状态，如 `published`、`unpublished`、`unknown` |
| `source` | CourtListener cluster 的来源字段 |
| `judges_raw` | 未拆分的法官信息 |
| `syllabus` | 来源提供的 syllabus/headnote，允许为空 |
| `posture` | 来源提供的程序姿态文本 |
| `procedural_history` | 来源提供的程序历史文本 |
| `jurisdiction_type`, `court_level` | 从法院维表投影的常用过滤字段 |
| `opinion_ids_json` | 该 cluster 下的 Opinion ID 数组 |
| `raw_json`, `provenance_json` | 原始 cluster 记录和来源追踪 |

## `opinion_record`：Opinion 文书

| 字段 | 含义 |
|---|---|
| `opinion_id` | Opinion 主键 |
| `cluster_id` | 关联 `case_record.cluster_id` |
| `opinion_type_raw` | CourtListener 原始 Opinion type |
| `opinion_type` | 规范化类型：combined/lead/trial court/concurrence/dissent/rehearing 等 |
| `opinion_group` | 检索分组：majority-like、separate concurrence、dissent、procedural/unknown |
| `author_id` | CourtListener 作者/法官标识，可能为空 |
| `per_curiam` | 是否为 per curiam 文书 |
| `html_with_citations` | 原始 HTML-with-citations 来源文本 |
| `plain_text` | 原始 plain-text 来源文本 |
| `preferred_text` | 清洗后优先用于检索和 RAG 的完整正文 |
| `preferred_text_source` | `preferred_text` 选择自哪个来源字段 |
| `text_length` | `preferred_text` 字符数 |
| `text_sha1` | 文本内容 SHA-1，用于重复检查 |
| `cited_opinion_ids_json` | 来源提供的 cited Opinion ID 数组 |
| `has_usable_text` | 是否达到构建时可用正文质量门槛 |
| `quality_metrics_json` | 文本长度、字符和清洗质量指标 |
| `raw_json`, `provenance_json` | 原始 Opinion 记录和来源追踪 |

## `search_document`：检索 Chunk

| 字段 | 含义 |
|---|---|
| `document_id` | Chunk 主键 |
| `case_id`, `opinion_id`, `cluster_id` | 回连案例和原始 Opinion 的标识 |
| `case_name`, `court_id`, `court_level`, `jurisdiction_type` | 冗余检索过滤元数据 |
| `decision_date`, `decision_year`, `precedential_status`, `opinion_type` | 时间、先例状态和文书类型过滤字段 |
| `section_type` | 识别出的片段类型/位置 |
| `section_weight` | 构建时赋予 section 的检索权重 |
| `primary_topic` | v2 弱主题字段，允许为空 |
| `statutes_json` | v2 规则抽取的法条数组 |
| `chunk_index` | 同一 Opinion 内的 chunk 顺序 |
| `chunk_text` | 提供给 BM25、Dense 或 LLM 的文本 |
| `chunk_token_count` | 构建器估算的 token 数，不绑定特定商业 tokenizer |
| `bm25_text` | 供词法索引使用的文本版本 |
| `embedding_json` | 预留向量字段，发布库通常为空数组；向量应存独立索引 |

## `case_features`：v2 规则弱特征

| 字段 | 含义 |
|---|---|
| `case_id` | 一案一行主键 |
| `practice_area_json`, `primary_topic`, `secondary_topics_json` | 早期规则主题，不应替代 v3 taxonomy |
| `statutes_json`, `constitutional_provisions_json` | 正则抽取的法条和宪法条款 |
| `disposition_json` | Opinion 尾部规则提取的结果候选 |
| `primary_legal_issue`, `holding` | 早期预留字段，可能为空 |
| `relief_ordered_json`, `government_authority_direction` | 弱救济/政府方向候选 |
| `feature_source_json`, `confidence_json` | 提取方法和置信度 |
| `evidence_spans_json`, `rule_signals_json` | 命中位置、上下文和规则信号 |

## `case_taxonomy_v3`：每案最终 Taxonomy 投影

| 字段 | 含义 |
|---|---|
| `case_id` | 一案一行主键 |
| `annotation_status` | 整条标注状态；当前 20,000 条均为 `valid` |
| `primary_practice_area` | 主要 Practice Area，允许为空 |
| `secondary_practice_areas_json` | 次要 Practice Area 数组 |
| `matter_types_json` | Matter Type 对象数组；规范化统计优先连接专表 |
| `legal_issues_json` | 保留的 Legal Issue 对象数组 |
| `unmapped_matter_types_json`, `unmapped_legal_issues_json` | Registry 外候选，供审计而非直接搜索 |
| `needs_review` | 历史整案审核标记，不等同于每个子标签错误 |
| `review_applied`, `review_status` | 是否应用复核及复核结果 |
| `raw_annotation_json` | 完整模型/后处理输出，供审计 |

## `case_practice_area_v3`：规范化 Practice Area

| 字段 | 含义 |
|---|---|
| `case_id`, `practice_area` | 案例与 canonical area 的复合主键部分 |
| `area_role` | `primary` 或 `secondary` |
| `confidence` | 标签置信度 |
| `evidence_json` | 支持该领域的证据和来源 |

## `case_matter_type_v3`：规范化 Matter Type

| 字段 | 含义 |
|---|---|
| `case_id`, `matter_type` | 案例与 canonical Matter Type 的复合主键 |
| `practice_area` | Matter Type 所属上位领域；允许为空或使用 general 类型 |
| `confidence` | 投影置信度 |
| `needs_review` | 该 Matter Type 是否需要复核；最终发布为 0 |
| `evidence_json` | 当前案件支持证据和标注来源 |

一个 case 可有多个 Matter Type。Feature Pack 由 `matter_type` 选择，不由 Legal Issue 选择。

## `case_legal_issue_v3`：规范化 Legal Issue

| 字段 | 含义 |
|---|---|
| `case_id`, `issue_id` | 案例与 canonical issue 的复合主键 |
| `issue_status` | Issue 在当前 Opinion 中的处理状态 |
| `mention_confidence` | 文本确实提到该法律概念的置信度 |
| `adjudication_confidence` | 当前法院实际分析/裁判该问题的置信度 |
| `evidence_json` | 法院分析或 holding 等支持证据 |

Legal Issue 不追求全覆盖。未出现一行不能解释为法院明确否定该 issue。

## Matter Type Feature 三表

### `matter_type_feature_job_v1_1`

| 字段 | 含义 |
|---|---|
| `job_id` | `<case_id>::<matter_type>` 形式的任务主键 |
| `case_id`, `case_name` | 案例关联和显示名 |
| `annotation_source` | 初标/复核模型或人工复核链路 |
| `annotation_status` | `accepted` 或明确的 `missing` |
| `review_history_json`, `human_review_json` | 复核历史和人工决策 |
| `raw_annotation_json` | 原始完整标注结果 |

### `matter_type_annotation_v1_1`

| 字段 | 含义 |
|---|---|
| `job_id`, `case_id`, `matter_type` | 任务、案例和 Matter Type |
| `matter_occurrence` | 同案同类多个独立争议对象的序号 |
| `matter_status` | 该 matter 的状态 |
| `matter_target_json` | 该标注具体针对的请求、charge、合同、财产或其他对象 |

### `matter_type_feature_value_v1_1`

| 字段 | 含义 |
|---|---|
| `job_id`, `case_id`, `matter_type`, `matter_occurrence` | 回连具体 Matter occurrence |
| `feature_key` | Registry 中的 canonical Feature key |
| `feature_occurrence` | 同一 Feature 多值时的序号 |
| `value_status` | `present`、`absent`、`uncertain`、`not_mentioned`、`not_applicable` |
| `value_json` | 完整规范化值，适合数组/对象/日期等复杂类型 |
| `value_text` | 可直接筛选的文本/枚举值 |
| `value_number` | 可直接比较、聚合的数值 |
| `unit` | `USD`、`USD/month`、`days`、`percent` 等；数值查询必须同时检查单位 |
| `confidence` | 该值置信度 |
| `missing_reason` | 非 present 状态的原因 |
| `evidence_json` | 当前 Opinion 中直接支持该值的文本、位置和 scope |

Feature 的数据类型、单位、allowed values，以及 `Matter Type → Feature[]` / `Feature → Matter Type[]`
包含关系，见 `../registry/matter_type_feature_registry_v1_1.json` 和
`../docs/MATTER_TYPE_FEATURE_REFERENCE_zh.md`。

## 版本与 Registry 表

- `annotation_release`：`release_id`、taxonomy/feature version、创建时间、记录数和构建 metadata。
- `annotation_registry_snapshot`：Registry 名称、版本、SHA256 和完整 `content_json` 快照。
- `build_state`：v2 构建器的键值状态；`key` 为名称，`value` 为序列化状态值。

发布库已移除仅用于迁移的历史 backup 表。Registry 快照是解释标签和 Feature 的最终依据。
