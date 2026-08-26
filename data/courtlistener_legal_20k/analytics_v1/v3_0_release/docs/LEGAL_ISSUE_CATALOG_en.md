# Legal Issue Catalog v3.0

This catalog defines the legal questions used by the Legal Bench v3.0 analytical feature layer.

Each Legal Issue is a directly reviewable legal question. Broad or ambiguous concepts are retained as deprecated entries when they are useful historically but should not be used as searchable final labels.

## `due_process` — Due Process

- Chinese label: 正当程序
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Procedural or substantive due process under the Fifth or Fourteenth Amendment.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: General fairness language is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `equal_protection` — Equal Protection

- Chinese label: 平等保护
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Unequal governmental treatment and the applicable constitutional standard of review.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Generic equality language is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `free_exercise_of_religion` — Free Exercise Of Religion

- Chinese label: 宗教自由行使
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Government burden on religious exercise or practice.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Religious identity without a free-exercise dispute is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `free_speech` — Free Speech

- Chinese label: 言论自由
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Protection or regulation of speech, expression, association, or press.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: A reference to speaking or expression in ordinary language is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `search_and_seizure` — Search And Seizure

- Chinese label: 搜查与扣押
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Fourth Amendment search, seizure, warrant, reasonableness, or exclusion issues.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: A factual search without a contested legal issue is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `custodial_interrogation_self_incrimination` — Custodial Interrogation Self Incrimination

- Chinese label: 羁押讯问与自证其罪
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Miranda, custodial interrogation, silence, or the privilege against self-incrimination.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Exclude generic interviews with no custody or privilege issue.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `right_to_counsel` — Right To Counsel

- Chinese label: 律师帮助权
- Namespace: `substantive_law`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Access to counsel, invocation of counsel, appointment, or effective assistance.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: An attorney's appearance alone is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `tax_deduction` — Tax Deduction

- Chinese label: 税前扣除
- Namespace: `substantive_law`
- Status: `active_strict`
- Searchable: `True`
- Definition: Availability, amount, or denial of a tax deduction.
- Allowed outcomes: `allowed, disallowed, partially_allowed`
- Feature pack: `li_pack.tax_deduction`
- Exclude when: An accounting deduction outside tax law is excluded.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `taxpayer_type` | Taxpayer Type | `issue_specific` | `enum` | `False` |
| `tax_years` | Tax Years | `issue_specific` | `integer[]` | `False` |
| `deduction_type` | Deduction Type | `issue_specific` | `string[]` | `False` |
| `deduction_amount` | Deduction Amount | `issue_specific` | `money_object[]` | `False` |
| `tax_authority_position` | Tax Authority Position | `issue_specific` | `enum` | `False` |

## `insurance_coverage_trigger` — Insurance Coverage Trigger

- Chinese label: 保险责任触发
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an event, injury, offense, claim, or loss triggers coverage.
- Allowed outcomes: `triggered, not_triggered, unresolved`
- Feature pack: `li_pack.insurance_coverage_trigger`
- Exclude when: An insured event mentioned only as background is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `policy_type` | Policy Type | `issue_specific` | `enum` | `False` |
| `coverage_claim_type` | Coverage Claim Type | `issue_specific` | `enum[]` | `False` |
| `triggering_event` | Triggering Event | `issue_specific` | `string` | `False` |
| `loss_or_injury_type` | Loss or Injury Type | `issue_specific` | `string[]` | `False` |
| `trigger_result` | Trigger Result | `issue_specific` | `enum` | `False` |

## `insurance_policy_interpretation` — Insurance Policy Interpretation

- Chinese label: 保险合同解释
- Namespace: `insurance`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Construction of insurance policy language, definitions, ambiguity, or scope.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: The mere existence of a policy is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `insurance_policy_exclusion` — Insurance Policy Exclusion

- Chinese label: 保险除外条款
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Application, validity, or interpretation of a policy exclusion.
- Allowed outcomes: `applies, does_not_apply, unresolved`
- Feature pack: `li_pack.insurance_policy_exclusion`
- Exclude when: An exclusion listed but not analyzed is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `policy_type` | Policy Type | `issue_specific` | `enum` | `False` |
| `exclusion_type` | Exclusion Type | `issue_specific` | `string[]` | `False` |
| `excluded_loss_or_conduct` | Excluded Loss or Conduct | `issue_specific` | `string` | `False` |
| `exception_to_exclusion` | Exception to Exclusion | `issue_specific` | `string` | `False` |
| `exclusion_result` | Exclusion Result | `issue_specific` | `enum` | `False` |

## `insurance_duty_to_defend` — Insurance Duty To Defend

- Chinese label: 保险人抗辩义务
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an insurer owes or breached a duty to defend.
- Allowed outcomes: `owed, not_owed, unresolved`
- Feature pack: `li_pack.insurance_duty_to_defend`
- Exclude when: Defense counsel participation alone is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `insurer` | Insurer | `issue_specific` | `string` | `False` |
| `insured` | Insured | `issue_specific` | `string` | `False` |
| `underlying_claim_type` | Underlying Claim Type | `issue_specific` | `string[]` | `False` |
| `complaint_allegations_trigger` | Complaint Allegations Trigger | `issue_specific` | `enum` | `False` |
| `duty_to_defend_result` | Duty to Defend Result | `issue_specific` | `enum` | `False` |

