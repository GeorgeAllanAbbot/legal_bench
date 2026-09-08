# Matter Type Feature Reference

This reference defines factual fields extracted under each Matter Type. Features describe facts, amounts, dates, parties, and outcomes; they do not replace Legal Issues.

## Feature Status

- `present`: explicitly supported by the current opinion and accompanied by evidence.
- `not_mentioned`: not supplied by the opinion; do not infer it.
- `not_applicable`: not applicable to this case.
- `uncertain`: relevant material exists but does not support a non-contradictory value.

Numeric values must be JSON numbers with explicit units. Quoted cases, abstract legal standards, and hypotheticals cannot alone support case-fact amounts.

`matter_status` and `matter_outcome` are top-level Matter Type annotation properties and are not duplicated in the Feature Registry below.

## Feature Registry

| Key | Label | Type | Unit | Matter Types | Non-not-mentioned |
|---|---|---|---|---:|---:|
| `accident_date` | Accident Date | `date` | `-` | 4 | 654 |
| `accommodation_requested` | Accommodation Requested | `string` | `-` | 5 | 58 |
| `accounting_period` | Accounting Period | `object` | `-` | 10 | 109 |
| `accuracy_related_penalty_usd` | Accuracy-Related Penalty | `number` | `USD` | 5 | 147 |
| `acreage` | Acreage | `number` | `acres` | 4 | 234 |
| `actual_damages_usd` | Actual Damages | `number` | `USD` | 6 | 19 |
| `adjusted_gross_income_usd` | Adjusted Gross Income | `number` | `USD` | 5 | 95 |
| `administrative_record_complete` | Administrative Record Complete | `boolean` | `-` | 4 | 298 |
| `adverse_action` | Adverse Action | `enum[]` | `-` | 4 | 770 |
| `affected_area_acres` | Affected Area | `number` | `acres` | 6 | 25 |
| `affected_sales_usd` | Affected Sales | `number` | `USD` | 5 | 0 |
| `agency_action_type` | Agency Action Type | `enum[]` | `-` | 4 | 1376 |
| `agency_name` | Agency Name | `string` | `-` | 4 | 1367 |
| `alimony_monthly_usd` | Monthly Alimony | `number` | `USD/month` | 5 | 704 |
| `amount_awarded_usd` | Amount Awarded | `number` | `USD` | 120 | 2707 |
| `amount_claimed_usd` | Amount Claimed | `number` | `USD` | 120 | 2599 |
| `annual_salary_usd` | Annual Salary | `number` | `USD/year` | 4 | 56 |
| `application_year` | Application Year | `integer` | `-` | 4 | 86 |
| `apr_percent` | APR | `number` | `percent` | 6 | 105 |
| `arrears_period` | Arrears Period | `object` | `-` | 5 | 570 |
| `attorney_fees_awarded` | Attorney Fees Awarded | `boolean` | `-` | 5 | 229 |
| `attorney_fees_requested` | Attorney Fees Requested | `boolean` | `-` | 5 | 202 |
| `attorney_fees_usd` | Attorney Fees | `number` | `USD` | 120 | 2709 |
| `avoidance_amount_usd` | Avoidance Amount | `number` | `USD` | 5 | 126 |
| `award_modified_on_appeal` | Award Modified on Appeal | `boolean` | `-` | 120 | 12660 |
| `awarded_relief` | Awarded Relief | `enum[]` | `-` | 120 | 13244 |
| `back_pay_usd` | Back Pay | `number` | `USD` | 4 | 62 |
| `bankruptcy_chapter` | Bankruptcy Chapter | `enum` | `-` | 5 | 250 |
| `beneficiary_count` | Beneficiary Count | `number` | `-` | 10 | 96 |
| `benefit_amount_usd` | Benefit Amount | `number` | `USD` | 4 | 538 |
| `benefit_period_end` | Benefit Period End | `date` | `-` | 4 | 820 |
| `benefit_period_start` | Benefit Period Start | `date` | `-` | 4 | 829 |
| `benefit_start_date` | Benefit Start Date | `date` | `-` | 1 | 57 |
| `best_interest_factors_discussed` | Best Interest Factors Discussed | `boolean` | `-` | 1 | 287 |
| `bond_amount_usd` | Bond Amount | `number` | `USD` | 4 | 211 |
| `breach_date` | Breach Date | `date` | `-` | 4 | 222 |
| `breach_type` | Breach Type | `enum[]` | `-` | 4 | 525 |
| `cargo_value_usd` | Cargo Value | `number` | `USD` | 7 | 12 |
| `child_count` | Child Count | `number` | `-` | 5 | 880 |
| `child_support_deviation_monthly_usd` | Monthly Child Support Deviation | `number` | `USD/month` | 5 | 471 |
| `child_support_guideline_amount_usd` | Guideline Child Support | `number` | `USD/month` | 5 | 484 |
| `child_support_monthly_usd` | Monthly Child Support | `number` | `USD/month` | 5 | 489 |
| `child_support_weekly_usd` | Weekly Child Support | `number` | `USD/week` | 1 | 146 |
| `civil_penalty_usd` | Civil Penalty | `number` | `USD` | 17 | 1049 |
| `claim_amount_usd` | Claim Amount | `number` | `USD` | 25 | 324 |
| `claim_count` | Claim or Count Number | `number` | `-` | 120 | 5746 |
| `class_action_alleged` | Class Action Alleged | `boolean` | `-` | 6 | 164 |
| `class_period` | Class Period | `object` | `-` | 4 | 80 |
| `cleanup_cost_usd` | Cleanup Cost | `number` | `USD` | 6 | 28 |
| `collateral_value_usd` | Collateral Value | `number` | `USD` | 11 | 270 |
| `collection_fee_usd` | Collection Fee | `number` | `USD` | 6 | 79 |
| `comparative_fault_percent` | Comparative Fault | `number` | `percent` | 4 | 300 |
| `compensatory_damages_usd` | Compensatory Damages | `number` | `USD` | 7 | 81 |
| `constitutional_rights_invoked` | Rights Invoked | `enum[]` | `-` | 7 | 1461 |
| `consumer_product_or_service` | Consumer Product or Service | `string` | `-` | 6 | 171 |
| `consumer_statute` | Consumer Statute | `string[]` | `-` | 6 | 172 |
| `contract_amount_usd` | Contract Amount | `number` | `USD` | 4 | 176 |
| `contract_date` | Contract Date | `date` | `-` | 4 | 312 |
| `contract_type` | Contract Type | `enum[]` | `-` | 4 | 632 |
| `conviction_status` | Conviction Status | `enum` | `-` | 4 | 3432 |
| `costs_usd` | Costs | `number` | `USD` | 120 | 2606 |
| `country_of_origin` | Country of Origin | `string` | `-` | 4 | 338 |
| `counts_of_conviction` | Counts of Conviction | `number` | `-` | 4 | 2186 |
| `coverage_amount_awarded_usd` | Coverage Amount Awarded | `number` | `USD` | 10 | 76 |
| `coverage_amount_claimed_usd` | Coverage Amount Claimed | `number` | `USD` | 10 | 128 |
| `coverage_period_end` | Coverage Period End | `date` | `-` | 10 | 203 |
| `coverage_period_start` | Coverage Period Start | `date` | `-` | 10 | 207 |
| `credit_amount_usd` | Tax Credit Amount | `number` | `USD` | 5 | 112 |
| `credit_limit_usd` | Credit Limit | `number` | `USD` | 6 | 128 |
| `credit_score_or_report_issue` | Credit Score or Report Issue | `string` | `-` | 6 | 123 |
| `criminal_history_category` | Criminal History Category | `enum` | `-` | 4 | 1803 |
| `current_court_disposition` | Current Court Disposition | `enum[]` | `-` | 120 | 13804 |
| `custody_awarded_to` | Custody Awarded To | `enum` | `-` | 5 | 801 |
| `custody_modified` | Custody Modified | `boolean` | `-` | 5 | 775 |
| `damages_awarded_usd` | Damages Awarded | `number` | `USD` | 4 | 170 |
| `damages_claimed_usd` | Damages Claimed | `number` | `USD` | 4 | 148 |
| `death_claim` | Death Claim | `boolean` | `-` | 4 | 1018 |
| `debt_amount_usd` | Debt Amount | `number` | `USD` | 11 | 242 |
| `debtor_type` | Debtor Type | `enum` | `-` | 5 | 280 |
| `deductible_amount_usd` | Deductible | `number` | `USD` | 10 | 96 |
| `deduction_amount_usd` | Deduction Amount | `number` | `USD` | 5 | 145 |
| `default_amount_usd` | Default Amount | `number` | `USD` | 1 | 30 |
| `defendant_fault_percent` | Defendant Fault Percent | `number` | `percent` | 4 | 208 |
| `defense_costs_usd` | Defense Costs | `number` | `USD` | 10 | 42 |
| `deficiency_amount_usd` | Deficiency Amount | `number` | `USD` | 5 | 148 |
| `detention_days` | Detention Length | `number` | `days` | 4 | 202 |
| `disability_onset_date` | Disability Onset Date | `date` | `-` | 1 | 318 |
| `discharge_denied` | Discharge Denied | `boolean` | `-` | 5 | 224 |
| `discipline_days` | Discipline Days | `number` | `days` | 5 | 59 |
| `domestic_violence_alleged` | Domestic Violence Alleged | `boolean` | `-` | 5 | 458 |
| `drug_quantity` | Drug Quantity | `object` | `-` | 4 | 2907 |
| `education_program` | Education Program | `string` | `-` | 5 | 69 |
| `employee_count` | Employee Count | `number` | `-` | 4 | 137 |
| `employee_role` | Employee Role | `string` | `-` | 4 | 652 |
| `employment_end_date` | Employment End Date | `date` | `-` | 4 | 387 |
| `employment_start_date` | Employment Start Date | `date` | `-` | 4 | 355 |
| `estate_value_usd` | Estate Value | `number` | `USD` | 10 | 26 |
| `eviction_possession_awarded` | Possession Awarded | `boolean` | `-` | 4 | 550 |
| `fiduciary_role` | Fiduciary Role | `enum[]` | `-` | 10 | 165 |
| `finance_charge_usd` | Finance Charge | `number` | `USD` | 6 | 100 |
| `fine_amount_usd` | Criminal Fine | `number` | `USD` | 4 | 921 |
| `force_or_misconduct_type` | Force or Misconduct Type | `enum[]` | `-` | 7 | 1465 |
| `foreclosure_judgment_usd` | Foreclosure Judgment | `number` | `USD` | 4 | 305 |
| `fraud_penalty_usd` | Fraud Penalty | `number` | `USD` | 5 | 117 |
| `front_pay_usd` | Front Pay | `number` | `USD` | 4 | 91 |
| `future_medical_expenses_usd` | Future Medical Expenses | `number` | `USD` | 4 | 115 |
| `goods_or_services` | Goods or Services | `string` | `-` | 6 | 346 |
| `government_actor_type` | Government Actor Type | `enum[]` | `-` | 7 | 1555 |
| `gross_income_amount_usd` | Gross Income | `number` | `USD` | 5 | 118 |
| `guarantor_party` | Guarantor Party | `string` | `-` | 6 | 325 |
| `guideline_offense_level` | Guideline Offense Level | `number` | `-` | 4 | 2014 |
| `health_program` | Health Program | `enum[]` | `-` | 7 | 246 |
| `hearing_date` | Administrative Hearing Date | `date` | `-` | 4 | 685 |
| `hourly_wage_usd` | Hourly Wage | `number` | `USD/hour` | 4 | 52 |
| `immigration_relief_type` | Immigration Relief Type | `enum[]` | `-` | 4 | 390 |
| `income_parent_1_monthly_usd` | Parent 1 Monthly Income | `number` | `USD/month` | 5 | 282 |
| `income_parent_1_usd` | Parent 1 Income | `number` | `USD/year` | 5 | 308 |
| `income_parent_2_monthly_usd` | Parent 2 Monthly Income | `number` | `USD/month` | 5 | 273 |
| `income_parent_2_usd` | Parent 2 Income | `number` | `USD/year` | 5 | 271 |
| `infringing_product_or_work` | Infringing Product or Work | `string` | `-` | 4 | 242 |
| `injunction_ordered` | Injunction Ordered | `boolean` | `-` | 4 | 205 |
| `injury_severity` | Injury Severity | `enum` | `-` | 11 | 1056 |
| `injury_type` | Injury Type | `enum[]` | `-` | 4 | 1031 |
| `insured_notice_delay_days` | Insured Notice Delay | `number` | `days` | 10 | 104 |
| `insured_party` | Insured Party | `string` | `-` | 10 | 636 |
| `insurer_disclaimer_delay_days` | Insurer Disclaimer Delay | `number` | `days` | 10 | 106 |
| `insurer_party` | Insurer Party | `string` | `-` | 10 | 642 |
| `interest_amount_usd` | Interest Amount | `number` | `USD` | 120 | 4270 |
| `interest_rate_percent` | Interest Rate | `number` | `percent` | 4 | 83 |
| `invoice_amount_usd` | Invoice Amount | `number` | `USD` | 6 | 173 |
| `ip_asset_type` | IP Asset Type | `enum[]` | `-` | 4 | 283 |
| `lease_term_months` | Lease Term | `number` | `months` | 4 | 479 |
| `license_or_permit_type` | License or Permit Type | `string` | `-` | 4 | 1381 |
| `license_status` | License Status | `enum` | `-` | 4 | 1377 |
| `lien_amount_usd` | Lien Amount | `number` | `USD` | 4 | 302 |
| `liquidated_damages_usd` | Liquidated Damages | `number` | `USD` | 8 | 181 |
| `loan_balance_usd` | Loan Balance | `number` | `USD` | 4 | 293 |
| `loss_amount_usd` | Loss Amount | `number` | `USD` | 4 | 23 |
| `lost_profits_usd` | Lost Profits | `number` | `USD` | 4 | 20 |
| `lost_wages_usd` | Lost Wages | `number` | `USD` | 4 | 103 |
| `lower_court_disposition` | Lower Court Disposition | `enum[]` | `-` | 120 | 12455 |
| `maintenance_rate_usd_per_day` | Maintenance Rate | `number` | `USD/day` | 7 | 28 |
| `mandatory_minimum_months` | Mandatory Minimum | `number` | `months` | 4 | 578 |
| `marital_debt_amount_usd` | Marital Debt | `number` | `USD` | 5 | 664 |
| `marital_property_value_usd` | Marital Property Value | `number` | `USD` | 5 | 682 |
| `market_definition` | Market Definition | `string` | `-` | 5 | 42 |
| `market_share_percent` | Market Share | `number` | `percent` | 5 | 9 |
| `medical_expenses_usd` | Medical Expenses | `number` | `USD` | 4 | 137 |
| `minimum_wage_usd_per_hour` | Minimum Wage | `number` | `USD/hour` | 1 | 33 |
| `misstatement_type` | Misstatement Type | `enum[]` | `-` | 4 | 79 |
| `mitigation_amount_usd` | Mitigation Amount | `number` | `USD` | 4 | 81 |
| `mortgage_principal_usd` | Mortgage Principal | `number` | `USD` | 1 | 83 |
| `motion_or_order_at_issue` | Motion or Order at Issue | `string` | `-` | 120 | 13256 |
| `nominal_damages_usd` | Nominal Damages | `number` | `USD` | 7 | 60 |
| `non_usd_amounts` | Non-USD Amounts | `object[]` | `-` | 120 | 2205 |
| `notice_delay_days` | Notice Delay | `number` | `days` | 10 | 136 |
| `offense_category` | Offense Category | `enum[]` | `-` | 4 | 3349 |
| `offense_statutes` | Offense Statutes | `string[]` | `-` | 4 | 2355 |
| `overcharge_amount_usd` | Overcharge Amount | `number` | `USD` | 5 | 3 |
| `overpayment_amount_usd` | Overpayment Amount | `number` | `USD` | 11 | 995 |
| `overtime_hours` | Overtime Hours | `number` | `hours` | 4 | 96 |
| `ownership_percent` | Ownership Percent | `number` | `percent` | 6 | 297 |
| `pain_suffering_usd` | Pain and Suffering | `number` | `USD` | 4 | 102 |
| `parenting_time_percent` | Parenting Time Percent | `number` | `percent` | 1 | 37 |
| `patient_count` | Patient Count | `number` | `-` | 7 | 102 |
| `payment_frequency` | Payment Frequency | `enum` | `-` | 1 | 206 |
| `penalty_amount_usd` | Penalty Amount | `number` | `USD` | 5 | 141 |
| `performance_ordered` | Performance Ordered | `boolean` | `-` | 4 | 584 |
| `permit_limit_value` | Permit Limit Value | `object` | `-` | 6 | 50 |
| `petition_date` | Petition Date | `date` | `-` | 5 | 193 |
| `physical_injury_present` | Physical Injury Present | `boolean` | `-` | 7 | 1065 |
| `plan_payment_usd` | Plan Payment | `number` | `USD` | 5 | 156 |
| `plea_type` | Plea Type | `enum` | `-` | 4 | 2651 |
| `policy_limit_usd` | Policy Limit | `number` | `USD` | 10 | 177 |
| `policy_type` | Policy Type | `enum[]` | `-` | 10 | 658 |
| `pollutant_or_substance` | Pollutant or Substance | `string` | `-` | 6 | 63 |
| `premium_amount_usd` | Premium Amount | `number` | `USD` | 10 | 62 |
| `primary_parties` | Primary Parties | `object[]` | `-` | 120 | 13927 |
| `principal_amount_usd` | Principal Amount | `number` | `USD` | 6 | 163 |
| `probation_months` | Probation Length | `number` | `months` | 4 | 1506 |
| `property_address_or_description` | Property Address or Description | `string` | `-` | 4 | 574 |
| `property_damage_usd` | Property Damage | `number` | `USD` | 4 | 216 |
| `property_division_amount_usd` | Property Division Amount | `number` | `USD` | 5 | 690 |
| `property_type` | Property Type | `enum[]` | `-` | 4 | 606 |
| `property_value_usd` | Property Value | `number` | `USD` | 4 | 46 |
| `protected_class` | Protected Class | `enum[]` | `-` | 4 | 748 |
| `protected_ground` | Protected Ground | `enum[]` | `-` | 4 | 329 |
| `provider_type` | Provider Type | `enum[]` | `-` | 7 | 246 |
| `punitive_damages_usd` | Punitive Damages | `number` | `USD` | 11 | 179 |
| `redemption_amount_usd` | Redemption Amount | `number` | `USD` | 4 | 331 |
| `refund_amount_usd` | Refund Amount | `number` | `USD` | 5 | 116 |
| `registration_or_patent_number` | Registration or Patent Number | `string` | `-` | 4 | 165 |
| `regulated_medium` | Regulated Medium | `enum[]` | `-` | 6 | 76 |
| `reimbursement_amount_usd` | Reimbursement Amount | `number` | `USD` | 7 | 62 |
| `relevant_dates` | Relevant Dates | `object[]` | `-` | 120 | 13354 |
| `remand_to_agency` | Remand to Agency | `boolean` | `-` | 4 | 1277 |
| `removal_country` | Removal Country | `string` | `-` | 4 | 170 |
| `rent_arrears_usd` | Rent Arrears | `number` | `USD` | 4 | 401 |
| `rent_monthly_usd` | Monthly Rent | `number` | `USD/month` | 4 | 402 |
| `requested_relief` | Requested Relief | `enum[]` | `-` | 120 | 11795 |
| `rescission_ordered` | Rescission Ordered | `boolean` | `-` | 4 | 586 |
| `reservation_of_rights_issued` | Reservation of Rights Issued | `boolean` | `-` | 10 | 120 |
| `restitution_amount_usd` | Restitution | `number` | `USD` | 4 | 955 |
| `retaliation_protected_activity` | Retaliation Protected Activity | `string` | `-` | 4 | 644 |
| `royalty_rate_percent` | Royalty Rate | `number` | `percent` | 4 | 37 |
| `sale_price_usd` | Sale Price | `number` | `USD` | 4 | 237 |
| `sale_surplus_or_deficiency_usd` | Sale Surplus or Deficiency | `number` | `USD` | 1 | 31 |
| `salvage_award_usd` | Salvage Award | `number` | `USD` | 7 | 25 |
| `secured_debt_amount_usd` | Secured Debt | `number` | `USD` | 5 | 59 |
| `secured_party` | Secured Party | `string` | `-` | 6 | 351 |
| `security_type` | Security Type | `enum[]` | `-` | 4 | 85 |
| `sentence_consecutive_or_concurrent` | Consecutive or Concurrent Sentence | `enum` | `-` | 4 | 982 |
| `sentence_months` | Sentence Length | `number` | `months` | 4 | 2388 |
| `services_hours` | Services Hours | `number` | `hours` | 5 | 56 |
| `settlement_amount_usd` | Settlement Amount | `number` | `USD` | 120 | 5398 |
| `share_count` | Share Count | `number` | `-` | 10 | 318 |
| `specific_performance_ordered` | Specific Performance Ordered | `boolean` | `-` | 4 | 592 |
| `statutory_damages_usd` | Statutory Damages | `number` | `USD` | 10 | 73 |
| `statutory_penalty_usd` | Statutory Penalty | `number` | `USD` | 4 | 99 |
| `stay_violation_damages_usd` | Stay Violation Damages | `number` | `USD` | 5 | 148 |
| `stock_price_drop_percent` | Stock Price Drop | `number` | `percent` | 1 | 21 |
| `student_level` | Student Level | `enum[]` | `-` | 5 | 92 |
| `supervised_release_months` | Supervised Release | `number` | `months` | 4 | 1617 |
| `support_arrears_usd` | Support Arrears | `number` | `USD` | 5 | 401 |
| `support_modified` | Support Modified | `boolean` | `-` | 5 | 835 |
| `suspended_sentence_months` | Suspended Sentence | `number` | `months` | 4 | 1002 |
| `tax_form_or_schedule` | Tax Form or Schedule | `string[]` | `-` | 5 | 193 |
| `tax_liability_amount_usd` | Tax Liability Amount | `number` | `USD` | 5 | 104 |
| `tax_years` | Tax Years | `integer[]` | `-` | 5 | 263 |
| `taxpayer_type` | Taxpayer Type | `enum` | `-` | 5 | 348 |
| `time_served_credit_days` | Time Served Credit | `number` | `days` | 4 | 379 |
| `transaction_amount_usd` | Transaction Amount | `number` | `USD` | 10 | 204 |
| `transaction_type` | Transaction Type | `enum[]` | `-` | 6 | 398 |
| `treble_damages_usd` | Treble Damages | `number` | `USD` | 5 | 2 |
| `trust_value_usd` | Trust Value | `number` | `USD` | 10 | 103 |
| `tuition_or_fees_usd` | Tuition or Fees | `number` | `USD` | 5 | 42 |
| `underlying_action_type` | Underlying Action Type | `string` | `-` | 10 | 660 |
| `unpaid_amount_usd` | Unpaid Amount | `number` | `USD` | 4 | 166 |
| `unpaid_balance_usd` | Unpaid Balance | `number` | `USD` | 6 | 128 |
| `unpaid_overtime_usd` | Unpaid Overtime | `number` | `USD` | 1 | 36 |
| `unsecured_debt_amount_usd` | Unsecured Debt | `number` | `USD` | 5 | 45 |
| `vessel_type` | Vessel Type | `enum[]` | `-` | 7 | 40 |
| `vessel_value_usd` | Vessel Value | `number` | `USD` | 7 | 8 |
| `visitation_ordered` | Visitation Ordered | `boolean` | `-` | 5 | 680 |
| `weapon_type` | Weapon Type | `enum[]` | `-` | 4 | 3153 |
| `years_in_us` | Years in United States | `number` | `years` | 4 | 53 |

