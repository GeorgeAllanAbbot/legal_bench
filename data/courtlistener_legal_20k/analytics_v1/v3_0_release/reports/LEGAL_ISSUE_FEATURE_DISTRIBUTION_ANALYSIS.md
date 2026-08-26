# Legal Issue Feature Result Analysis

Generated: `2026-08-26T16:55:27.569178+00:00`

## Executive Summary

- Feature jobs: `9023`
- Feature job cases: `9023`
- Valid / needs_review / failed: `9023` / `0` / `0`
- Cases with decided Legal Issue: `8152`
- Cases with at least one present feature: `8461`
- Projection cases: `20000`
- Projection cases with Legal Issue: `15259`
- Feature coverage vs all projection cases: `45.12%`
- Feature coverage vs projected Legal-Issue cases: `59.13%`

## Repair Source Distribution

- `legal_issue_feature_full_v1_16k`: `8707`
- `legal_issue_feature_full_v1_16k_gpt54_review`: `302`
- `legal_issue_feature_full_v1_16k_gpt55_needs_review`: `9`
- `legal_issue_feature_full_v1_16k_gpt56sol_needs_review_final`: `3`
- `legal_issue_feature_full_v1_16k_gpt55_failed_review`: `1`
- `legal_issue_feature_full_v1_16k_gpt56sol_failed_final`: `1`

## Issue Status Distribution

- `decided`: `10234`
- `false_match`: `623`
- `raised_not_decided`: `396`
- `background_only`: `373`
- `not_reached`: `204`
- `quoted_authority`: `2`

## Feature Status Distribution

- `present`: `34306`
- `not_mentioned`: `14062`
- `not_applicable`: `1513`
- `absent`: `431`
- `uncertain`: `102`

## Top Legal Issues In Feature Jobs

- `subject_matter_jurisdiction`: `2220`
- `harmless_error`: `1597`
- `pleading_sufficiency`: `1022`
- `statute_of_limitations`: `808`
- `mootness`: `714`
- `standing`: `628`
- `sufficiency_of_evidence`: `513`
- `expert_testimony`: `292`
- `service_of_process`: `271`
- `relevance_prejudice_balancing`: `262`
- `arbitration_enforceability`: `253`
- `insurance_coverage_trigger`: `252`
- `claim_preclusion`: `242`
- `personal_jurisdiction`: `220`
- `removal_and_remand`: `209`
- `character_evidence`: `195`
- `hearsay`: `194`
- `issue_preclusion_collateral_estoppel`: `163`
- `evidence_authentication`: `149`
- `ineffective_assistance_of_counsel`: `128`
- `confrontation_clause`: `124`
- `tax_deduction`: `107`
- `class_certification`: `106`
- `insurance_duty_to_indemnify`: `98`
- `weight_of_the_evidence`: `94`
- `insurance_policy_exclusion`: `92`
- `insurance_duty_to_defend`: `84`
- `double_jeopardy`: `76`
- `insurance_bad_faith`: `63`
- `attorney_client_privilege`: `52`

## Top Present Features

- `jurisdiction_basis`: `1999`
- `subject_matter_jurisdiction_result`: `1948`
- `jurisdiction_defect`: `1617`
- `error_type`: `1217`
- `harmless_error_result`: `985`
- `pleading_result`: `964`
- `pleading_defect`: `903`
- `challenged_claim`: `871`
- `limitations_result`: `776`
- `harmless_error_standard`: `680`
- `trigger_date_or_event`: `677`
- `limitations_period`: `671`
- `tolling_or_accrual_rule`: `631`
- `error_preservation_status`: `617`
- `filing_date`: `595`
- `mootness_event`: `521`
- `standing_party`: `511`
- `challenged_offense_or_claim`: `505`
- `sufficiency_result`: `501`
- `evidence_relied_on`: `484`
- `sufficiency_standard`: `473`
- `mootness_result`: `472`
- `standing_result`: `438`
- `challenged_element`: `407`
- `evidence_item`: `390`
- `leave_to_amend`: `347`
- `policy_type`: `330`
- `prior_case_or_judgment`: `320`
- `challenge_basis`: `271`
- `expert_testimony_result`: `261`

## Top Feature Keys