## `insurance_duty_to_indemnify` — Insurance Duty To Indemnify

- Chinese label: 保险人赔偿义务
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an insurer owes or breached a duty to indemnify.
- Allowed outcomes: `owed, not_owed, unresolved`
- Feature pack: `li_pack.insurance_duty_to_indemnify`
- Exclude when: Generic indemnity outside insurance is excluded.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `insurer` | Insurer | `issue_specific` | `string` | `False` |
| `insured` | Insured | `issue_specific` | `string` | `False` |
| `liability_or_settlement_target` | Liability or Settlement Target | `issue_specific` | `string` | `False` |
| `indemnity_ripeness` | Indemnity Ripeness | `issue_specific` | `enum` | `False` |
| `duty_to_indemnify_result` | Duty to Indemnify Result | `issue_specific` | `enum` | `False` |

## `insurance_notice_compliance` — Insurance Notice Compliance

- Chinese label: 保险通知合规
- Namespace: `insurance`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Compliance with notice-of-claim, notice-of-loss, or notice-of-suit requirements.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Generic litigation notice is excluded.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `insurance_cooperation_clause` — Insurance Cooperation Clause

- Chinese label: 保险协助条款
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Compliance with or breach of an insured's cooperation obligations.
- Allowed outcomes: `complied, breached, unresolved`
- Feature pack: `li_pack.insurance_cooperation_clause`
- Exclude when: Ordinary litigation cooperation is excluded.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `cooperation_obligation` | Cooperation Obligation | `issue_specific` | `string` | `False` |
| `insured_conduct` | Insured Conduct | `issue_specific` | `string` | `False` |
| `insurer_prejudice` | Insurer Prejudice | `issue_specific` | `enum` | `False` |
| `cooperation_clause_result` | Cooperation Clause Result | `issue_specific` | `enum` | `False` |

## `insurance_misrepresentation_rescission` — Insurance Misrepresentation Rescission

- Chinese label: 保险虚假陈述与撤销
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Misrepresentation in insurance application or claim and policy rescission.
- Allowed outcomes: `rescission_allowed, rescission_denied, unresolved`
- Feature pack: `li_pack.insurance_misrepresentation_rescission`
- Exclude when: Unrelated fraud or rescission is excluded.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `misrepresentation_subject` | Misrepresentation Subject | `issue_specific` | `string` | `False` |
| `speaker_or_applicant` | Speaker or Applicant | `issue_specific` | `string` | `False` |
| `materiality_result` | Materiality Result | `issue_specific` | `enum` | `False` |
| `rescission_result` | Rescission Result | `issue_specific` | `enum` | `False` |

## `insurance_bad_faith` — Insurance Bad Faith

- Chinese label: 保险恶意理赔
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Insurer bad-faith denial, delay, settlement, or claim handling.
- Allowed outcomes: `established, not_established, unresolved`
- Feature pack: `li_pack.insurance_bad_faith`
- Exclude when: A party allegation of bad faith without court analysis is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `claim_handling_conduct` | Claim Handling Conduct | `issue_specific` | `enum[]` | `False` |
| `benefits_or_coverage_due` | Benefits or Coverage Due | `issue_specific` | `enum` | `False` |
| `bad_faith_standard` | Bad Faith Standard | `issue_specific` | `string` | `False` |
| `bad_faith_result` | Bad Faith Result | `issue_specific` | `enum` | `False` |

## `insurance_claim_handling_duties` — Insurance Claim Handling Duties

- Chinese label: 保险理赔处理义务
- Namespace: `insurance`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Legal duties governing investigation, adjustment, processing, or settlement of an insurance claim.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Routine claim history without a disputed legal duty is insufficient.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `insurance_limit_interpretation` — Insurance Limit Interpretation

- Chinese label: 保险限额解释
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Interpretation or application of aggregate, per-occurrence, or other policy limits.
- Allowed outcomes: `limit_applied, limit_not_applied, unresolved`
- Feature pack: `li_pack.insurance_limit_interpretation`
- Exclude when: A policy amount mentioned only as fact is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `limit_type` | Limit Type | `issue_specific` | `string[]` | `False` |
| `limit_amount` | Limit Amount | `issue_specific` | `money_object` | `False` |
| `number_of_occurrences_or_claims` | Number of Occurrences or Claims | `issue_specific` | `integer` | `False` |
| `limit_result` | Limit Result | `issue_specific` | `enum` | `False` |

## `insurance_allocation_between_insurers` — Insurance Allocation Between Insurers

- Chinese label: 保险人之间责任分配
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Priority, contribution, allocation, or exhaustion among insurers.
- Allowed outcomes: `allocation_ordered, allocation_denied, unresolved`
- Feature pack: `li_pack.insurance_allocation_between_insurers`
- Exclude when: Multiple insurers named without an allocation dispute are insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `insurers` | Insurers | `issue_specific` | `string[]` | `False` |
| `allocation_basis` | Allocation Basis | `issue_specific` | `enum` | `False` |
| `allocation_amounts` | Allocation Amounts | `issue_specific` | `money_object[]` | `False` |
| `allocation_result` | Allocation Result | `issue_specific` | `enum` | `False` |