## Matter Type → Features

### `air_pollution_regulation` — Air Pollution Regulation

Practice area: `environmental_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `regulated_medium`, `pollutant_or_substance`, `cleanup_cost_usd`, `civil_penalty_usd`, `permit_limit_value`, `affected_area_acres`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `apa_review` — Apa Review

Practice area: `administrative_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `agency_name`, `agency_action_type`, `benefit_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `license_status`, `remand_to_agency`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `administrative_record_complete`, `hearing_date`, `benefit_period_start`, `benefit_period_end`, `license_or_permit_type`

### `arbitration_clause_dispute` — Arbitration Clause Dispute

Practice area: `contract_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `contract_type`, `contract_amount_usd`, `unpaid_amount_usd`, `damages_claimed_usd`, `damages_awarded_usd`, `liquidated_damages_usd`, `interest_rate_percent`, `performance_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `breach_type`, `contract_date`, `breach_date`, `mitigation_amount_usd`, `specific_performance_ordered`, `rescission_ordered`

### `asylum_protection` — Asylum Protection

Practice area: `immigration_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `immigration_relief_type`, `country_of_origin`, `removal_country`, `detention_days`, `bond_amount_usd`, `years_in_us`, `application_year`, `protected_ground`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `attorney_fee_civil_rights` — Attorney Fee Civil Rights

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `auto_insurance_coverage` — Auto Insurance Coverage

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `automatic_stay_issue` — Automatic Stay Issue

