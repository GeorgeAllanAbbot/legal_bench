# Analytical Feature Catalog v3.0（中文）

本目录定义从美国判例 opinion 中抽取的结构化字段。每个字段都必须有文本证据；若 opinion 未提及，应标记为 not_mentioned 或 not_applicable，而不是猜测。

| Feature | 中文名 | 类型 | 层级 | 生产状态 | 包含于 Legal Issues | 中文说明 |
|---|---|---|---|---|---|---|
| `party_types` | 当事人实体类型 | `enum[]` | `A` | `tier_a` |  | 抽取“当事人实体类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：caption_rules_plus_llm。 |
| `substantive_roles` | 当事人实体角色 | `enum[]` | `B` | `validator_required` |  | 抽取“当事人实体角色”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `party_roles` | 诉讼角色 | `object[]` | `A` | `validator_required` |  | 抽取“诉讼角色”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：caption_rules。 |
| `claims_or_charges` | 请求权基础或刑事指控 | `enum[]` | `C` | `validator_required` |  | 抽取“请求权基础或刑事指控”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：statute_rules_plus_llm。 |
| `defenses` | 抗辩 | `enum[]` | `C` | `validator_required` |  | 抽取“抗辩”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `requested_relief` | 请求的救济 | `enum[]` | `C` | `validator_required` |  | 抽取“请求的救济”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `claim_outcomes` | 逐项请求结果 | `object[]` | `D` | `validator_required` |  | 抽取“逐项请求结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `decision_for_party` | 实质胜诉方 | `enum` | `C` | `validator_required` |  | 抽取“实质胜诉方”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `case_disposition` | 案件最终处理 | `enum` | `B` | `validator_required` |  | 抽取“案件最终处理”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `motion_dispositions` | 动议处理结果 | `object[]` | `B` | `validator_required` |  | 抽取“动议处理结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `substantive_relief` | 实体救济 | `enum[]` | `C` | `experimental` |  | 抽取“实体救济”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `monetary_amounts` | 涉案金额 | `object[]` | `A` | `validator_required` |  | 抽取“涉案金额”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：regex_plus_role_llm。 |
| `event_dates` | 关键事实日期 | `object[]` | `A` | `validator_required` |  | 抽取“关键事实日期”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：date_rules_plus_llm。 |
| `locations` | 行为地点与场所 | `object[]` | `A` | `validator_required` |  | 抽取“行为地点与场所”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `injury_or_harm` | 损害类型 | `object` | `C` | `experimental` |  | 抽取“损害类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `evidentiary_failure` | 是否因证据不足败诉 | `boolean` | `C` | `validator_required` |  | 抽取“是否因证据不足败诉”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `settlement_status` | 和解状态 | `enum` | `C` | `validator_required` |  | 抽取“和解状态”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `standard_of_review` | 审查标准 | `enum[]` | `B` | `validator_required` |  | 抽取“审查标准”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：phrase_rules_plus_llm。 |
| `offense_types` | 罪名类型 | `enum[]` | `C` | `validator_required` |  | 抽取“罪名类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `criminal_conduct_types` | 犯罪行为方式 | `enum[]` | `C` | `validator_required` |  | 抽取“犯罪行为方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `weapon_types` | 武器类型 | `enum[]` | `C` | `validator_required` |  | 抽取“武器类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `victim_attributes` | 被害人属性 | `enum[]` | `C` | `validator_required` |  | 抽取“被害人属性”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `injury_severity` | 伤害程度 | `enum` | `C` | `validator_required` |  | 抽取“伤害程度”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `offense_location_type` | 犯罪场所类型 | `enum` | `C` | `validator_required` |  | 抽取“犯罪场所类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `repeat_offender_status` | 累犯或惯犯状态 | `enum` | `C` | `validator_required` |  | 抽取“累犯或惯犯状态”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `plea_type` | 认罪方式 | `enum` | `C` | `validator_required` |  | 抽取“认罪方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `sentence_components` | 刑罚组成 | `object[]` | `C` | `validator_required` |  | 抽取“刑罚组成”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `guideline_adjustments` | 量刑指南调整项 | `object[]` | `C` | `validator_required` |  | 抽取“量刑指南调整项”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `suppression_result` | 证据排除结果 | `enum` | `C` | `validator_required` |  | 抽取“证据排除结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `government_actor_type` | 政府行为主体 | `enum[]` | `C` | `validator_required` |  | 抽取“政府行为主体”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `challenged_government_conduct` | 被诉政府行为 | `enum[]` | `C` | `validator_required` |  | 抽取“被诉政府行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `force_type` | 使用武力方式 | `enum[]` | `C` | `validator_required` |  | 抽取“使用武力方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `threat_status` | 即时威胁状态 | `enum` | `C` | `validator_required` |  | 抽取“即时威胁状态”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `immunity_type` | 豁免类型 | `enum[]` | `C` | `validator_required` |  | 抽取“豁免类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `immunity_result` | 豁免裁判结果 | `enum` | `C` | `validator_required` |  | 抽取“豁免裁判结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `clearly_established_right_result` | 权利是否明确确立 | `enum` | `C` | `validator_required` |  | 抽取“权利是否明确确立”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `prison_exhaustion_result` | 囚犯申诉穷尽结果 | `enum` | `C` | `validator_required` |  | 抽取“囚犯申诉穷尽结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `constitutional_violation_result` | 宪法侵权认定 | `enum` | `C` | `validator_required` |  | 抽取“宪法侵权认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `employment_relationship` | 雇佣关系 | `enum` | `C` | `validator_required` |  | 抽取“雇佣关系”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `protected_characteristics` | 受保护属性 | `enum[]` | `C` | `validator_required` |  | 抽取“受保护属性”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `adverse_employment_actions` | 不利就业行为 | `enum[]` | `C` | `validator_required` |  | 抽取“不利就业行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `protected_activity` | 受保护活动 | `enum[]` | `C` | `validator_required` |  | 抽取“受保护活动”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `pretext_result` | 借口认定 | `enum` | `C` | `validator_required` |  | 抽取“借口认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `employment_exhaustion_status` | 就业案件行政前置 | `enum` | `C` | `validator_required` |  | 抽取“就业案件行政前置”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `wage_components` | 工资组成 | `enum[]` | `C` | `validator_required` |  | 抽取“工资组成”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `accommodation_types` | 便利或调整类型 | `enum[]` | `C` | `validator_required` |  | 抽取“便利或调整类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `immigration_relief_types` | 移民救济类型 | `enum[]` | `C` | `validator_required` |  | 抽取“移民救济类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `protected_grounds` | 迫害保护理由 | `enum[]` | `C` | `validator_required` |  | 抽取“迫害保护理由”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `persecution_types` | 迫害方式 | `enum[]` | `C` | `validator_required` |  | 抽取“迫害方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `credibility_result` | 可信度认定 | `enum` | `C` | `validator_required` |  | 抽取“可信度认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `protected_ground_nexus_result` | 迫害关联认定 | `enum` | `C` | `validator_required` |  | 抽取“迫害关联认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `removability_grounds` | 可遣返理由 | `enum[]` | `C` | `validator_required` |  | 抽取“可遣返理由”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `immigration_detention_status` | 移民拘留状态 | `object` | `C` | `validator_required` |  | 抽取“移民拘留状态”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `country_of_origin` | 原籍国 | `country_code` | `C` | `validator_required` |  | 抽取“原籍国”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `contract_types` | 合同类型 | `enum[]` | `C` | `validator_required` |  | 抽取“合同类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `formation_method` | 签约方式 | `enum` | `C` | `validator_required` |  | 抽取“签约方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `contract_validity_result` | 合同效力认定 | `enum` | `C` | `validator_required` |  | 抽取“合同效力认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `breach_types` | 违约类型 | `enum[]` | `C` | `validator_required` |  | 抽取“违约类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `performance_status` | 履行状态 | `enum` | `C` | `validator_required` |  | 抽取“履行状态”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `contract_damages_types` | 合同损害赔偿类型 | `enum[]` | `C` | `validator_required` |  | 抽取“合同损害赔偿类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `collateral_types` | 担保物类型 | `enum[]` | `C` | `validator_required` |  | 抽取“担保物类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `arbitration_clause_status` | 仲裁条款状态 | `enum` | `C` | `validator_required` |  | 抽取“仲裁条款状态”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `policy_types` | 保单类型 | `enum[]` | `C` | `validator_required` |  | 抽取“保单类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `insured_status` | 被保险人身份 | `enum` | `C` | `validator_required` |  | 抽取“被保险人身份”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `coverage_claim_types` | 保险请求类型 | `enum[]` | `C` | `experimental` |  | 抽取“保险请求类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `policy_provisions` | 争议保单条款 | `enum[]` | `C` | `validator_required` |  | 抽取“争议保单条款”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `coverage_result` | 承保结果 | `enum` | `C` | `validator_required` |  | 抽取“承保结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `claim_handling_conduct` | 理赔行为 | `enum[]` | `C` | `validator_required` | insurance_bad_faith | 抽取“理赔行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `bad_faith_result` | 恶意理赔认定 | `enum` | `C` | `validator_required` | insurance_bad_faith | 抽取“恶意理赔认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `insured_notice` | 被保险人通知 | `enum` | `C` | `validator_required` |  | 抽取“被保险人通知”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `insurer_disclaimer` | 保险人拒赔通知 | `enum` | `C` | `validator_required` |  | 抽取“保险人拒赔通知”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `jurisdiction_basis` | 管辖权基础 | `enum[]` | `C` | `validator_required` | subject_matter_jurisdiction | 抽取“管辖权基础”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `jurisdiction_result` | 管辖权结果 | `enum` | `C` | `validator_required` |  | 抽取“管辖权结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `standing_elements_result` | 适格要件结果 | `object` | `C` | `validator_required` |  | 抽取“适格要件结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `mootness_basis` | 案件无实际争议理由 | `enum` | `C` | `validator_required` |  | 抽取“案件无实际争议理由”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `limitations_trigger` | 时效起算事件 | `string` | `C` | `validator_required` |  | 抽取“时效起算事件”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `limitations_tolling_basis` | 时效中止或延长理由 | `enum[]` | `C` | `validator_required` |  | 抽取“时效中止或延长理由”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `limitations_result` | 时效裁判结果 | `enum` | `C` | `validator_required` | statute_of_limitations | 抽取“时效裁判结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `service_method` | 送达方式 | `enum` | `C` | `validator_required` | service_of_process | 抽取“送达方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `service_result` | 送达效力结果 | `enum` | `C` | `validator_required` | service_of_process | 抽取“送达效力结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `pleading_defect_types` | 诉状缺陷类型 | `enum[]` | `C` | `validator_required` |  | 抽取“诉状缺陷类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `pleading_result` | 诉状审查结果 | `enum` | `C` | `validator_required` | pleading_sufficiency | 抽取“诉状审查结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `preclusion_elements_result` | 既判力要件结果 | `object` | `C` | `validator_required` |  | 抽取“既判力要件结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `class_certification_result` | 集体诉讼认证结果 | `enum` | `C` | `validator_required` | class_certification | 抽取“集体诉讼认证结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `discovery_request_types` | 证据开示请求类型 | `enum[]` | `C` | `validator_required` |  | 抽取“证据开示请求类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `privilege_result` | 特权认定结果 | `enum` | `C` | `validator_required` | attorney_client_privilege | 抽取“特权认定结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `hearsay_exception` | 传闻例外 | `enum[]` | `C` | `validator_required` | hearsay | 抽取“传闻例外”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `hearsay_result` | 传闻证据结果 | `enum` | `C` | `validator_required` | hearsay | 抽取“传闻证据结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `expert_admissibility_standard` | 专家证据准入标准 | `enum` | `C` | `validator_required` |  | 抽取“专家证据准入标准”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `expert_testimony_result` | 专家证据结果 | `enum` | `C` | `validator_required` | expert_testimony | 抽取“专家证据结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `authentication_method` | 证据认证方式 | `enum[]` | `C` | `validator_required` | evidence_authentication | 抽取“证据认证方式”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `character_evidence_purpose` | 品格证据用途 | `enum[]` | `C` | `validator_required` |  | 抽取“品格证据用途”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `confrontation_result` | 对质权裁判结果 | `enum` | `C` | `validator_required` | confrontation_clause | 抽取“对质权裁判结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `error_preservation_status` | 错误是否保留 | `enum` | `C` | `validator_required` | harmless_error | 抽取“错误是否保留”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `harmless_error_result` | 无害错误结果 | `enum` | `C` | `validator_required` | harmless_error | 抽取“无害错误结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `due_process_interest_type` | 正当程序保护利益 | `enum[]` | `C` | `experimental` |  | 抽取“正当程序保护利益”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `due_process_protection_result` | 正当程序保障结果 | `enum` | `C` | `experimental` |  | 抽取“正当程序保障结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `equal_protection_classification` | 平等保护分类 | `enum[]` | `C` | `validator_required` |  | 抽取“平等保护分类”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `equal_protection_scrutiny` | 平等保护审查强度 | `enum` | `C` | `validator_required` |  | 抽取“平等保护审查强度”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `speech_category` | 言论类型 | `enum[]` | `C` | `validator_required` |  | 抽取“言论类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `forum_type` | 公共论坛类型 | `enum` | `C` | `validator_required` |  | 抽取“公共论坛类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `speech_regulation_result` | 言论规制结果 | `enum` | `C` | `validator_required` |  | 抽取“言论规制结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `religious_burden_type` | 宗教活动负担类型 | `enum[]` | `C` | `validator_required` |  | 抽取“宗教活动负担类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `religious_law_neutrality` | 法律是否中立普遍适用 | `enum` | `C` | `validator_required` |  | 抽取“法律是否中立普遍适用”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `right_to_counsel_stage` | 律师权所处阶段 | `enum` | `C` | `validator_required` |  | 抽取“律师权所处阶段”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `counsel_waiver_result` | 律师权放弃结果 | `enum` | `C` | `validator_required` |  | 抽取“律师权放弃结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `venue_transfer_basis` | 移送审理依据 | `enum[]` | `C` | `validator_required` |  | 抽取“移送审理依据”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `venue_transfer_result` | 移送审理结果 | `enum` | `C` | `validator_required` |  | 抽取“移送审理结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `relevance_prejudice_result` | 相关性与不当偏见权衡结果 | `enum` | `C` | `validator_required` | relevance_prejudice_balancing | 抽取“相关性与不当偏见权衡结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `policy_interpretation_method` | 保单解释方法 | `enum[]` | `C` | `validator_required` |  | 抽取“保单解释方法”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `duty_to_defend_result` | 保险人抗辩义务结果 | `enum` | `C` | `validator_required` | insurance_duty_to_defend | 抽取“保险人抗辩义务结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `duty_to_indemnify_result` | 保险人赔偿义务结果 | `enum` | `C` | `validator_required` | insurance_duty_to_indemnify | 抽取“保险人赔偿义务结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `cooperation_clause_result` | 协助义务条款结果 | `enum` | `C` | `validator_required` | insurance_cooperation_clause | 抽取“协助义务条款结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `insurance_misrepresentation_result` | 保险虚假陈述结果 | `enum` | `C` | `validator_required` |  | 抽取“保险虚假陈述结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `policy_limit_result` | 保险限额解释结果 | `object` | `C` | `validator_required` |  | 抽取“保险限额解释结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `interinsurer_allocation_method` | 保险人之间分摊方法 | `enum` | `C` | `validator_required` |  | 抽取“保险人之间分摊方法”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `insurance_subrogation_result` | 保险代位权结果 | `enum` | `C` | `validator_required` |  | 抽取“保险代位权结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `insurance_waiver_estoppel_result` | 保险弃权或禁反言结果 | `enum` | `C` | `validator_required` |  | 抽取“保险弃权或禁反言结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `agency_action_types` | 行政行为类型 | `enum[]` | `C` | `validator_required` |  | 抽取“行政行为类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `administrative_exhaustion_result` | 行政救济穷尽结果 | `enum` | `C` | `validator_required` |  | 抽取“行政救济穷尽结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `benefit_program_types` | 福利项目类型 | `enum[]` | `C` | `validator_required` |  | 抽取“福利项目类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `bankruptcy_chapter` | 破产章节 | `enum` | `C` | `validator_required` |  | 抽取“破产章节”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `creditor_status` | 债权人地位 | `enum[]` | `C` | `validator_required` |  | 抽取“债权人地位”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `automatic_stay_result` | 自动中止结果 | `enum` | `C` | `validator_required` |  | 抽取“自动中止结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `tax_types` | 税种 | `enum[]` | `C` | `validator_required` |  | 抽取“税种”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `taxpayer_types` | 纳税人类型 | `enum[]` | `C` | `validator_required` |  | 抽取“纳税人类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `deduction_or_credit_types` | 扣除或抵免类型 | `enum[]` | `C` | `validator_required` |  | 抽取“扣除或抵免类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `tax_adjustment_result` | 税务调整结果 | `enum` | `C` | `validator_required` |  | 抽取“税务调整结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `ip_right_types` | 知识产权类型 | `enum[]` | `C` | `validator_required` |  | 抽取“知识产权类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `infringement_result` | 侵权认定结果 | `enum` | `C` | `validator_required` |  | 抽取“侵权认定结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `property_interest_types` | 不动产权利类型 | `enum[]` | `C` | `validator_required` |  | 抽取“不动产权利类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `foreclosure_result` | 止赎结果 | `enum` | `C` | `validator_required` |  | 抽取“止赎结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `tenancy_issue_types` | 租赁争议类型 | `enum[]` | `C` | `validator_required` |  | 抽取“租赁争议类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `custody_best_interests_result` | 儿童最佳利益认定 | `enum` | `C` | `validator_required` |  | 抽取“儿童最佳利益认定”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `support_obligation_types` | 抚养义务类型 | `enum[]` | `C` | `validator_required` |  | 抽取“抚养义务类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `product_defect_types` | 产品缺陷类型 | `enum[]` | `C` | `validator_required` |  | 抽取“产品缺陷类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `negligence_elements_result` | 过失责任要件结果 | `object` | `C` | `validator_required` |  | 抽取“过失责任要件结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `defamation_statement_types` | 诽谤陈述类型 | `enum[]` | `C` | `validator_required` |  | 抽取“诽谤陈述类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `consumer_transaction_types` | 消费交易类型 | `enum[]` | `C` | `validator_required` |  | 抽取“消费交易类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `consumer_compliance_result` | 消费者保护合规结果 | `enum` | `C` | `validator_required` |  | 抽取“消费者保护合规结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `credit_or_debt_conduct` | 信用或债务处理行为 | `enum[]` | `C` | `validator_required` |  | 抽取“信用或债务处理行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `environmental_regulated_medium` | 环境监管对象 | `enum[]` | `C` | `validator_required` |  | 抽取“环境监管对象”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `environmental_agency_action` | 环境行政行为 | `enum[]` | `C` | `validator_required` |  | 抽取“环境行政行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `environmental_compliance_result` | 环境合规结果 | `enum` | `C` | `validator_required` |  | 抽取“环境合规结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `health_program_or_service` | 医疗项目或服务 | `enum[]` | `C` | `validator_required` |  | 抽取“医疗项目或服务”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `healthcare_entity_types` | 医疗主体类型 | `enum[]` | `C` | `validator_required` |  | 抽取“医疗主体类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `health_regulatory_result` | 医疗监管结果 | `enum` | `C` | `validator_required` |  | 抽取“医疗监管结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `education_institution_type` | 教育机构类型 | `enum` | `C` | `validator_required` |  | 抽取“教育机构类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `education_action_types` | 教育争议行为 | `enum[]` | `C` | `validator_required` |  | 抽取“教育争议行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `education_remedy_result` | 教育案件救济结果 | `enum` | `C` | `validator_required` |  | 抽取“教育案件救济结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `security_instrument_types` | 证券工具类型 | `enum[]` | `C` | `validator_required` |  | 抽取“证券工具类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `securities_misconduct_types` | 证券违法行为类型 | `enum[]` | `C` | `validator_required` |  | 抽取“证券违法行为类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `securities_liability_result` | 证券责任结果 | `enum` | `C` | `validator_required` |  | 抽取“证券责任结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `estate_or_trust_instrument` | 遗产或信托文书 | `enum[]` | `C` | `validator_required` |  | 抽取“遗产或信托文书”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `fiduciary_role_types` | 受信义务主体 | `enum[]` | `C` | `validator_required` |  | 抽取“受信义务主体”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `probate_or_trust_result` | 遗嘱信托争议结果 | `enum` | `C` | `validator_required` |  | 抽取“遗嘱信托争议结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `antitrust_conduct_types` | 反垄断行为类型 | `enum[]` | `C` | `validator_required` |  | 抽取“反垄断行为类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `relevant_market` | 相关市场 | `object` | `C` | `validator_required` |  | 抽取“相关市场”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `antitrust_liability_result` | 反垄断责任结果 | `enum` | `C` | `validator_required` |  | 抽取“反垄断责任结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `maritime_claim_types` | 海商请求类型 | `enum[]` | `C` | `validator_required` |  | 抽取“海商请求类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `vessel_or_cargo_types` | 船舶或货物类型 | `enum[]` | `C` | `validator_required` |  | 抽取“船舶或货物类型”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `maritime_liability_result` | 海商责任结果 | `enum` | `C` | `validator_required` |  | 抽取“海商责任结果”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `corporate_actor_roles` | 公司参与者角色 | `enum[]` | `C` | `validator_required` |  | 抽取“公司参与者角色”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `corporate_governance_conduct` | 公司治理行为 | `enum[]` | `C` | `validator_required` |  | 抽取“公司治理行为”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
| `family_relationship_context` | 家庭关系背景 | `enum[]` | `C` | `validator_required` |  | 抽取“家庭关系背景”字段。必须由当前 opinion 文本支持；未提及时允许标记为 not_mentioned 或 not_applicable。抽取方式：llm_verified。 |