## `insurance_additional_insured_status` — Insurance Additional Insured Status

- Chinese label: 附加被保险人身份
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a person or entity qualifies for additional-insured coverage.
- Allowed outcomes: `qualifies, does_not_qualify, unresolved`
- Feature pack: `li_pack.insurance_additional_insured_status`
- Exclude when: An additional insured listed but not disputed is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `claimed_insured` | Claimed Insured | `issue_specific` | `string` | `False` |
| `named_insured` | Named Insured | `issue_specific` | `string` | `False` |
| `additional_insured_basis` | Additional Insured Basis | `issue_specific` | `string` | `False` |
| `additional_insured_result` | Additional Insured Result | `issue_specific` | `enum` | `False` |

## `insurance_subrogation_right` — Insurance Subrogation Right

- Chinese label: 保险代位求偿权
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Existence, scope, priority, or enforcement of insurer subrogation rights.
- Allowed outcomes: `exists, does_not_exist, unresolved`
- Feature pack: `li_pack.insurance_subrogation_right`
- Exclude when: Payment by an insurer alone is insufficient.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `subrogor` | Subrogor | `issue_specific` | `string` | `False` |
| `subrogee` | Subrogee | `issue_specific` | `string` | `False` |
| `target_defendant_or_fund` | Target Defendant or Fund | `issue_specific` | `string` | `False` |
| `subrogation_amount` | Subrogation Amount | `issue_specific` | `money_object` | `False` |
| `subrogation_result` | Subrogation Result | `issue_specific` | `enum` | `False` |

## `insurance_waiver_estoppel` — Insurance Waiver Estoppel

- Chinese label: 保险弃权与禁反言
- Namespace: `insurance`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether waiver or estoppel affects insurance coverage or policy defenses.
- Allowed outcomes: `applies, does_not_apply, unresolved`
- Feature pack: `li_pack.insurance_waiver_estoppel`
- Exclude when: Waiver or estoppel outside an insurance relationship is excluded.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `waiver_or_estoppel_actor` | Waiver or Estoppel Actor | `issue_specific` | `enum` | `False` |
| `conduct_supporting_waiver_estoppel` | Conduct Supporting Waiver or Estoppel | `issue_specific` | `string` | `False` |
| `reliance_or_prejudice` | Reliance or Prejudice | `issue_specific` | `enum` | `False` |
| `waiver_estoppel_result` | Waiver or Estoppel Result | `issue_specific` | `enum` | `False` |

## `personal_jurisdiction` — Personal Jurisdiction

- Chinese label: 属人管辖权
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the court may exercise personal jurisdiction over a party.
- Allowed outcomes: `exists, absent, waived`
- Feature pack: `li_pack.personal_jurisdiction`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `jurisdiction_target_party` | Jurisdiction Target Party | `issue_specific` | `string` | `False` |
| `forum_state` | Forum State | `issue_specific` | `string` | `False` |
| `contact_type` | Contact Type | `issue_specific` | `string[]` | `False` |
| `jurisdiction_theory` | Jurisdiction Theory | `issue_specific` | `enum[]` | `False` |
| `personal_jurisdiction_result` | Personal Jurisdiction Result | `issue_specific` | `enum` | `False` |

## `subject_matter_jurisdiction` — Subject Matter Jurisdiction

- Chinese label: 事项管辖权
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the court has authority over the category of dispute.
- Allowed outcomes: `exists, absent`
- Feature pack: `li_pack.subject_matter_jurisdiction`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `jurisdiction_basis` | Jurisdiction Basis | `issue_specific` | `enum[]` | `False` |
| `jurisdiction_defect` | Jurisdiction Defect | `issue_specific` | `string` | `False` |
| `amount_in_controversy` | Amount in Controversy | `issue_specific` | `money_object` | `False` |
| `subject_matter_jurisdiction_result` | Subject Matter Jurisdiction Result | `issue_specific` | `enum` | `False` |

## `venue_transfer` — Venue Transfer

- Chinese label: 审判地点移送
- Namespace: `civil_procedure`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Whether venue is proper or the matter should be transferred or dismissed for forum reasons.
- Allowed outcomes: ``
- Feature pack: ``
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `removal_and_remand` — Removal And Remand

- Chinese label: 移送联邦法院与发回州法院
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether removal to federal court or remand to state court is proper.
- Allowed outcomes: `removal_proper, remand_required, remand_denied`
- Feature pack: `li_pack.removal_and_remand`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `removing_party` | Removing Party | `issue_specific` | `string` | `False` |
| `removal_basis` | Removal Basis | `issue_specific` | `enum[]` | `False` |
| `remand_basis` | Remand Basis | `issue_specific` | `string[]` | `False` |
| `removal_timing` | Removal Timing | `issue_specific` | `enum` | `False` |
| `removal_remand_result` | Removal or Remand Result | `issue_specific` | `enum` | `False` |

