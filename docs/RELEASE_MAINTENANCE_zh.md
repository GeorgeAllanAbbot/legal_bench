# 发布维护规范

## 冻结范围

每次发布必须同时冻结 taxonomy Registry、feature Registry、标注数据、报告和 manifest。不能只更新 Registry 而不重新生成受影响的标注；如不重跑，必须提供明确的兼容迁移记录。

## 必须执行的检查

1. 逐行解析所有 JSONL。
2. 按数据类型检查 `case_id` 或 `job_id` 唯一性。
3. 重新计算记录数、压缩大小和 `manifest.json` 中的 SHA-256。
4. 重新计算每个 feature 的非 `not_mentioned` 有效数。
5. 明确记录缺失任务和复核 lineage，禁止静默删除。
6. 检查所有 canonical ID 都存在于冻结 Registry。
7. 发布前运行 contradiction 和 assertion-scope validator。

## 版本规则

- Major：不兼容的数据结构变化或 taxonomy 层级语义变化。
- Minor：增加 canonical ID 或 feature，且旧字段保持兼容。
- Patch：不改变标注结果的文档、计数或元数据修正。

Query template 和字段目录只是查询接口，不是 benchmark gold question。后续 benchmark 应单独版本化问题、预期 case ID、可执行查询计划和回答 provenance。