Practice area: `bankruptcy_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `bankruptcy_chapter`, `debtor_type`, `debt_amount_usd`, `claim_amount_usd`, `collateral_value_usd`, `plan_payment_usd`, `avoidance_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `petition_date`, `secured_debt_amount_usd`, `unsecured_debt_amount_usd`, `discharge_denied`, `stay_violation_damages_usd`

### `avoidance_action` — Avoidance Action

Practice area: `bankruptcy_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `bankruptcy_chapter`, `debtor_type`, `debt_amount_usd`, `claim_amount_usd`, `collateral_value_usd`, `plan_payment_usd`, `avoidance_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `petition_date`, `secured_debt_amount_usd`, `unsecured_debt_amount_usd`, `discharge_denied`, `stay_violation_damages_usd`

### `beneficiary_dispute` — Beneficiary Dispute

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `benefits_review` — Benefits Review

Practice area: `administrative_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `agency_name`, `agency_action_type`, `benefit_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `license_status`, `remand_to_agency`, `disability_onset_date`, `benefit_start_date`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `administrative_record_complete`, `hearing_date`, `benefit_period_start`, `benefit_period_end`, `license_or_permit_type`

### `breach_of_contract` — Breach Of Contract

Practice area: `contract_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `contract_type`, `contract_amount_usd`, `unpaid_amount_usd`, `damages_claimed_usd`, `damages_awarded_usd`, `liquidated_damages_usd`, `interest_rate_percent`, `performance_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `breach_type`, `contract_date`, `breach_date`, `mitigation_amount_usd`, `specific_performance_ordered`, `rescission_ordered`