## `standing` — Standing

- Chinese label: 诉讼资格
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the claimant has constitutional or prudential standing.
- Allowed outcomes: `established, not_established`
- Feature pack: `li_pack.standing`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `standing_party` | Standing Party | `issue_specific` | `string` | `False` |
| `injury_in_fact` | Injury in Fact | `issue_specific` | `enum` | `False` |
| `causation` | Causation | `issue_specific` | `enum` | `False` |
| `redressability` | Redressability | `issue_specific` | `enum` | `False` |
| `standing_result` | Standing Result | `issue_specific` | `enum` | `False` |

## `mootness` — Mootness

- Chinese label: 争议已失实效
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether changed circumstances eliminate a live controversy.
- Allowed outcomes: `moot, not_moot, exception_applies`
- Feature pack: `li_pack.mootness`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `mootness_event` | Mootness Event | `issue_specific` | `string` | `False` |
| `mootness_exception` | Mootness Exception | `issue_specific` | `enum[]` | `False` |
| `mootness_result` | Mootness Result | `issue_specific` | `enum` | `False` |

## `claim_preclusion` — Claim Preclusion

- Chinese label: 请求排除/既判力
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a prior judgment bars the present claim.
- Allowed outcomes: `applies, does_not_apply`
- Feature pack: `li_pack.claim_preclusion`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `prior_case_or_judgment` | Prior Case or Judgment | `issue_specific` | `string` | `False` |
| `same_parties_or_privies` | Same Parties or Privies | `issue_specific` | `enum` | `False` |
| `same_claim_or_transaction` | Same Claim or Transaction | `issue_specific` | `enum` | `False` |
| `final_judgment_on_merits` | Final Judgment on Merits | `issue_specific` | `enum` | `False` |
| `claim_preclusion_result` | Claim Preclusion Result | `issue_specific` | `enum` | `False` |

## `issue_preclusion_collateral_estoppel` — Issue Preclusion Collateral Estoppel

- Chinese label: 争点排除/附带禁反言
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether collateral estoppel or issue preclusion bars relitigation of a legal or factual issue.
- Allowed outcomes: `applies, does_not_apply`
- Feature pack: `li_pack.issue_preclusion_collateral_estoppel`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `prior_case_or_judgment` | Prior Case or Judgment | `issue_specific` | `string` | `False` |
| `identical_issue` | Identical Issue | `issue_specific` | `enum` | `False` |
| `actually_litigated` | Actually Litigated | `issue_specific` | `enum` | `False` |
| `necessary_to_judgment` | Necessary to Judgment | `issue_specific` | `enum` | `False` |
| `issue_preclusion_result` | Issue Preclusion Result | `issue_specific` | `enum` | `False` |

## `class_certification` — Class Certification

- Chinese label: 集体诉讼认证
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the proposed class satisfies certification requirements.
- Allowed outcomes: `granted, denied, vacated`
- Feature pack: `li_pack.class_certification`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `class_definition` | Class Definition | `issue_specific` | `string` | `False` |
| `rule_23_basis` | Rule 23 Basis | `issue_specific` | `enum[]` | `False` |
| `certification_stage` | Certification Stage | `issue_specific` | `enum` | `False` |
| `class_certification_result` | Class Certification Result | `issue_specific` | `enum` | `False` |

## `pleading_sufficiency` — Pleading Sufficiency

- Chinese label: 诉状充分性
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the pleading states a legally sufficient claim or defense.
- Allowed outcomes: `sufficient, insufficient, partially_sufficient`
- Feature pack: `li_pack.pleading_sufficiency`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `challenged_claim` | Challenged Claim | `issue_specific` | `string` | `False` |
| `pleading_defect` | Pleading Defect | `issue_specific` | `enum[]` | `False` |
| `leave_to_amend` | Leave to Amend | `issue_specific` | `enum` | `False` |
| `pleading_result` | Pleading Result | `issue_specific` | `enum` | `False` |

## `service_of_process` — Service Of Process

- Chinese label: 送达程序
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether process was properly served.
- Allowed outcomes: `proper, improper, waived`
- Feature pack: `li_pack.service_of_process`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `service_method` | Service Method | `issue_specific` | `string` | `False` |
| `recipient_or_location` | Recipient or Location | `issue_specific` | `string` | `False` |
| `service_timing` | Service Timing | `issue_specific` | `enum` | `False` |
| `service_result` | Service Result | `issue_specific` | `enum` | `False` |

## `statute_of_limitations` — Statute Of Limitations

- Chinese label: 诉讼时效
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a claim or charge is time-barred.
- Allowed outcomes: `timely, time_barred, tolled`
- Feature pack: `li_pack.statute_of_limitations`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `limitations_period` | Limitations Period | `issue_specific` | `duration_object` | `False` |
| `trigger_date_or_event` | Trigger Date or Event | `issue_specific` | `string` | `False` |
| `filing_date` | Filing Date | `issue_specific` | `date` | `False` |
| `tolling_or_accrual_rule` | Tolling or Accrual Rule | `issue_specific` | `string[]` | `False` |
| `limitations_result` | Limitations Result | `issue_specific` | `enum` | `False` |

