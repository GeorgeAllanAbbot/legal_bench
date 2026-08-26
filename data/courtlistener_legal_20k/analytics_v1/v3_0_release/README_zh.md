# Legal Bench v3.0 发布包

本目录是 CourtListener 英文法律案例数据项目的 v3.0 清洗版发布包。

## 内容

- `data/legal_issue_feature_full_v1_16k_final_merged.json.xz`：最终合并后的 Legal Issue feature 标注压缩包。使用 `scripts/restore_v3_0_feature_annotations.sh` 还原。
- `data/legal_issue_feature_full_v1_16k_final_merged.summary.json`：最终标注摘要。
- `reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md`：结果与分布分析。
- `reports/legal_issue_feature_full_v1_16k_distribution_analysis.json`：机器可读分布分析。
- `registry/`：本版本使用的 taxonomy / feature registry 快照。
- `docs/LEGAL_ISSUE_CATALOG_zh.md`：Legal Issue 中文解释、包含关系和对应 feature pack。
- `docs/FEATURE_CATALOG_zh.md`：Feature 中文解释及其被哪些 Legal Issue 使用。

## 当前状态

- Feature jobs 总数：`9023`
- Valid：`9023`
- Needs review：`0`
- Failed：`0`
- 人工审阅剩余：`0`

## 未纳入 Git 的内容

大型 SQLite 数据库、供应商缓存、checkpoint、日志、smoke run 和中间试跑结果不放入 v3.0 清洗发布包。它们仍保留在本地工作目录中。

## 还原最终标注 JSON

```bash
./scripts/restore_v3_0_feature_annotations.sh
```
