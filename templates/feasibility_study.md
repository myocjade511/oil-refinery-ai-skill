# Feasibility Study

## {{project_title}}

**Document Number:** {{document_number}}  
**Revision:** {{revision}}  
**Date:** {{study_date}}  
**Prepared By:** {{prepared_by}}  
**Company:** {{company_name}}

---

## Executive Summary

### Project Overview

{{project_overview}}

### Key Findings

{{#each key_findings}}
- {{this}}
{{/each}}

### Recommendation

**{{recommendation}}**

{{recommendation_rationale}}

### Economic Summary

| Metric | Value |
|--------|-------|
| **Total Investment** | ${{total_investment}} million |
| **NPV (10%)** | ${{npv_10}} million |
| **IRR** | {{irr}}% |
| **Payback Period** | {{payback_period}} years |
| **ROI** | {{roi}}% |

---

## 1. Introduction

### 1.1 Background

{{project_background}}

### 1.2 Objectives

{{#each objectives}}
1. {{this}}
{{/each}}

### 1.3 Scope

**Included in Scope:**
{{#each scope_included}}
- {{this}}
{{/each}}

**Excluded from Scope:**
{{#each scope_excluded}}
- {{this}}
{{/each}}

### 1.4 Study Basis

- **Study Date:** {{study_date}}
- **Currency:** {{currency}}
- **Base Year:** {{base_year}}
- **Evaluation Period:** {{evaluation_years}} years
- **Discount Rate:** {{discount_rate}}%

---

## 2. Technical Description

### 2.1 Location

**Site:** {{site_location}}  
**Coordinates:** {{coordinates}}  
**Land Area:** {{land_area}} acres  
**Access:** {{site_access}}

### 2.2 Reservoir/Feedstock Characteristics

{{#if is_upstream}}
**Reservoir Parameters:**

| Parameter | Value | Unit |
|-----------|-------|------|
| Reservoir Type | {{reservoir_type}} | - |
| Depth | {{reservoir_depth}} | ft |
| Area | {{reservoir_area}} | acres |
| Net Pay | {{net_pay}} | ft |
| Porosity | {{porosity}} | % |
| Permeability | {{permeability}} | md |
| Oil Gravity | {{oil_gravity}} | °API |
| Viscosity | {{oil_viscosity}} | cp |
| Initial Pressure | {{initial_pressure}} | psi |
| Temperature | {{reservoir_temperature}} | °F |
| OOIP | {{ooip}} | MMSTB |
| OGIP | {{ogip}} | Bscf |
{{/if}}

{{#if is_downstream}}
**Feedstock Characteristics:**

| Parameter | Value | Unit |
|-----------|-------|------|
| Feed Type | {{feed_type}} | - |
| API Gravity | {{feed_api}} | °API |
| Sulfur Content | {{sulfur_content}} | wt% |
| TAN | {{tan}} | mg KOH/g |
| Distillation | {{distillation_curve}} | - |
| Capacity | {{feed_capacity}} | BPSD |
{{/if}}

### 2.3 Process Description

{{process_description}}

**Process Flow:**

```
{{process_flow_diagram}}
```

**Major Equipment:**

| Equipment | Quantity | Specifications |
|-----------|----------|----------------|
{{#each major_equipment}}
| {{name}} | {{quantity}} | {{specifications}} |
{{/each}}

### 2.4 Technology Selection

**Selected Technology:** {{technology_name}}

**Selection Criteria:**
{{#each technology_criteria}}
- {{criterion}}: {{score}}/10 - {{justification}}
{{/each}}

**Alternatives Considered:**
{{#each alternatives}}
- **{{name}}:** {{description}} (Not selected because: {{reason}})
{{/each}}

---

## 3. Market Analysis

### 3.1 Supply and Demand

**Current Market:**
- Global Demand: {{global_demand}}
- Growth Rate: {{growth_rate}}% per year
- Regional Demand: {{regional_demand}}

**Price Forecast:**

| Year | {{product_name}} Price | Basis |
|------|------------------------|-------|
{{#each price_forecast}}
| {{year}} | ${{price}} | {{basis}} |
{{/each}}

### 3.2 Competition

**Competitive Landscape:**
{{#each competitors}}
- **{{name}}:** Capacity {{capacity}}, Location {{location}}
{{/each}}

**Competitive Advantage:**
{{competitive_advantage}}

### 3.3 Marketing Strategy

**Target Customers:**
{{#each target_customers}}
- {{segment}}: {{volume}} {{unit}}/year
{{/each}}

**Pricing Strategy:** {{pricing_strategy}}

**Sales and Distribution:**
{{sales_strategy}}

---

## 4. Environmental and Social Impact

### 4.1 Environmental Assessment

**Air Emissions:**

| Pollutant | Estimated Emissions | Permit Limit | Compliance |
|-----------|---------------------|--------------|------------|
{{#each air_emissions}}
| {{pollutant}} | {{emissions}} | {{limit}} | {{status}} |
{{/each}}

**Water Usage:**
- Fresh Water: {{fresh_water_usage}} m³/day
- Wastewater: {{wastewater_volume}} m³/day
- Treatment: {{water_treatment}}

**Waste Generation:**
{{#each waste_streams}}
- **{{type}}:** {{volume}} {{unit}}/year - {{disposal_method}}
{{/each}}

### 4.2 Social Impact

**Employment:**
- Construction: {{construction_jobs}} jobs
- Operations: {{operations_jobs}} jobs
- Indirect: {{indirect_jobs}} jobs

**Community Benefits:**
{{#each community_benefits}}
- {{this}}
{{/each}}

**Stakeholder Engagement:**
{{stakeholder_engagement_summary}}

### 4.3 Mitigation Measures

{{#each mitigation_measures}}
**{{category}}:**
- {{measure}}
- Cost: ${{cost}} million
{{/each}}

---

## 5. Implementation Plan

### 5.1 Schedule

| Phase | Duration | Start | Finish |
|-------|----------|-------|--------|
{{#each schedule_phases}}
| {{phase}} | {{duration}} | {{start_date}} | {{end_date}} |
{{/each}}

**Critical Path:**
{{critical_path_activities}}

### 5.2 Organization

**Project Team:**

| Role | Responsibility |
|------|----------------|
{{#each project_team}}
| {{role}} | {{responsibility}} |
{{/each}}

**Contracting Strategy:** {{contracting_strategy}}

### 5.3 Risk Management

**Risk Register:**

| Risk | Probability | Impact | Mitigation | Residual Risk |
|------|-------------|--------|------------|---------------|
{{#each risks}}
| {{description}} | {{probability}} | {{impact}} | {{mitigation}} | {{residual}} |
{{/each}}

---

## 6. Economic Analysis

### 6.1 Capital Cost Estimate

| Category | Cost ($ million) | Basis |
|----------|------------------|-------|
{{#each capex_breakdown}}
| {{category}} | ${{cost}} | {{basis}} |
{{/each}}
| **Total Capital Cost** | **${{total_capex}}** | |

**Cost Estimate Accuracy:** {{estimate_accuracy}}

### 6.2 Operating Cost Estimate

| Category | Annual Cost ($ million) |
|----------|-------------------------|
{{#each opex_breakdown}}
| {{category}} | ${{cost}} |
{{/each}}
| **Total Operating Cost** | **${{total_opex}}** |

**Unit Operating Cost:** ${{unit_opex}} per {{unit}}

### 6.3 Revenue Projection

| Year | Production | Price | Revenue |
|------|------------|-------|---------|
{{#each revenue_projection}}
| {{year}} | {{production}} | ${{price}} | ${{revenue}} |
{{/each}}

### 6.4 Cash Flow Analysis

| Year | Capital | Operating | Revenue | Net Cash Flow | Cumulative |
|------|---------|-----------|---------|---------------|------------|
{{#each cash_flow}}
| {{year}} | ${{capex}} | ${{opex}} | ${{revenue}} | ${{net_cf}} | ${{cumulative}} |
{{/each}}

### 6.5 Economic Indicators

**Base Case:**

| Indicator | Value | Unit |
|-----------|-------|------|
| NPV @ 10% | ${{npv_10}} | million |
| NPV @ 15% | ${{npv_15}} | million |
| IRR | {{irr}} | % |
| Payout (undiscounted) | {{payout_simple}} | years |
| Payout (discounted) | {{payout_discounted}} | years |
| Profitability Index | {{pi}} | - |
| EMV | ${{emv}} | million |

### 6.6 Sensitivity Analysis

**Tornado Diagram Data:**

| Variable | Low Case | Base Case | High Case | NPV Impact |
|----------|----------|-----------|-----------|------------|
{{#each sensitivity_variables}}
| {{variable}} | {{low}} | {{base}} | {{high}} | ${{npv_impact}} |
{{/each}}

**Scenario Analysis:**

| Scenario | NPV | IRR | Description |
|----------|-----|-----|-------------|
| Pessimistic | ${{npv_pessimistic}} | {{irr_pessimistic}}% | {{pessimistic_assumptions}} |
| Base Case | ${{npv_base}} | {{irr_base}}% | {{base_assumptions}} |
| Optimistic | ${{npv_optimistic}} | {{irr_optimistic}}% | {{optimistic_assumptions}} |

### 6.7 Break-Even Analysis

**Break-Even Price:** ${{breakeven_price}} per {{unit}}

**Break-Even Production:** {{breakeven_production}} {{unit}}/year

---

## 7. Financing

### 7.1 Capital Structure

| Source | Amount ($ million) | % | Terms |
|--------|-------------------|---|-------|
{{#each financing_sources}}
| {{source}} | ${{amount}} | {{percentage}}% | {{terms}} |
{{/each}}
| **Total** | **${{total_financing}}** | **100%** | |

### 7.2 Debt Service

**Loan Terms:**
- Principal: ${{loan_principal}} million
- Interest Rate: {{interest_rate}}%
- Term: {{loan_term}} years
- Grace Period: {{grace_period}} years

**Debt Service Coverage Ratio:** {{dscr}}

---

## 8. Conclusions and Recommendations

### 8.1 Conclusions

{{#each conclusions}}
1. {{this}}
{{/each}}

### 8.2 Recommendations

**Primary Recommendation:**
{{primary_recommendation}}

**Next Steps:**
{{#each next_steps}}
1. {{action}} - {{timeline}} - {{responsible}}
{{/each}}

### 8.3 Critical Success Factors

{{#each critical_success_factors}}
- {{factor}}
{{/each}}

---

## Appendices

### Appendix A: Detailed Cost Estimates

{{appendix_a}}

### Appendix B: Process Flow Diagrams

{{appendix_b}}

### Appendix C: Equipment Lists

{{appendix_c}}

### Appendix D: Site Plans

{{appendix_d}}

### Appendix E: Environmental Permits

{{appendix_e}}

### Appendix F: Market Study Data

{{appendix_f}}

---

## Document Control

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
{{#each revisions}}
| {{number}} | {{date}} | {{author}} | {{description}} |
{{/each}}

**Approvals:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | {{pm_name}} | _________________ | {{pm_date}} |
| Technical Lead | {{tl_name}} | _________________ | {{tl_date}} |
| Economic Analyst | {{ea_name}} | _________________ | {{ea_date}} |
| Engineering Manager | {{em_name}} | _________________ | {{em_date}} |

---

*This document contains confidential and proprietary information. Unauthorized distribution is prohibited.*