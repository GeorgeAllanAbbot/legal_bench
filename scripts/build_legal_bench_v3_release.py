#!/usr/bin/env python3
"""Build a clean Legal Bench v3.0 release package.

The release package intentionally excludes caches, SQLite databases,
checkpoints, smoke runs, and provider logs. It contains final merged annotations,
summary/distribution reports, registry snapshots, and bilingual documentation.
"""

from __future__ import annotations

import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ANALYTICS = ROOT / "data/courtlistener_legal_20k/analytics_v1"
TAXONOMY = ANALYTICS / "taxonomy_v3"
RUNS = ANALYTICS / "feature_full_runs"
RELEASE = ANALYTICS / "v3_0_release"


ISSUE_ZH = {
    "due_process": "正当程序",
    "equal_protection": "平等保护",
    "free_exercise_of_religion": "宗教自由行使",
    "free_speech": "言论自由",
    "search_and_seizure": "搜查与扣押",
    "custodial_interrogation_self_incrimination": "羁押讯问与自证其罪",
    "right_to_counsel": "律师帮助权",
    "tax_deduction": "税前扣除",
    "insurance_coverage_trigger": "保险责任触发",
    "insurance_policy_interpretation": "保险合同解释",
    "insurance_policy_exclusion": "保险除外条款",
    "insurance_duty_to_defend": "保险人抗辩义务",
    "insurance_duty_to_indemnify": "保险人赔偿义务",
    "insurance_notice_compliance": "保险通知合规",
    "insurance_cooperation_clause": "保险协助条款",
    "insurance_misrepresentation_rescission": "保险虚假陈述与撤销",
    "insurance_bad_faith": "保险恶意理赔",
    "insurance_claim_handling_duties": "保险理赔处理义务",
    "insurance_limit_interpretation": "保险限额解释",
    "insurance_allocation_between_insurers": "保险人之间责任分配",
    "insurance_additional_insured_status": "附加被保险人身份",
    "insurance_subrogation_right": "保险代位求偿权",
    "insurance_waiver_estoppel": "保险弃权与禁反言",
    "personal_jurisdiction": "属人管辖权",
    "subject_matter_jurisdiction": "事项管辖权",
    "venue_transfer": "审判地点移送",
    "removal_and_remand": "移送联邦法院与发回州法院",
    "standing": "诉讼资格",
    "mootness": "争议已失实效",
    "claim_preclusion": "请求排除/既判力",
    "issue_preclusion_collateral_estoppel": "争点排除/附带禁反言",
    "class_certification": "集体诉讼认证",
    "pleading_sufficiency": "诉状充分性",
    "service_of_process": "送达程序",
    "statute_of_limitations": "诉讼时效",
    "arbitration_enforceability": "仲裁条款可执行性",
    "attorney_client_privilege": "律师-客户特权",
    "work_product_protection": "律师工作成果保护",
    "discovery_scope": "证据开示范围",
    "hearsay": "传闻证据",
    "expert_testimony": "专家证言",
    "evidence_authentication": "证据认证",
    "character_evidence": "品格证据",
    "relevance_prejudice_balancing": "相关性与不公平偏见权衡",
    "confrontation_clause": "对质权",
    "harmless_error": "无害错误",
    "sufficiency_of_evidence": "证据充分性",
    "ineffective_assistance_of_counsel": "律师帮助无效",
    "anders_review": "Anders 审查",
    "double_jeopardy": "双重危险",
    "certificate_of_appealability": "上诉许可证明",
    "habeas_exhaustion": "人身保护令救济穷尽",
    "lesser_included_offense_instruction": "较轻包含罪指示",
    "qualified_immunity": "合格豁免",
    "supplemental_jurisdiction": "补充管辖权",
    "plra_exhaustion": "PLRA 救济穷尽",
    "younger_abstention": "Younger 回避原则",
    "rooker_feldman": "Rooker-Feldman 原则",
    "judicial_immunity": "司法豁免",
    "dismissal_for_failure_to_prosecute": "因未推进诉讼而驳回",
    "weight_of_the_evidence": "证据权重审查",
    "sentencing_reasonableness": "量刑合理性",
}