## `arbitration_enforceability` — Arbitration Enforceability

- Chinese label: 仲裁条款可执行性
- Namespace: `civil_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an arbitration agreement or award is enforceable.
- Allowed outcomes: `enforceable, unenforceable, waived`
- Feature pack: `li_pack.arbitration_enforceability`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `arbitration_clause_source` | Arbitration Clause Source | `issue_specific` | `string` | `False` |
| `delegation_clause` | Delegation Clause | `issue_specific` | `enum` | `False` |
| `scope_of_arbitration` | Scope of Arbitration | `issue_specific` | `enum` | `False` |
| `waiver_or_unconscionability` | Waiver or Unconscionability | `issue_specific` | `enum[]` | `False` |
| `arbitration_result` | Arbitration Result | `issue_specific` | `enum` | `False` |

## `attorney_client_privilege` — Attorney Client Privilege

- Chinese label: 律师-客户特权
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a communication is protected by attorney-client privilege.
- Allowed outcomes: `protected, not_protected, waived`
- Feature pack: `li_pack.attorney_client_privilege`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `communication_type` | Communication Type | `issue_specific` | `string` | `False` |
| `privilege_holder` | Privilege Holder | `issue_specific` | `string` | `False` |
| `waiver_basis` | Waiver Basis | `issue_specific` | `string` | `False` |
| `privilege_result` | Privilege Result | `issue_specific` | `enum` | `False` |

## `work_product_protection` — Work Product Protection

- Chinese label: 律师工作成果保护
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether material is protected as attorney work product.
- Allowed outcomes: `protected, not_protected, waived`
- Feature pack: `li_pack.work_product_protection`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `material_type` | Material Type | `issue_specific` | `string` | `False` |
| `prepared_in_anticipation` | Prepared in Anticipation of Litigation | `issue_specific` | `enum` | `False` |
| `substantial_need_exception` | Substantial Need Exception | `issue_specific` | `enum` | `False` |
| `work_product_result` | Work Product Result | `issue_specific` | `enum` | `False` |

## `discovery_scope` — Discovery Scope

- Chinese label: 证据开示范围
- Namespace: `evidence_privilege`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Whether requested discovery is permissible, proportional, or protected.
- Allowed outcomes: ``
- Feature pack: ``
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `hearsay` — Hearsay

- Chinese label: 传闻证据
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an out-of-court statement is admissible under hearsay rules.
- Allowed outcomes: `admitted, excluded, exception_applies`
- Feature pack: `li_pack.hearsay`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `statement_or_evidence` | Statement or Evidence | `issue_specific` | `string` | `False` |
| `declarant` | Declarant | `issue_specific` | `string` | `False` |
| `hearsay_exception` | Hearsay Exception | `issue_specific` | `string[]` | `False` |
| `hearsay_result` | Hearsay Result | `issue_specific` | `enum` | `False` |

## `expert_testimony` — Expert Testimony

- Chinese label: 专家证言
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether expert evidence satisfies admissibility requirements.
- Allowed outcomes: `admitted, excluded, limited`
- Feature pack: `li_pack.expert_testimony`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `expert_field` | Expert Field | `issue_specific` | `string` | `False` |
| `admissibility_standard` | Admissibility Standard | `issue_specific` | `enum` | `False` |
| `challenge_basis` | Challenge Basis | `issue_specific` | `string[]` | `False` |
| `expert_testimony_result` | Expert Testimony Result | `issue_specific` | `enum` | `False` |

## `evidence_authentication` — Evidence Authentication

- Chinese label: 证据认证
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether evidence has been sufficiently authenticated.
- Allowed outcomes: `authenticated, not_authenticated`
- Feature pack: `li_pack.evidence_authentication`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `evidence_item` | Evidence Item | `issue_specific` | `string` | `False` |
| `authentication_method` | Authentication Method | `issue_specific` | `string[]` | `False` |
| `authentication_result` | Authentication Result | `issue_specific` | `enum` | `False` |

## `character_evidence` — Character Evidence

- Chinese label: 品格证据
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether character or other-act evidence is admissible.
- Allowed outcomes: `admitted, excluded, limited`
- Feature pack: `li_pack.character_evidence`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `character_evidence_item` | Character Evidence Item | `issue_specific` | `string` | `False` |
| `purpose` | Purpose | `issue_specific` | `enum[]` | `False` |
| `rule_or_standard` | Rule or Standard | `issue_specific` | `string` | `False` |
| `character_evidence_result` | Character Evidence Result | `issue_specific` | `enum` | `False` |

## `relevance_prejudice_balancing` — Relevance Prejudice Balancing

- Chinese label: 相关性与不公平偏见权衡
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether relevance is substantially outweighed by unfair prejudice or related concerns.
- Allowed outcomes: `admitted, excluded, limited`
- Feature pack: `li_pack.relevance_prejudice_balancing`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `evidence_item` | Evidence Item | `issue_specific` | `string` | `False` |
| `probative_value_basis` | Probative Value Basis | `issue_specific` | `string` | `False` |
| `unfair_prejudice_basis` | Unfair Prejudice Basis | `issue_specific` | `string` | `False` |
| `relevance_prejudice_result` | Relevance Prejudice Result | `issue_specific` | `enum` | `False` |

## `confrontation_clause` — Confrontation Clause

- Chinese label: 对质权
- Namespace: `evidence_privilege`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether admission or exclusion of evidence violates confrontation rights.
- Allowed outcomes: `violation, no_violation`
- Feature pack: `li_pack.confrontation_clause`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `testimonial_statement` | Testimonial Statement | `issue_specific` | `string` | `False` |
| `declarant_availability` | Declarant Availability | `issue_specific` | `enum` | `False` |
| `prior_cross_examination` | Prior Cross Examination | `issue_specific` | `enum` | `False` |
| `confrontation_result` | Confrontation Result | `issue_specific` | `enum` | `False` |

## `harmless_error` — Harmless Error

- Chinese label: 无害错误
- Namespace: `appellate_review`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an identified error warrants reversal or was harmless.
- Allowed outcomes: `harmless, prejudicial, structural`
- Feature pack: `li_pack.harmless_error`

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `error_type` | Error Type | `issue_specific` | `string` | `False` |
| `error_preservation_status` | Error Preservation Status | `issue_specific` | `enum` | `False` |
| `harmless_error_standard` | Harmless Error Standard | `issue_specific` | `string` | `False` |
| `harmless_error_result` | Harmless Error Result | `issue_specific` | `enum` | `False` |

## `sufficiency_of_evidence` — Sufficiency of Evidence

- Chinese label: 证据充分性
- Namespace: `evidence_and_trial`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the evidence, viewed under the governing legal standard, is legally sufficient to support a verdict, conviction, finding, or judgment.
- Allowed outcomes: `sufficient, insufficient`
- Feature pack: `li_pack.sufficiency_of_evidence`
- Exclude when: A challenge only to the relative weight or credibility of evidence., Pleading sufficiency or substantial-evidence review of agency action.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `challenged_offense_or_claim` | Challenged Offense or Claim | `issue_specific` | `string` | `False` |
| `challenged_element` | Challenged Element | `issue_specific` | `string[]` | `False` |
| `evidence_relied_on` | Evidence Relied On | `issue_specific` | `string[]` | `False` |
| `sufficiency_standard` | Sufficiency Standard | `issue_specific` | `string` | `False` |
| `sufficiency_result` | Sufficiency Result | `issue_specific` | `enum` | `False` |

## `ineffective_assistance_of_counsel` — Ineffective Assistance of Counsel

- Chinese label: 律师帮助无效
- Namespace: `constitutional_criminal_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether counsel's deficient performance prejudiced a criminal defendant or post-conviction petitioner under the governing effectiveness standard.
- Allowed outcomes: `established, not_established, prejudice_not_shown`
- Feature pack: `li_pack.ineffective_assistance_of_counsel`
- Exclude when: A denial of counsel without analysis of counsel's performance., Ordinary disagreement with litigation strategy outside an effectiveness claim.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `alleged_deficiency` | Alleged Deficiency | `issue_specific` | `string[]` | `False` |
| `strickland_deficiency_result` | Strickland Deficiency Result | `issue_specific` | `enum` | `False` |
| `strickland_prejudice_result` | Strickland Prejudice Result | `issue_specific` | `enum` | `False` |
| `iac_result` | IAC Result | `issue_specific` | `enum` | `False` |

