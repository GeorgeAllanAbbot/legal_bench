# Legal Bench v3：CourtListener 标注数据

Legal Bench v3 覆盖 20,000 条英文 CourtListener Opinion Cluster 案例，同时发布精简的纯标注版本和完整集成 SQLite 版本。仓库不包含向量、检索索引、提示词、供应商日志或模型密钥。

仓库现同时提供可选的**完整集成 SQLite 版本**，把 CourtListener v2 全文语料、v3 taxonomy 和 Matter Type Feature 标注合并在同一数据库。说明见 `data/integrated/README.md`，恢复命令为 `./scripts/restore_integrated_db.sh`。

## 标注层级

- **Practice Area（法律领域）**：案件所属的宽泛法律领域，例如 `criminal_law`、`tax_law`。
- **Matter Type（案件/争议类型）**：具体的案件、请求、争议或程序类型，也是选择分析特征包的主要依据。
- **Legal Issue（法律争点）**：法院实际处理的法律问题，不等同于案件类型分类。
- **Matter Type Features（案件类型特征）**：按照 Matter Type 抽取的事实、结果、日期、金额、比例、主体及其他结构化字段。

## 文件

- `data/taxonomy/case_taxonomy_v3.jsonl.xz`：20,000 条 case 级 taxonomy 标注。
- `data/features/matter_type_features_v1_1.jsonl.xz`：12,714 条 `case × Matter Type` 特征标注。
- `data/registry/`：本版本冻结使用的 Registry 与 schema。
- `data/reports/`：发布质量和覆盖率报告。
- `docs/ANNOTATION_SCHEMA_zh.md`：字段含义、关联方式和限制。
- `docs/MATTER_TYPE_FEATURE_REFERENCE_zh.md`：全部 feature key 及有效数量。
- `data/query/`：供后续 RAG 使用的可查询字段目录和英文 Query IR 模板。

## 解压与校验

```bash
./scripts/restore_annotations.sh
python3 scripts/verify_release.py
```

解压后的 JSONL 写入 Git 忽略的 `restored/` 目录。

## 与原始案例关联

通过 `case_id` 与另行获取的 CourtListener 数据关联。ID 使用标准化形式 `cluster_<CourtListener cluster id>`；feature 数据另有 `<case_id>::<matter_type_id>` 格式的 `job_id`。

## 使用范围

适用于检索约束、benchmark 构建、分层抽样、弱监督和结构化法律分析。该数据属于模型辅助研究标注，不是人工 gold label，也不构成法律意见。Taxonomy projection 保留了 9,284 条 `needs_review=true` 审计标记，高置信度统计应过滤或单独报告这些记录。重试后仍有 2 个预期 Matter Type feature job 被明确记录为缺失，详情见最终报告。