COMMON_ZH = {
    "Issue Status": "争点处理状态",
    "Issue-Specific Outcome": "争点具体结果",
    "Issue Target": "争点对象",
    "Current Court Action": "当前法院动作",
    "Decision Basis": "裁判理由",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def feature_label_zh(feature: dict[str, Any]) -> str:
    return feature.get("label_zh") or COMMON_ZH.get(feature.get("label")) or feature.get("label") or feature.get("preferred_label") or feature.get("feature_key")


def issue_zh(issue_id: str, fallback: str) -> str:
    return ISSUE_ZH.get(issue_id) or fallback


def build_catalogs() -> dict[str, Any]:
    issue_registry = load_json(TAXONOMY / "legal_issue_registry_v3.json")
    feature_packs = load_json(TAXONOMY / "legal_issue_feature_packs_v1.json")
    feature_registry = load_json(TAXONOMY / "analytical_feature_registry_v1_3.json")

    packs_by_issue = {pack["issue_id"]: pack for pack in feature_packs["packs"]}
    feature_to_issues: dict[str, list[str]] = defaultdict(list)
    issue_rows = []

    for issue in issue_registry["entries"]:
        issue_id = issue["issue_id"]
        pack = packs_by_issue.get(issue_id)
        pack_features = []
        if pack:
            for group, items in (
                ("core", pack.get("core_features", [])),
                ("issue_specific", pack.get("issue_features", [])),
            ):
                for feature in items:
                    key = feature["feature_key"]
                    feature_to_issues[key].append(issue_id)
                    pack_features.append({
                        "feature_key": key,
                        "label_en": feature.get("label") or feature.get("preferred_label") or key,
                        "label_zh": feature_label_zh(feature),
                        "group": group,
                        "data_type": feature.get("data_type"),
                        "required": bool(feature.get("required")),
                        "allowed_values": feature.get("allowed_values", []),
                        "definition_en": feature.get("definition", ""),
                    })
        issue_rows.append({
            "issue_id": issue_id,
            "label_en": issue.get("preferred_label") or issue_id,
            "label_zh": issue_zh(issue_id, issue.get("preferred_label") or issue_id),
            "namespace": issue.get("namespace"),
            "status": issue.get("status", "active"),
            "searchable": issue.get("searchable", bool(pack)),
            "definition_en": issue.get("scope_note", ""),
            "definition_zh": zh_issue_definition(issue_id, issue.get("scope_note", "")),
            "include_when_en": issue.get("include_when", []),
            "exclude_when_en": issue.get("exclusions", []),
            "allowed_specific_outcomes": issue.get("allowed_specific_outcomes", []),
            "feature_pack_id": pack.get("feature_pack_id") if pack else None,
            "features": pack_features,
            "deprecation_reason": issue.get("deprecation_reason", ""),
        })

    feature_rows = []
    for feature in feature_registry["entries"]:
        key = feature["feature_key"]
        feature_rows.append({
            "feature_key": key,
            "label_en": feature.get("preferred_label") or key,
            "label_zh": feature_label_zh(feature),
            "data_type": feature.get("data_type"),
            "definition_en": feature.get("definition", ""),
            "definition_zh": zh_feature_definition(feature),
            "tier": feature.get("tier"),
            "production_status": feature.get("production_status"),
            "outcome_feature": feature.get("outcome_feature", False),
            "extraction_method": feature.get("extraction_method"),
            "required_evidence_roles": feature.get("required_evidence_roles", []),
            "allowed_assertion_scopes": feature.get("allowed_assertion_scopes", []),
            "forbidden_assertion_scopes": feature.get("forbidden_assertion_scopes", []),
            "allowed_values": feature.get("allowed_values", []),
            "included_in_legal_issues": sorted(set(feature_to_issues.get(key, []))),
            "applies_to": feature.get("applies_to", {}),
            "include_when": feature.get("include_when", []),
            "exclude_when": feature.get("exclude_when", []),
        })

    return {
        "issues": issue_rows,
        "features": feature_rows,
        "metadata": {
            "issue_count": len(issue_rows),
            "feature_count": len(feature_rows),
            "feature_pack_count": len(feature_packs["packs"]),
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
    }


def zh_issue_definition(issue_id: str, scope_note: str) -> str:
    label = ISSUE_ZH.get(issue_id)
    if label:
        return f"用于标注法院是否实际处理了“{label}”这一法律争点。仅在当前案件意见书中有法院分析、裁判结论或明确争点处理时使用。"
    return f"用于标注法院是否实际处理该法律争点。英文范围说明：{scope_note}"


def zh_feature_definition(feature: dict[str, Any]) -> str:
    label = feature_label_zh(feature)
    method = feature.get("extraction_method") or "规则或 LLM 抽取"
    return f"抽取“{label}”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：{method}。"


def md_table_escape(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = ", ".join(str(x) for x in value)
    elif isinstance(value, dict):
        value = json.dumps(value, ensure_ascii=False)
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_issue_md_en(path: Path, issues: list[dict[str, Any]]) -> None:
    lines = [
        "# Legal Issue Catalog v3.0",
        "",
        "This catalog defines the legal questions used by the Legal Bench v3.0 analytical feature layer.",
        "",
        "Each Legal Issue is a directly reviewable legal question. Broad or ambiguous concepts are retained as deprecated entries when they are useful historically but should not be used as searchable final labels.",
        "",
    ]
    for issue in issues:
        lines += [
            f"## `{issue['issue_id']}` — {issue['label_en']}",
            "",
            f"- Chinese label: {issue['label_zh']}",
            f"- Namespace: `{issue.get('namespace') or ''}`",
            f"- Status: `{issue.get('status') or 'active'}`",
            f"- Searchable: `{issue.get('searchable')}`",
            f"- Definition: {issue.get('definition_en') or ''}",
            f"- Allowed outcomes: `{', '.join(issue.get('allowed_specific_outcomes') or [])}`",
            f"- Feature pack: `{issue.get('feature_pack_id') or ''}`",
        ]
        if issue.get("exclude_when_en"):
            lines.append(f"- Exclude when: {md_table_escape(issue['exclude_when_en'])}")
        if issue.get("deprecation_reason"):
            lines.append(f"- Deprecation reason: {issue['deprecation_reason']}")
        lines += ["", "| Feature | Label | Group | Type | Required |", "|---|---|---|---|---|"]
        for f in issue.get("features") or []:
            lines.append(
                f"| `{f['feature_key']}` | {md_table_escape(f['label_en'])} | `{f['group']}` | `{f.get('data_type') or ''}` | `{f.get('required')}` |"
            )
        if not issue.get("features"):
            lines.append("|  | No production feature pack. |  |  |  |")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_issue_md_zh(path: Path, issues: list[dict[str, Any]]) -> None:
    lines = [
        "# Legal Issue Catalog v3.0（中文）",
        "",
        "本目录说明 Legal Bench v3.0 中 Legal Issue 层的标签。Legal Issue 表示法院实际处理的法律争点，而不是案由、事实主题或当事人单方主张。",
        "",
        "原则：候选标签不等于最终标签；最终标签需要当前案件 opinion 中的法院分析、法院 holding 或明确裁判对象支持。",
        "",
    ]
    for issue in issues:
        lines += [
            f"## `{issue['issue_id']}` — {issue['label_zh']}",
            "",
            f"- English label: {issue['label_en']}",
            f"- 命名空间：`{issue.get('namespace') or ''}`",
            f"- 状态：`{issue.get('status') or 'active'}`",
            f"- 是否进入检索层：`{issue.get('searchable')}`",
            f"- 中文定义：{issue.get('definition_zh') or ''}",
            f"- 英文范围：{issue.get('definition_en') or ''}",
            f"- 允许结果：`{', '.join(issue.get('allowed_specific_outcomes') or [])}`",
            f"- 对应 feature pack：`{issue.get('feature_pack_id') or ''}`",
        ]
        if issue.get("exclude_when_en"):
            lines.append(f"- 排除边界：{md_table_escape(issue['exclude_when_en'])}")
        if issue.get("deprecation_reason"):
            lines.append(f"- 废弃/不建议直接检索原因：{issue['deprecation_reason']}")
        lines += ["", "| Feature | 中文名 | 分组 | 类型 | 必填 |", "|---|---|---|---|---|"]
        for f in issue.get("features") or []:
            lines.append(
                f"| `{f['feature_key']}` | {md_table_escape(f['label_zh'])} | `{f['group']}` | `{f.get('data_type') or ''}` | `{f.get('required')}` |"
            )
        if not issue.get("features"):
            lines.append("|  | 无生产级 feature pack。 |  |  |  |")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_feature_md_en(path: Path, features: list[dict[str, Any]]) -> None:
    lines = [
        "# Analytical Feature Catalog v3.0",
        "",
        "This catalog defines the structured fields extracted from opinions for Legal Bench v3.0.",
        "",
        "| Feature | Label | Type | Tier | Production status | Included in Legal Issues | Definition |",
        "|---|---|---|---|---|---|---|",
    ]
    for f in features:
        lines.append(
            f"| `{f['feature_key']}` | {md_table_escape(f['label_en'])} | `{f.get('data_type') or ''}` | `{f.get('tier') or ''}` | `{f.get('production_status') or ''}` | {md_table_escape(f.get('included_in_legal_issues') or [])} | {md_table_escape(f.get('definition_en') or '')} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_feature_md_zh(path: Path, features: list[dict[str, Any]]) -> None:
    lines = [
        "# Analytical Feature Catalog v3.0（中文）",
        "",
        "本目录定义从美国判例 opinion 中抽取的结构化字段。每个字段都必须有文本证据；若 opinion 未提及，应标记为 not_mentioned 或 not_applicable，而不是猜测。",
        "",
        "| Feature | 中文名 | 类型 | 层级 | 生产状态 | 包含于 Legal Issues | 中文说明 |",
        "|---|---|---|---|---|---|---|",
    ]
    for f in features:
        lines.append(
            f"| `{f['feature_key']}` | {md_table_escape(f['label_zh'])} | `{f.get('data_type') or ''}` | `{f.get('tier') or ''}` | `{f.get('production_status') or ''}` | {md_table_escape(f.get('included_in_legal_issues') or [])} | {md_table_escape(f.get('definition_zh') or '')} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readmes(summary: dict[str, Any]) -> None:
    readme_en = RELEASE / "README.md"
    readme_zh = RELEASE / "README_zh.md"
    readme_en.write_text(f"""# Legal Bench v3.0 Release

This directory is the cleaned v3.0 release package for the CourtListener-based Legal Bench dataset work.

## Contents

- `data/legal_issue_feature_full_v1_16k_final_merged.json`: final merged Legal Issue feature annotations.
- `data/legal_issue_feature_full_v1_16k_final_merged.summary.json`: final annotation summary.
- `reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md`: distribution analysis.
- `reports/legal_issue_feature_full_v1_16k_distribution_analysis.json`: machine-readable distribution analysis.
- `registry/`: registry snapshots used by this release.
- `docs/LEGAL_ISSUE_CATALOG_en.md`: Legal Issue definitions and feature-pack membership.
- `docs/FEATURE_CATALOG_en.md`: analytical feature definitions and inclusion mapping.

## Current Status

- Total feature jobs: `{summary['total_jobs']}`
- Valid jobs: `{summary['status_counts'].get('valid', 0)}`
- Needs review: `{summary['status_counts'].get('needs_review', 0)}`
- Failed: `{summary['status_counts'].get('failed', 0)}`
- Manual review items: `{summary['manual_review_count']}`

## Excluded From Git

Large SQLite databases, provider caches, checkpoint logs, smoke runs, and raw intermediate runs are intentionally excluded from this clean release package.
""", encoding="utf-8")
    readme_zh.write_text(f"""# Legal Bench v3.0 发布包

本目录是 CourtListener 英文法律案例数据项目的 v3.0 清洗版发布包。

## 内容

- `data/legal_issue_feature_full_v1_16k_final_merged.json`：最终合并后的 Legal Issue feature 标注。
- `data/legal_issue_feature_full_v1_16k_final_merged.summary.json`：最终标注摘要。
- `reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md`：结果与分布分析。
- `reports/legal_issue_feature_full_v1_16k_distribution_analysis.json`：机器可读分布分析。
- `registry/`：本版本使用的 taxonomy / feature registry 快照。
- `docs/LEGAL_ISSUE_CATALOG_zh.md`：Legal Issue 中文解释、包含关系和对应 feature pack。
- `docs/FEATURE_CATALOG_zh.md`：Feature 中文解释及其被哪些 Legal Issue 使用。

## 当前状态

- Feature jobs 总数：`{summary['total_jobs']}`
- Valid：`{summary['status_counts'].get('valid', 0)}`
- Needs review：`{summary['status_counts'].get('needs_review', 0)}`
- Failed：`{summary['status_counts'].get('failed', 0)}`
- 人工审阅剩余：`{summary['manual_review_count']}`

## 未纳入 Git 的内容

大型 SQLite 数据库、供应商缓存、checkpoint、日志、smoke run 和中间试跑结果不放入 v3.0 清洗发布包。它们仍保留在本地工作目录中。
""", encoding="utf-8")


def main() -> int:
    if RELEASE.exists():
        shutil.rmtree(RELEASE)
    (RELEASE / "data").mkdir(parents=True)
    (RELEASE / "reports").mkdir()
    (RELEASE / "registry").mkdir()
    (RELEASE / "docs").mkdir()

    catalogs = build_catalogs()
    write_json(RELEASE / "registry/legal_issue_catalog_v3_0.json", catalogs["issues"])
    write_json(RELEASE / "registry/feature_catalog_v3_0.json", catalogs["features"])
    write_json(RELEASE / "registry/catalog_manifest_v3_0.json", catalogs["metadata"])

    for name in [
        "legal_issue_registry_v3.json",
        "legal_issue_feature_packs_v1.json",
        "analytical_feature_registry_v1_3.json",
        "practice_area_registry_v3.json",
        "matter_type_registry_v3.json",
        "case_taxonomy_schema_v3.json",
    ]:
        copy_file(TAXONOMY / name, RELEASE / "registry/source" / name)

    copy_file(
        RUNS / "legal_issue_feature_full_v1_16k_final_merged.json",
        RELEASE / "data/legal_issue_feature_full_v1_16k_final_merged.json",
    )
    copy_file(
        RUNS / "legal_issue_feature_full_v1_16k_final_merged.summary.json",
        RELEASE / "data/legal_issue_feature_full_v1_16k_final_merged.summary.json",
    )
    copy_file(
        RUNS / "legal_issue_feature_full_v1_16k_distribution_analysis.json",
        RELEASE / "reports/legal_issue_feature_full_v1_16k_distribution_analysis.json",
    )
    copy_file(
        RUNS / "LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md",
        RELEASE / "reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md",
    )

    write_issue_md_en(RELEASE / "docs/LEGAL_ISSUE_CATALOG_en.md", catalogs["issues"])
    write_issue_md_zh(RELEASE / "docs/LEGAL_ISSUE_CATALOG_zh.md", catalogs["issues"])
    write_feature_md_en(RELEASE / "docs/FEATURE_CATALOG_en.md", catalogs["features"])
    write_feature_md_zh(RELEASE / "docs/FEATURE_CATALOG_zh.md", catalogs["features"])

    summary = load_json(RUNS / "legal_issue_feature_full_v1_16k_final_merged.summary.json")
    manifest = {
        "release": "legal_bench_v3.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "contents": {
            "final_annotation_json": "data/legal_issue_feature_full_v1_16k_final_merged.json",
            "summary_json": "data/legal_issue_feature_full_v1_16k_final_merged.summary.json",
            "distribution_report_md": "reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md",
            "legal_issue_catalog_en": "docs/LEGAL_ISSUE_CATALOG_en.md",
            "legal_issue_catalog_zh": "docs/LEGAL_ISSUE_CATALOG_zh.md",
            "feature_catalog_en": "docs/FEATURE_CATALOG_en.md",
            "feature_catalog_zh": "docs/FEATURE_CATALOG_zh.md",
        },
        "summary": summary,
        "catalogs": catalogs["metadata"],
    }
    write_json(RELEASE / "manifest.json", manifest)
    write_readmes(summary)
    print(json.dumps({
        "release_dir": str(RELEASE),
        "issue_count": catalogs["metadata"]["issue_count"],
        "feature_count": catalogs["metadata"]["feature_count"],
        "feature_pack_count": catalogs["metadata"]["feature_pack_count"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