## `anders_review` — Anders Review

- Chinese label: Anders 审查
- Namespace: `appellate_procedure`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Whether appointed appellate counsel may withdraw because an appeal is frivolous and whether independent judicial review reveals any nonfrivolous issue.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Any ordinary finding that an appeal or argument is frivolous.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `double_jeopardy` — Double Jeopardy

- Chinese label: 双重危险
- Namespace: `constitutional_criminal_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a prosecution, conviction, or punishment violates the constitutional prohibition against successive prosecution or multiple punishment for the same offense.
- Allowed outcomes: `violation, no_violation, offenses_merge`
- Feature pack: `li_pack.double_jeopardy`
- Exclude when: Generic claim preclusion or duplicate civil claims., A lesser-included-offense issue without a double-jeopardy question.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `prior_proceeding_or_charge` | Prior Proceeding or Charge | `issue_specific` | `string` | `False` |
| `current_charge_or_punishment` | Current Charge or Punishment | `issue_specific` | `string` | `False` |
| `same_offense_test` | Same Offense Test | `issue_specific` | `string` | `False` |
| `jeopardy_attached` | Jeopardy Attached | `issue_specific` | `enum` | `False` |
| `double_jeopardy_result` | Double Jeopardy Result | `issue_specific` | `enum` | `False` |

## `certificate_of_appealability` — Certificate of Appealability

- Chinese label: 上诉许可证明
- Namespace: `appellate_procedure`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Whether a habeas or Section 2255 applicant has made the showing required for appellate review.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Ordinary appellate jurisdiction or permission for an interlocutory appeal.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `habeas_exhaustion` — Habeas Exhaustion

- Chinese label: 人身保护令救济穷尽
- Namespace: `habeas_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a habeas petitioner exhausted available state remedies before seeking federal habeas relief.
- Allowed outcomes: `exhausted, not_exhausted, excused`
- Feature pack: `li_pack.habeas_exhaustion`
- Exclude when: PLRA exhaustion by prisoners challenging conditions., Generic administrative exhaustion or procedural default alone.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `habeas_claims` | Habeas Claims | `issue_specific` | `string[]` | `False` |
| `state_remedies_status` | State Remedies Status | `issue_specific` | `enum` | `False` |
| `procedural_default` | Procedural Default | `issue_specific` | `enum` | `False` |
| `habeas_exhaustion_result` | Habeas Exhaustion Result | `issue_specific` | `enum` | `False` |