### `broker_dealer_regulation` — Broker Dealer Regulation

Practice area: `securities_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `security_type`, `transaction_amount_usd`, `loss_amount_usd`, `share_count`, `class_period`, `misstatement_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `business_entity_dissolution` — Business Entity Dissolution

Practice area: `commercial_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `transaction_type`, `transaction_amount_usd`, `unpaid_balance_usd`, `collateral_value_usd`, `share_count`, `ownership_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `goods_or_services`, `invoice_amount_usd`, `principal_amount_usd`, `guarantor_party`, `secured_party`

### `cargo_loss` — Cargo Loss

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `chapter_identification` — Chapter Identification

Practice area: `bankruptcy_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `bankruptcy_chapter`, `debtor_type`, `debt_amount_usd`, `claim_amount_usd`, `collateral_value_usd`, `plan_payment_usd`, `avoidance_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `petition_date`, `secured_debt_amount_usd`, `unsecured_debt_amount_usd`, `discharge_denied`, `stay_violation_damages_usd`

### `conditions_of_confinement` — Conditions Of Confinement

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `consumer_credit_reporting` — Consumer Credit Reporting

Practice area: `consumer_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `consumer_product_or_service`, `debt_amount_usd`, `credit_limit_usd`, `finance_charge_usd`, `apr_percent`, `statutory_damages_usd`, `actual_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `consumer_statute`, `class_action_alleged`, `credit_score_or_report_issue`, `collection_fee_usd`