- `jurisdiction_basis`: `2222`
- `jurisdiction_defect`: `2220`
- `amount_in_controversy`: `2220`
- `subject_matter_jurisdiction_result`: `2220`
- `error_type`: `1597`
- `error_preservation_status`: `1597`
- `harmless_error_standard`: `1597`
- `harmless_error_result`: `1597`
- `challenged_claim`: `1022`
- `pleading_defect`: `1022`
- `leave_to_amend`: `1022`
- `pleading_result`: `1022`
- `limitations_period`: `861`
- `trigger_date_or_event`: `861`
- `filing_date`: `861`
- `tolling_or_accrual_rule`: `861`
- `limitations_result`: `860`
- `mootness_exception`: `715`
- `mootness_event`: `714`
- `mootness_result`: `714`
- `standing_party`: `628`
- `injury_in_fact`: `628`
- `causation`: `628`
- `redressability`: `628`
- `standing_result`: `628`
- `challenged_offense_or_claim`: `513`
- `challenged_element`: `513`
- `evidence_relied_on`: `513`
- `sufficiency_standard`: `513`
- `sufficiency_result`: `513`

## Evidence Distribution

### Role
- `court_analysis`: `39420`
- `court_holding`: `18309`
- `case_background`: `6221`
- `party_argument`: `963`
- `procedural_history`: `515`
- `court_background`: `72`
- `caption`: `68`
- `court_finding`: `27`
- `unknown`: `2`
- `case_analysis`: `1`
- `case_holding`: `1`
- `court_action`: `1`

### Assertion Scope
- `court_holding`: `30154`
- `court_finding`: `19832`
- `case_fact`: `9537`
- `legal_standard`: `3605`
- `party_allegation`: `1719`
- `statutory_definition`: `307`
- `court_analysis`: `203`
- `quoted_other_case`: `82`
- `case_finding`: `57`
- `court_standard`: `21`
- `court_fact`: `18`
- `current_case`: `18`
- `party_argument`: `17`
- `case_holding`: `11`
- `citation_parenthetical`: `8`
- `policy_text`: `3`
- `procedural_history`: `3`
- `unknown`: `2`
- `case_analysis`: `1`
- `policy_contract_text`: `1`
- `quoted_authority`: `1`

## Projection Distribution

### Practice Area
- `criminal_law`: `5983`
- `administrative_law`: `1811`
- `civil_rights_law`: `1655`
- `tort_law`: `1389`
- `labor_employment_law`: `1251`
- `family_law`: `1145`
- `real_property_law`: `1128`
- `contract_law`: `904`
- `commercial_law`: `788`
- `insurance_law`: `674`
- `immigration_law`: `488`
- `health_law`: `488`
- `bankruptcy_law`: `409`
- `tax_law`: `370`
- `other`: `338`
- `intellectual_property_law`: `292`
- `consumer_law`: `211`
- `trusts_estates_probate_law`: `183`
- `education_law`: `111`
- `securities_law`: `95`
- `environmental_law`: `95`
- `admiralty_maritime_law`: `69`
- `antitrust_competition_law`: `53`

### Matter Type
- `sentencing_guideline_dispute`: `2041`
- `drug_offense`: `863`
- `section_1983_claim`: `834`
- `negligence_personal_injury`: `738`
- `benefits_review`: `567`
- `breach_of_contract`: `522`
- `firearm_offense`: `458`
- `final_agency_action`: `421`
- `prisoner_rights`: `403`
- `employment_discrimination`: `398`
- `custody_visitation`: `325`
- `parentage_adoption`: `302`
- `support_obligation`: `285`
- `tax_liability_dispute`: `253`
- `apa_review`: `248`
- `title_boundary_easement`: `244`
- `foreclosure_mortgage`: `243`
- `asylum_protection`: `234`
- `employment_retaliation`: `187`
- `custodial_interrogation`: `185`
- `auto_insurance_coverage`: `174`
- `wage_hour_dispute`: `158`
- `corporate_governance_dispute`: `155`
- `landlord_tenant_eviction`: `152`
- `exhaustion_or_timeliness`: `149`

## Confidence

```json
{
  "count": 50414,
  "min": 0.0,
  "p25": 0.88,
  "median": 0.95,
  "p75": 0.98,
  "max": 1.0,
  "mean": 0.835
}
```

## Numeric Feature Summaries

- `amount_in_controversy`: `{"count": 73, "min": 50.0, "p25": 75000.0, "median": 75000.0, "p75": 91910.42, "max": 88000000000.0, "mean": 1207242151.512}`
- `limitations_period`: `{"count": 102, "min": 1.0, "p25": 2.0, "median": 4.0, "p75": 30.0, "max": 365.0, "mean": 39.745}`
- `limit_amount`: `{"count": 2, "min": 20000.0, "p25": 20000.0, "median": 20000.0, "p75": 20000.0, "max": 85000.0, "mean": 52500.0}`
- `number_of_occurrences_or_claims`: `{"count": 2, "min": 1.0, "p25": 1.0, "median": 1.0, "p75": 1.0, "max": 1.0, "mean": 1.0}`
- `subrogation_amount`: `{"count": 10, "min": 2000.0, "p25": 10000.0, "median": 59000.0, "p75": 872762.02, "max": 3882571.19, "mean": 803853.851}`