## `lesser_included_offense_instruction` — Lesser-Included-Offense Instruction

- Chinese label: 较轻包含罪指示
- Namespace: `evidence_and_trial`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether the jury should have been instructed on, or a conviction may rest on, a lesser included offense.
- Allowed outcomes: `required, not_required, error_harmless`
- Feature pack: `li_pack.lesser_included_offense_instruction`
- Exclude when: Generic jury-instruction error., Double-jeopardy analysis based on overlapping offenses.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `charged_offense` | Charged Offense | `issue_specific` | `string` | `False` |
| `lesser_included_offense` | Lesser Included Offense | `issue_specific` | `string` | `False` |
| `instruction_requested_by` | Instruction Requested By | `issue_specific` | `enum` | `False` |
| `instruction_entitlement_basis` | Instruction Entitlement Basis | `issue_specific` | `string` | `False` |
| `lesser_included_instruction_result` | Lesser Included Instruction Result | `issue_specific` | `enum` | `False` |

## `qualified_immunity` — Qualified Immunity

- Chinese label: 合格豁免
- Namespace: `civil_rights_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a government official is shielded from civil liability because the asserted right was not clearly established or no constitutional violation occurred.
- Allowed outcomes: `granted, denied, fact_dispute`
- Feature pack: `li_pack.qualified_immunity`
- Exclude when: Absolute judicial, prosecutorial, legislative, or sovereign immunity.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `government_official` | Government Official | `issue_specific` | `string` | `False` |
| `challenged_conduct` | Challenged Conduct | `issue_specific` | `string` | `False` |
| `constitutional_violation_prong` | Constitutional Violation Prong | `issue_specific` | `enum` | `False` |
| `clearly_established_prong` | Clearly Established Prong | `issue_specific` | `enum` | `False` |
| `qualified_immunity_result` | Qualified Immunity Result | `issue_specific` | `enum` | `False` |

## `supplemental_jurisdiction` — Supplemental Jurisdiction

- Chinese label: 补充管辖权
- Namespace: `jurisdiction_and_justiciability`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a federal court may or should exercise jurisdiction over additional claims under the supplemental-jurisdiction doctrine.
- Allowed outcomes: `exercised, declined, unavailable`
- Feature pack: `li_pack.supplemental_jurisdiction`
- Exclude when: Whether original federal-question or diversity jurisdiction exists.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `anchor_federal_claims` | Anchor Federal Claims | `issue_specific` | `string[]` | `False` |
| `supplemental_state_claims` | Supplemental State Claims | `issue_specific` | `string[]` | `False` |
| `section_1367_basis` | Section 1367 Basis | `issue_specific` | `enum[]` | `False` |
| `supplemental_jurisdiction_result` | Supplemental Jurisdiction Result | `issue_specific` | `enum` | `False` |

## `plra_exhaustion` — PLRA Exhaustion

- Chinese label: PLRA 救济穷尽
- Namespace: `civil_rights_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether an incarcerated plaintiff properly exhausted available administrative remedies as required by the Prison Litigation Reform Act.
- Allowed outcomes: `exhausted, not_exhausted, remedy_unavailable`
- Feature pack: `li_pack.plra_exhaustion`
- Exclude when: Habeas exhaustion of state remedies., Generic administrative exhaustion outside the PLRA.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `prison_grievance_system` | Prison Grievance System | `issue_specific` | `string` | `False` |
| `grievance_steps_completed` | Grievance Steps Completed | `issue_specific` | `string[]` | `False` |
| `administrative_remedy_availability` | Administrative Remedy Availability | `issue_specific` | `enum` | `False` |
| `plra_exhaustion_result` | PLRA Exhaustion Result | `issue_specific` | `enum` | `False` |

## `younger_abstention` — Younger Abstention

- Chinese label: Younger 回避原则
- Namespace: `jurisdiction_and_justiciability`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a federal court should abstain from interfering with qualifying ongoing state proceedings under Younger.
- Allowed outcomes: `applies, does_not_apply, exception_applies`
- Feature pack: `li_pack.younger_abstention`
- Exclude when: Review of a completed state judgment or a generic comity reference.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `pending_state_proceeding` | Pending State Proceeding | `issue_specific` | `string` | `False` |
| `important_state_interest` | Important State Interest | `issue_specific` | `enum` | `False` |
| `adequate_opportunity_in_state_forum` | Adequate Opportunity in State Forum | `issue_specific` | `enum` | `False` |
| `younger_exception` | Younger Exception | `issue_specific` | `enum[]` | `False` |
| `younger_abstention_result` | Younger Abstention Result | `issue_specific` | `enum` | `False` |