### `consumer_debt_collection` — Consumer Debt Collection

Practice area: `consumer_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `consumer_product_or_service`, `debt_amount_usd`, `credit_limit_usd`, `finance_charge_usd`, `apr_percent`, `statutory_damages_usd`, `actual_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `consumer_statute`, `class_action_alleged`, `credit_score_or_report_issue`, `collection_fee_usd`

### `consumer_lending` — Consumer Lending

Practice area: `consumer_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `consumer_product_or_service`, `debt_amount_usd`, `credit_limit_usd`, `finance_charge_usd`, `apr_percent`, `statutory_damages_usd`, `actual_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `consumer_statute`, `class_action_alleged`, `credit_score_or_report_issue`, `collection_fee_usd`

### `consumer_warranty` — Consumer Warranty

Practice area: `consumer_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `consumer_product_or_service`, `debt_amount_usd`, `credit_limit_usd`, `finance_charge_usd`, `apr_percent`, `statutory_damages_usd`, `actual_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `consumer_statute`, `class_action_alleged`, `credit_score_or_report_issue`, `collection_fee_usd`

### `copyright_dispute` — Copyright Dispute

Practice area: `intellectual_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `ip_asset_type`, `registration_or_patent_number`, `infringing_product_or_work`, `royalty_rate_percent`, `lost_profits_usd`, `statutory_damages_usd`, `injunction_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `corporate_governance_dispute` — Corporate Governance Dispute

Practice area: `commercial_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `transaction_type`, `transaction_amount_usd`, `unpaid_balance_usd`, `collateral_value_usd`, `share_count`, `ownership_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `goods_or_services`, `invoice_amount_usd`, `principal_amount_usd`, `guarantor_party`, `secured_party`

### `custodial_interrogation` — Custodial Interrogation

Practice area: `criminal_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `offense_category`, `conviction_status`, `sentence_months`, `probation_months`, `fine_amount_usd`, `restitution_amount_usd`, `mandatory_minimum_months`, `guideline_offense_level`, `criminal_history_category`, `drug_quantity`, `weapon_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `counts_of_conviction`, `offense_statutes`, `plea_type`, `suspended_sentence_months`, `supervised_release_months`, `sentence_consecutive_or_concurrent`, `time_served_credit_days`

### `custody_visitation` — Custody Visitation

Practice area: `family_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `child_count`, `custody_awarded_to`, `visitation_ordered`, `child_support_monthly_usd`, `support_arrears_usd`, `alimony_monthly_usd`, `marital_property_value_usd`, `property_division_amount_usd`, `domestic_violence_alleged`, `best_interest_factors_discussed`, `parenting_time_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `custody_modified`, `support_modified`, `arrears_period`, `income_parent_1_usd`, `income_parent_2_usd`, `income_parent_1_monthly_usd`, `income_parent_2_monthly_usd`, `child_support_guideline_amount_usd`, `child_support_deviation_monthly_usd`, `marital_debt_amount_usd`, `attorney_fees_requested`, `attorney_fees_awarded`

### `deceptive_consumer_practices` — Deceptive Consumer Practices

Practice area: `consumer_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `consumer_product_or_service`, `debt_amount_usd`, `credit_limit_usd`, `finance_charge_usd`, `apr_percent`, `statutory_damages_usd`, `actual_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `consumer_statute`, `class_action_alleged`, `credit_score_or_report_issue`, `collection_fee_usd`

### `defamation` — Defamation

Practice area: `tort_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `injury_type`, `injury_severity`, `medical_expenses_usd`, `lost_wages_usd`, `property_damage_usd`, `comparative_fault_percent`, `punitive_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `accident_date`, `death_claim`, `pain_suffering_usd`, `future_medical_expenses_usd`, `defendant_fault_percent`

### `detention_bond` — Detention Bond

Practice area: `immigration_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `immigration_relief_type`, `country_of_origin`, `removal_country`, `detention_days`, `bond_amount_usd`, `years_in_us`, `application_year`, `protected_ground`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `dischargeability_issue` — Dischargeability Issue

Practice area: `bankruptcy_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `bankruptcy_chapter`, `debtor_type`, `debt_amount_usd`, `claim_amount_usd`, `collateral_value_usd`, `plan_payment_usd`, `avoidance_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `petition_date`, `secured_debt_amount_usd`, `unsecured_debt_amount_usd`, `discharge_denied`, `stay_violation_damages_usd`

### `drug_offense` — Drug Offense

Practice area: `criminal_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `offense_category`, `conviction_status`, `sentence_months`, `probation_months`, `fine_amount_usd`, `restitution_amount_usd`, `mandatory_minimum_months`, `guideline_offense_level`, `criminal_history_category`, `drug_quantity`, `weapon_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `counts_of_conviction`, `offense_statutes`, `plea_type`, `suspended_sentence_months`, `supervised_release_months`, `sentence_consecutive_or_concurrent`, `time_served_credit_days`

### `duty_to_defend_indemnify` — Duty To Defend Indemnify

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `education_access_rights` — Education Access Rights

Practice area: `education_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `student_level`, `education_program`, `discipline_days`, `tuition_or_fees_usd`, `services_hours`, `accommodation_requested`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `education_regulatory_dispute` — Education Regulatory Dispute

Practice area: `education_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `student_level`, `education_program`, `discipline_days`, `tuition_or_fees_usd`, `services_hours`, `accommodation_requested`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `elective_share` — Elective Share

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `employment_discrimination` — Employment Discrimination

Practice area: `labor_employment_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `employee_role`, `protected_class`, `adverse_action`, `back_pay_usd`, `front_pay_usd`, `hourly_wage_usd`, `overtime_hours`, `statutory_penalty_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `employment_start_date`, `employment_end_date`, `annual_salary_usd`, `liquidated_damages_usd`, `employee_count`, `retaliation_protected_activity`

### `employment_retaliation` — Employment Retaliation

Practice area: `labor_employment_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `employee_role`, `protected_class`, `adverse_action`, `back_pay_usd`, `front_pay_usd`, `hourly_wage_usd`, `overtime_hours`, `statutory_penalty_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `employment_start_date`, `employment_end_date`, `annual_salary_usd`, `liquidated_damages_usd`, `employee_count`, `retaliation_protected_activity`

### `emtala_emergency_care` — Emtala Emergency Care

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `environmental_cleanup_cercla` — Environmental Cleanup Cercla

Practice area: `environmental_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `regulated_medium`, `pollutant_or_substance`, `cleanup_cost_usd`, `civil_penalty_usd`, `permit_limit_value`, `affected_area_acres`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `environmental_review_nepa` — Environmental Review Nepa

