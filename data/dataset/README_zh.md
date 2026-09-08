# 集成 Legal RAG 数据库 v3.1

本目录把 CourtListener 20k 完整案例语料、v3.3 Matter Type 和 v1.1 Matter Type Feature 标注
放在同一个 SQLite 数据库中。数据库直接包含 21,261 份 Opinion 正文，不需要另行下载文书。

## 恢复

在仓库根目录执行：

```bash
./scripts/restore_integrated_db.sh
```

脚本会合并 4 个压缩分片，验证压缩包和数据库 SHA256，恢复
`data/dataset/legal_rag_dataset_v3.db`，并运行 `PRAGMA quick_check`。

## 说明文件

- `SCHEMA.sql`：可执行的数据库 Schema。
- `FIELD_CATALOG.json`：自动生成的字段类型、约束、主外键、索引和行数。
- `FIELD_DICTIONARY_en.md` / `FIELD_DICTIONARY_zh.md`：逐表字段业务含义。
- `COVERAGE_REPORT.json`：从本发布数据库直接计算的覆盖率和分布。
- `manifest.json`：数据库、分片校验和、版本及数据量。

恢复后请以只读方式打开，不要直接修改发布副本。