## `rooker_feldman` — Rooker-Feldman Doctrine

- Chinese label: Rooker-Feldman 原则
- Namespace: `jurisdiction_and_justiciability`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a federal district court lacks jurisdiction over a de facto appeal from a state-court judgment.
- Allowed outcomes: `bars_jurisdiction, does_not_bar`
- Feature pack: `li_pack.rooker_feldman`
- Exclude when: Ordinary preclusion, parallel proceedings, or review of executive action.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `state_court_judgment` | State Court Judgment | `issue_specific` | `string` | `False` |
| `source_of_injury` | Source of Injury | `issue_specific` | `enum` | `False` |
| `requested_federal_relief` | Requested Federal Relief | `issue_specific` | `string` | `False` |
| `rooker_feldman_result` | Rooker-Feldman Result | `issue_specific` | `enum` | `False` |

## `judicial_immunity` — Judicial Immunity

- Chinese label: 司法豁免
- Namespace: `civil_rights_procedure`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a judge or judicial officer has absolute immunity for conduct performed in a judicial capacity within jurisdiction.
- Allowed outcomes: `granted, denied`
- Feature pack: `li_pack.judicial_immunity`
- Exclude when: Qualified immunity or sovereign immunity of a government entity.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `judicial_actor` | Judicial Actor | `issue_specific` | `string` | `False` |
| `challenged_judicial_act` | Challenged Judicial Act | `issue_specific` | `string` | `False` |
| `judicial_capacity` | Judicial Capacity | `issue_specific` | `enum` | `False` |
| `clear_absence_of_jurisdiction` | Clear Absence of Jurisdiction | `issue_specific` | `enum` | `False` |
| `judicial_immunity_result` | Judicial Immunity Result | `issue_specific` | `enum` | `False` |

## `dismissal_for_failure_to_prosecute` — Dismissal for Failure to Prosecute

- Chinese label: 因未推进诉讼而驳回
- Namespace: `civil_procedure`
- Status: `deprecated_ambiguous`
- Searchable: `False`
- Definition: Whether dismissal is warranted or valid because a party failed to prosecute, comply with scheduling obligations, or obey litigation orders.
- Allowed outcomes: ``
- Feature pack: ``
- Exclude when: Voluntary dismissal or dismissal because a pleading fails to state a claim.
- Deprecation reason: No single directly observable decision question with a closed outcome vocabulary.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
|  | No production feature pack. |  |  |  |

## `weight_of_the_evidence` — Weight of the Evidence

- Chinese label: 证据权重审查
- Namespace: `evidence_and_trial`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a verdict or finding is contrary to the manifest or great weight of the evidence under the applicable review standard.
- Allowed outcomes: `against_weight, not_against_weight`
- Feature pack: `li_pack.weight_of_the_evidence`
- Exclude when: Whether any legally sufficient evidence supports the result.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `challenged_verdict_or_finding` | Challenged Verdict or Finding | `issue_specific` | `string` | `False` |
| `evidence_conflict` | Evidence Conflict | `issue_specific` | `string[]` | `False` |
| `weight_review_standard` | Weight Review Standard | `issue_specific` | `string` | `False` |
| `weight_of_evidence_result` | Weight of Evidence Result | `issue_specific` | `enum` | `False` |

## `sentencing_reasonableness` — Sentencing Reasonableness

- Chinese label: 量刑合理性
- Namespace: `sentencing`
- Status: `active_strict`
- Searchable: `True`
- Definition: Whether a criminal sentence is procedurally or substantively reasonable under the governing appellate sentencing standard.
- Allowed outcomes: `reasonable, procedurally_unreasonable, substantively_unreasonable`
- Feature pack: `li_pack.sentencing_reasonableness`
- Exclude when: A dispute limited to calculation of a Guidelines provision., Harmless-error analysis without a reasonableness question.

| Feature | Label | Group | Type | Required |
|---|---|---|---|---|
| `issue_status` | Issue Status | `core` | `enum` | `True` |
| `issue_specific_outcome` | Issue-Specific Outcome | `core` | `enum` | `True` |
| `issue_target` | Issue Target | `core` | `object` | `True` |
| `court_action` | Current Court Action | `core` | `enum` | `True` |
| `decision_basis` | Decision Basis | `core` | `string[]` | `False` |
| `sentence_components_challenged` | Sentence Components Challenged | `issue_specific` | `string[]` | `False` |
| `reasonableness_type` | Reasonableness Type | `issue_specific` | `enum[]` | `False` |
| `guidelines_or_statutory_range` | Guidelines or Statutory Range | `issue_specific` | `string` | `False` |
| `variance_or_departure` | Variance or Departure | `issue_specific` | `enum` | `False` |
| `sentencing_reasonableness_result` | Sentencing Reasonableness Result | `issue_specific` | `enum` | `False` |