Practice area: `environmental_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `regulated_medium`, `pollutant_or_substance`, `cleanup_cost_usd`, `civil_penalty_usd`, `permit_limit_value`, `affected_area_acres`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `estate_accounting` — Estate Accounting

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `estate_creditor_claim` — Estate Creditor Claim

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `excuse_of_performance` — Excuse Of Performance

Practice area: `contract_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `contract_type`, `contract_amount_usd`, `unpaid_amount_usd`, `damages_claimed_usd`, `damages_awarded_usd`, `liquidated_damages_usd`, `interest_rate_percent`, `performance_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `breach_type`, `contract_date`, `breach_date`, `mitigation_amount_usd`, `specific_performance_ordered`, `rescission_ordered`

### `exhaustion_or_timeliness` — Exhaustion Or Timeliness

Practice area: `administrative_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `agency_name`, `agency_action_type`, `benefit_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `license_status`, `remand_to_agency`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `administrative_record_complete`, `hearing_date`, `benefit_period_start`, `benefit_period_end`, `license_or_permit_type`

### `final_agency_action` — Final Agency Action

Practice area: `administrative_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `agency_name`, `agency_action_type`, `benefit_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `license_status`, `remand_to_agency`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `administrative_record_complete`, `hearing_date`, `benefit_period_start`, `benefit_period_end`, `license_or_permit_type`

### `firearm_offense` — Firearm Offense

Practice area: `criminal_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `offense_category`, `conviction_status`, `sentence_months`, `probation_months`, `fine_amount_usd`, `restitution_amount_usd`, `mandatory_minimum_months`, `guideline_offense_level`, `criminal_history_category`, `drug_quantity`, `weapon_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `counts_of_conviction`, `offense_statutes`, `plea_type`, `suspended_sentence_months`, `supervised_release_months`, `sentence_consecutive_or_concurrent`, `time_served_credit_days`

### `foreclosure_mortgage` — Foreclosure Mortgage

Practice area: `real_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `property_type`, `property_value_usd`, `loan_balance_usd`, `foreclosure_judgment_usd`, `rent_monthly_usd`, `rent_arrears_usd`, `acreage`, `sale_price_usd`, `mortgage_principal_usd`, `default_amount_usd`, `sale_surplus_or_deficiency_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `property_address_or_description`, `lien_amount_usd`, `redemption_amount_usd`, `eviction_possession_awarded`, `lease_term_months`

### `guaranty_indemnity` — Guaranty Indemnity

Practice area: `contract_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `contract_type`, `contract_amount_usd`, `unpaid_amount_usd`, `damages_claimed_usd`, `damages_awarded_usd`, `liquidated_damages_usd`, `interest_rate_percent`, `performance_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `breach_type`, `contract_date`, `breach_date`, `mitigation_amount_usd`, `specific_performance_ordered`, `rescission_ordered`

### `guardianship_conservatorship` — Guardianship Conservatorship

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `hazardous_waste_rcra` — Hazardous Waste Rcra

Practice area: `environmental_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `regulated_medium`, `pollutant_or_substance`, `cleanup_cost_usd`, `civil_penalty_usd`, `permit_limit_value`, `affected_area_acres`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `health_disability_insurance` — Health Disability Insurance

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `health_information_privacy` — Health Information Privacy

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `health_professions_licensing` — Health Professions Licensing

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `healthcare_fraud_abuse` — Healthcare Fraud Abuse

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `innocent_spouse_relief` — Innocent Spouse Relief

Practice area: `tax_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `tax_years`, `taxpayer_type`, `deficiency_amount_usd`, `tax_liability_amount_usd`, `deduction_amount_usd`, `penalty_amount_usd`, `refund_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `tax_form_or_schedule`, `gross_income_amount_usd`, `adjusted_gross_income_usd`, `credit_amount_usd`, `accuracy_related_penalty_usd`, `fraud_penalty_usd`

### `insurance_agent_broker_liability` — Insurance Agent Broker Liability

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `insurance_bad_faith` — Insurance Bad Faith

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `insurance_regulatory_dispute` — Insurance Regulatory Dispute

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `intestate_succession` — Intestate Succession

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `landlord_tenant_eviction` — Landlord Tenant Eviction

Practice area: `real_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `property_type`, `property_value_usd`, `loan_balance_usd`, `foreclosure_judgment_usd`, `rent_monthly_usd`, `rent_arrears_usd`, `acreage`, `sale_price_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `property_address_or_description`, `lien_amount_usd`, `redemption_amount_usd`, `eviction_possession_awarded`, `lease_term_months`

### `leave_or_accommodation` — Leave Or Accommodation

Practice area: `labor_employment_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `employee_role`, `protected_class`, `adverse_action`, `back_pay_usd`, `front_pay_usd`, `hourly_wage_usd`, `overtime_hours`, `statutory_penalty_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `employment_start_date`, `employment_end_date`, `annual_salary_usd`, `liquidated_damages_usd`, `employee_count`, `retaliation_protected_activity`

### `liability_insurance_coverage` — Liability Insurance Coverage

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `life_insurance_benefits` — Life Insurance Benefits

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `limitation_of_liability` — Limitation Of Liability

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `maintenance_and_cure` — Maintenance And Cure

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `maritime_lien` — Maritime Lien

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `maritime_salvage` — Maritime Salvage

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `market_allocation` — Market Allocation

Practice area: `antitrust_competition_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `market_definition`, `market_share_percent`, `overcharge_amount_usd`, `treble_damages_usd`, `affected_sales_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `medical_malpractice` — Medical Malpractice

Practice area: `tort_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `injury_type`, `injury_severity`, `medical_expenses_usd`, `lost_wages_usd`, `property_damage_usd`, `comparative_fault_percent`, `punitive_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `accident_date`, `death_claim`, `pain_suffering_usd`, `future_medical_expenses_usd`, `defendant_fault_percent`

### `medicare_medicaid` — Medicare Medicaid

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `merger_challenge` — Merger Challenge

Practice area: `antitrust_competition_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `market_definition`, `market_share_percent`, `overcharge_amount_usd`, `treble_damages_usd`, `affected_sales_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `monell_liability` — Monell Liability

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `monopolization` — Monopolization

Practice area: `antitrust_competition_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `market_definition`, `market_share_percent`, `overcharge_amount_usd`, `treble_damages_usd`, `affected_sales_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `mortgage_servicing` — Mortgage Servicing

Practice area: `consumer_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `consumer_product_or_service`, `debt_amount_usd`, `credit_limit_usd`, `finance_charge_usd`, `apr_percent`, `statutory_damages_usd`, `actual_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `consumer_statute`, `class_action_alleged`, `credit_score_or_report_issue`, `collection_fee_usd`

### `naturalization_citizenship` — Naturalization Citizenship

Practice area: `immigration_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `immigration_relief_type`, `country_of_origin`, `removal_country`, `detention_days`, `bond_amount_usd`, `years_in_us`, `application_year`, `protected_ground`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `negligence_personal_injury` — Negligence Personal Injury

Practice area: `tort_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `injury_type`, `injury_severity`, `medical_expenses_usd`, `lost_wages_usd`, `property_damage_usd`, `comparative_fault_percent`, `punitive_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `accident_date`, `death_claim`, `pain_suffering_usd`, `future_medical_expenses_usd`, `defendant_fault_percent`

### `negotiable_instrument` — Negotiable Instrument

Practice area: `commercial_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `transaction_type`, `transaction_amount_usd`, `unpaid_balance_usd`, `collateral_value_usd`, `share_count`, `ownership_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `goods_or_services`, `invoice_amount_usd`, `principal_amount_usd`, `guarantor_party`, `secured_party`

### `parentage_adoption` — Parentage Adoption

Practice area: `family_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `child_count`, `custody_awarded_to`, `visitation_ordered`, `child_support_monthly_usd`, `support_arrears_usd`, `alimony_monthly_usd`, `marital_property_value_usd`, `property_division_amount_usd`, `domestic_violence_alleged`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `custody_modified`, `support_modified`, `arrears_period`, `income_parent_1_usd`, `income_parent_2_usd`, `income_parent_1_monthly_usd`, `income_parent_2_monthly_usd`, `child_support_guideline_amount_usd`, `child_support_deviation_monthly_usd`, `marital_debt_amount_usd`, `attorney_fees_requested`, `attorney_fees_awarded`

### `partition_ownership` — Partition Ownership

Practice area: `real_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `property_type`, `property_value_usd`, `loan_balance_usd`, `foreclosure_judgment_usd`, `rent_monthly_usd`, `rent_arrears_usd`, `acreage`, `sale_price_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `property_address_or_description`, `lien_amount_usd`, `redemption_amount_usd`, `eviction_possession_awarded`, `lease_term_months`

### `patent_dispute` — Patent Dispute

Practice area: `intellectual_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `ip_asset_type`, `registration_or_patent_number`, `infringing_product_or_work`, `royalty_rate_percent`, `lost_profits_usd`, `statutory_damages_usd`, `injunction_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `plan_confirmation` — Plan Confirmation

Practice area: `bankruptcy_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `bankruptcy_chapter`, `debtor_type`, `debt_amount_usd`, `claim_amount_usd`, `collateral_value_usd`, `plan_payment_usd`, `avoidance_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `petition_date`, `secured_debt_amount_usd`, `unsecured_debt_amount_usd`, `discharge_denied`, `stay_violation_damages_usd`

### `police_misconduct` — Police Misconduct

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `price_fixing` — Price Fixing

Practice area: `antitrust_competition_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `market_definition`, `market_share_percent`, `overcharge_amount_usd`, `treble_damages_usd`, `affected_sales_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `prisoner_rights` — Prisoner Rights

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `probate_administration` — Probate Administration

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `product_liability` — Product Liability

Practice area: `tort_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `injury_type`, `injury_severity`, `medical_expenses_usd`, `lost_wages_usd`, `property_damage_usd`, `comparative_fault_percent`, `punitive_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `accident_date`, `death_claim`, `pain_suffering_usd`, `future_medical_expenses_usd`, `defendant_fault_percent`

### `property_insurance_coverage` — Property Insurance Coverage

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `protection_order_family` — Protection Order Family

Practice area: `family_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `child_count`, `custody_awarded_to`, `visitation_ordered`, `child_support_monthly_usd`, `support_arrears_usd`, `alimony_monthly_usd`, `marital_property_value_usd`, `property_division_amount_usd`, `domestic_violence_alleged`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `custody_modified`, `support_modified`, `arrears_period`, `income_parent_1_usd`, `income_parent_2_usd`, `income_parent_1_monthly_usd`, `income_parent_2_monthly_usd`, `child_support_guideline_amount_usd`, `child_support_deviation_monthly_usd`, `marital_debt_amount_usd`, `attorney_fees_requested`, `attorney_fees_awarded`

### `provider_reimbursement` — Provider Reimbursement

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `public_health_regulation` — Public Health Regulation

Practice area: `health_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `health_program`, `provider_type`, `reimbursement_amount_usd`, `overpayment_amount_usd`, `civil_penalty_usd`, `patient_count`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `qualified_immunity` — Qualified Immunity

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `removability_ground` — Removability Ground

Practice area: `immigration_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `immigration_relief_type`, `country_of_origin`, `removal_country`, `detention_days`, `bond_amount_usd`, `years_in_us`, `application_year`, `protected_ground`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `school_governance` — School Governance

Practice area: `education_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `student_level`, `education_program`, `discipline_days`, `tuition_or_fees_usd`, `services_hours`, `accommodation_requested`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `seaman_personal_injury` — Seaman Personal Injury

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `section_1983_claim` — Section 1983 Claim

Practice area: `civil_rights_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `government_actor_type`, `constitutional_rights_invoked`, `force_or_misconduct_type`, `physical_injury_present`, `punitive_damages_usd`, `compensatory_damages_usd`, `nominal_damages_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `secured_transaction` — Secured Transaction

Practice area: `commercial_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `transaction_type`, `transaction_amount_usd`, `unpaid_balance_usd`, `collateral_value_usd`, `share_count`, `ownership_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `goods_or_services`, `invoice_amount_usd`, `principal_amount_usd`, `guarantor_party`, `secured_party`

### `securities_fraud` — Securities Fraud

Practice area: `securities_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `security_type`, `transaction_amount_usd`, `loss_amount_usd`, `share_count`, `class_period`, `misstatement_type`, `stock_price_drop_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `securities_registration_disclosure` — Securities Registration Disclosure

Practice area: `securities_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `security_type`, `transaction_amount_usd`, `loss_amount_usd`, `share_count`, `class_period`, `misstatement_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `sentencing_guideline_dispute` — Sentencing Guideline Dispute

Practice area: `criminal_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `offense_category`, `conviction_status`, `sentence_months`, `probation_months`, `fine_amount_usd`, `restitution_amount_usd`, `mandatory_minimum_months`, `guideline_offense_level`, `criminal_history_category`, `drug_quantity`, `weapon_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `counts_of_conviction`, `offense_statutes`, `plea_type`, `suspended_sentence_months`, `supervised_release_months`, `sentence_consecutive_or_concurrent`, `time_served_credit_days`

### `shareholder_derivative_action` — Shareholder Derivative Action

Practice area: `commercial_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `transaction_type`, `transaction_amount_usd`, `unpaid_balance_usd`, `collateral_value_usd`, `share_count`, `ownership_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `goods_or_services`, `invoice_amount_usd`, `principal_amount_usd`, `guarantor_party`, `secured_party`

### `shareholder_securities_action` — Shareholder Securities Action

Practice area: `securities_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `security_type`, `transaction_amount_usd`, `loss_amount_usd`, `share_count`, `class_period`, `misstatement_type`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `special_education_idea` — Special Education Idea

Practice area: `education_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `student_level`, `education_program`, `discipline_days`, `tuition_or_fees_usd`, `services_hours`, `accommodation_requested`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `species_habitat_protection` — Species Habitat Protection

Practice area: `environmental_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `regulated_medium`, `pollutant_or_substance`, `cleanup_cost_usd`, `civil_penalty_usd`, `permit_limit_value`, `affected_area_acres`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `student_discipline` — Student Discipline

Practice area: `education_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `student_level`, `education_program`, `discipline_days`, `tuition_or_fees_usd`, `services_hours`, `accommodation_requested`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `subrogation_contribution` — Subrogation Contribution

Practice area: `insurance_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `policy_type`, `insured_party`, `insurer_party`, `policy_limit_usd`, `coverage_amount_claimed_usd`, `coverage_amount_awarded_usd`, `claim_amount_usd`, `premium_amount_usd`, `defense_costs_usd`, `notice_delay_days`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `underlying_action_type`, `coverage_period_start`, `coverage_period_end`, `deductible_amount_usd`, `reservation_of_rights_issued`, `insurer_disclaimer_delay_days`, `insured_notice_delay_days`

### `support_obligation` — Support Obligation

Practice area: `family_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `child_count`, `custody_awarded_to`, `visitation_ordered`, `child_support_monthly_usd`, `support_arrears_usd`, `alimony_monthly_usd`, `marital_property_value_usd`, `property_division_amount_usd`, `domestic_violence_alleged`, `child_support_weekly_usd`, `payment_frequency`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `custody_modified`, `support_modified`, `arrears_period`, `income_parent_1_usd`, `income_parent_2_usd`, `income_parent_1_monthly_usd`, `income_parent_2_monthly_usd`, `child_support_guideline_amount_usd`, `child_support_deviation_monthly_usd`, `marital_debt_amount_usd`, `attorney_fees_requested`, `attorney_fees_awarded`

### `tax_deduction_issue` — Tax Deduction Issue

Practice area: `tax_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `tax_years`, `taxpayer_type`, `deficiency_amount_usd`, `tax_liability_amount_usd`, `deduction_amount_usd`, `penalty_amount_usd`, `refund_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `tax_form_or_schedule`, `gross_income_amount_usd`, `adjusted_gross_income_usd`, `credit_amount_usd`, `accuracy_related_penalty_usd`, `fraud_penalty_usd`

### `tax_deficiency_procedure` — Tax Deficiency Procedure

Practice area: `tax_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `tax_years`, `taxpayer_type`, `deficiency_amount_usd`, `tax_liability_amount_usd`, `deduction_amount_usd`, `penalty_amount_usd`, `refund_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `tax_form_or_schedule`, `gross_income_amount_usd`, `adjusted_gross_income_usd`, `credit_amount_usd`, `accuracy_related_penalty_usd`, `fraud_penalty_usd`

### `tax_liability_dispute` — Tax Liability Dispute

Practice area: `tax_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `tax_years`, `taxpayer_type`, `deficiency_amount_usd`, `tax_liability_amount_usd`, `deduction_amount_usd`, `penalty_amount_usd`, `refund_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `tax_form_or_schedule`, `gross_income_amount_usd`, `adjusted_gross_income_usd`, `credit_amount_usd`, `accuracy_related_penalty_usd`, `fraud_penalty_usd`

### `tax_penalty_issue` — Tax Penalty Issue

Practice area: `tax_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `tax_years`, `taxpayer_type`, `deficiency_amount_usd`, `tax_liability_amount_usd`, `deduction_amount_usd`, `penalty_amount_usd`, `refund_amount_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `tax_form_or_schedule`, `gross_income_amount_usd`, `adjusted_gross_income_usd`, `credit_amount_usd`, `accuracy_related_penalty_usd`, `fraud_penalty_usd`

### `termination_of_parental_rights` — Termination Of Parental Rights

Practice area: `family_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `child_count`, `custody_awarded_to`, `visitation_ordered`, `child_support_monthly_usd`, `support_arrears_usd`, `alimony_monthly_usd`, `marital_property_value_usd`, `property_division_amount_usd`, `domestic_violence_alleged`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `custody_modified`, `support_modified`, `arrears_period`, `income_parent_1_usd`, `income_parent_2_usd`, `income_parent_1_monthly_usd`, `income_parent_2_monthly_usd`, `child_support_guideline_amount_usd`, `child_support_deviation_monthly_usd`, `marital_debt_amount_usd`, `attorney_fees_requested`, `attorney_fees_awarded`

### `title_boundary_easement` — Title Boundary Easement

Practice area: `real_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `property_type`, `property_value_usd`, `loan_balance_usd`, `foreclosure_judgment_usd`, `rent_monthly_usd`, `rent_arrears_usd`, `acreage`, `sale_price_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `property_address_or_description`, `lien_amount_usd`, `redemption_amount_usd`, `eviction_possession_awarded`, `lease_term_months`

### `trade_secret_dispute` — Trade Secret Dispute

Practice area: `intellectual_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `ip_asset_type`, `registration_or_patent_number`, `infringing_product_or_work`, `royalty_rate_percent`, `lost_profits_usd`, `statutory_damages_usd`, `injunction_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `trademark_dispute` — Trademark Dispute

Practice area: `intellectual_property_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `ip_asset_type`, `registration_or_patent_number`, `infringing_product_or_work`, `royalty_rate_percent`, `lost_profits_usd`, `statutory_damages_usd`, `injunction_ordered`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `trust_administration` — Trust Administration

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `trust_breach_of_fiduciary_duty` — Trust Breach Of Fiduciary Duty

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `tying_exclusive_dealing` — Tying Exclusive Dealing

Practice area: `antitrust_competition_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `market_definition`, `market_share_percent`, `overcharge_amount_usd`, `treble_damages_usd`, `affected_sales_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `ucc_sales` — Ucc Sales

Practice area: `commercial_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `transaction_type`, `transaction_amount_usd`, `unpaid_balance_usd`, `collateral_value_usd`, `share_count`, `ownership_percent`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `goods_or_services`, `invoice_amount_usd`, `principal_amount_usd`, `guarantor_party`, `secured_party`

### `vessel_collision` — Vessel Collision

Practice area: `admiralty_maritime_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `vessel_type`, `cargo_value_usd`, `vessel_value_usd`, `salvage_award_usd`, `maintenance_rate_usd_per_day`, `injury_severity`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `wage_hour_dispute` — Wage Hour Dispute

Practice area: `labor_employment_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `employee_role`, `protected_class`, `adverse_action`, `back_pay_usd`, `front_pay_usd`, `hourly_wage_usd`, `overtime_hours`, `statutory_penalty_usd`, `minimum_wage_usd_per_hour`, `unpaid_overtime_usd`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`, `employment_start_date`, `employment_end_date`, `annual_salary_usd`, `liquidated_damages_usd`, `employee_count`, `retaliation_protected_activity`

### `water_pollution_regulation` — Water Pollution Regulation

Practice area: `environmental_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `regulated_medium`, `pollutant_or_substance`, `cleanup_cost_usd`, `civil_penalty_usd`, `permit_limit_value`, `affected_area_acres`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

### `will_contest` — Will Contest

Practice area: `trusts_estates_probate_law`

`primary_parties`, `requested_relief`, `awarded_relief`, `amount_claimed_usd`, `amount_awarded_usd`, `settlement_amount_usd`, `attorney_fees_usd`, `costs_usd`, `interest_amount_usd`, `relevant_dates`, `estate_value_usd`, `trust_value_usd`, `claim_amount_usd`, `beneficiary_count`, `fiduciary_role`, `accounting_period`, `current_court_disposition`, `lower_court_disposition`, `motion_or_order_at_issue`, `claim_count`, `award_modified_on_appeal`, `non_usd_amounts`

