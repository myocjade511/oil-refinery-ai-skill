# HAZOP Study Worksheet

## Study Information

**Facility:** {{facility_name}}  
**Unit/Node:** {{unit_node}}  
**P&ID Number:** {{pandid_number}}  
**Study Date:** {{study_date}}  
**Session:** {{session_number}} of {{total_sessions}}  
**Location:** {{study_location}}

## Team Members

| Role | Name | Organization | Signature |
|------|------|--------------|-----------|
| HAZOP Leader | {{leader_name}} | {{leader_org}} | _________________ |
| Scribe/Recorder | {{scribe_name}} | {{scribe_org}} | _________________ |
| Process Engineer | {{pe_name}} | {{pe_org}} | _________________ |
| Operations Representative | {{ops_name}} | {{ops_org}} | _________________ |
| Control Systems Engineer | {{cse_name}} | {{cse_org}} | _________________ |
| Maintenance Representative | {{maint_name}} | {{maint_org}} | _________________ |
{{#each additional_members}}
| {{role}} | {{name}} | {{org}} | _________________ |
{{/each}}

## Design Intent

**Node Description:**
{{node_description}}

**Design Conditions:**

| Parameter | Design Value | Unit | Operating Range |
|-----------|--------------|------|-----------------|
{{#each design_conditions}}
| {{parameter}} | {{design_value}} | {{unit}} | {{operating_range}} |
{{/each}}

**Process Intent:**
{{process_intent}}

**Boundaries:**
- Start: {{boundary_start}}
- End: {{boundary_end}}
- Includes: {{boundary_includes}}
- Excludes: {{boundary_excludes}}

## Guide Words and Parameters

### Standard Guide Words

| Guide Word | Meaning |
|------------|---------|
| NO | Negation of intent (none, not) |
| MORE | Quantitative increase (higher, longer) |
| LESS | Quantitative decrease (lower, shorter) |
| AS WELL AS | Qualitative increase (additional) |
| PART OF | Qualitative decrease (partial) |
| REVERSE | Opposite of intent (reverse flow) |
| OTHER THAN | Substitution (different material) |
| EARLY | Relative to clock time |
| LATE | Relative to clock time |
| BEFORE | Relative to order |
| AFTER | Relative to order |

### Parameters to Consider

- Flow
- Temperature
- Pressure
- Level
- Composition
- Phase
- pH
- Viscosity
- Reaction Rate
- Mixing
- Separation
- Corrosion/Erosion
- Utility Failure
- Maintenance
- Startup/Shutdown

## HAZOP Analysis

{{#each deviations}}
### {{number}}. {{guide_word}} + {{parameter}}

**Deviation:** {{deviation_description}}

**Causes:**
{{#each causes}}
{{number}}. {{description}}
   - Likelihood: {{likelihood}} ({{likelihood_rating}})
{{/each}}

**Consequences:**
{{#each consequences}}
{{number}}. {{description}}
   - Severity: {{severity}} ({{severity_rating}})
   - Category: {{category}}
{{/each}}

**Safeguards (Existing):**
{{#each safeguards}}
{{number}}. {{description}} ({{type}})
{{/each}}

**Risk Ranking:**

| Without Safeguards | With Safeguards |
|-------------------|-----------------|
| {{risk_without}} | {{risk_with}} |

**Risk Matrix:**
- Likelihood: {{final_likelihood}}
- Severity: {{final_severity}}
- Risk Level: {{risk_level}}

**Recommendations/Actions:**
{{#each recommendations}}
{{number}}. **{{priority}}** - {{description}}
   - Assigned To: {{assigned_to}}
   - Target Date: {{target_date}}
   - Status: {{status}}
{{/each}}

**Comments:**
{{comments}}

---

{{/each}}

## Summary

### Risk Distribution

| Risk Level | Count | Percentage |
|------------|-------|------------|
| High | {{high_count}} | {{high_pct}}% |
| Medium | {{medium_count}} | {{medium_pct}}% |
| Low | {{low_count}} | {{low_pct}}% |
| Negligible | {{negligible_count}} | {{negligible_pct}}% |

### Recommendations Summary

| Priority | Count | Open | Closed |
|----------|-------|------|--------|
| Critical | {{critical_count}} | {{critical_open}} | {{critical_closed}} |
| High | {{high_rec_count}} | {{high_open}} | {{high_closed}} |
| Medium | {{medium_rec_count}} | {{medium_open}} | {{medium_closed}} |
| Low | {{low_rec_count}} | {{low_open}} | {{low_closed}} |

### Action Items Register

| No. | Description | Priority | Assigned To | Due Date | Status | Closure Date |
|-----|-------------|----------|-------------|----------|--------|--------------|
{{#each action_items}}
| {{number}} | {{description}} | {{priority}} | {{assigned}} | {{due}} | {{status}} | {{closed}} |
{{/each}}

## Appendices

### Appendix A: P&ID Drawings
{{pandid_references}}

### Appendix B: Process Description
{{process_description_detailed}}

### Appendix C: Equipment Data Sheets
{{equipment_datasheets}}

### Appendix D: Cause-by-Cause Analysis (if required)
{{detailed_cause_analysis}}

### Appendix E: Consequence Analysis (if required)
{{detailed_consequence_analysis}}

### Appendix F: Previous HAZOP Actions Status
{{previous_actions_status}}

---

## Sign-Off

### Team Certification

We, the undersigned, certify that:

1. We have participated in the HAZOP study as indicated above.
2. We have reviewed and agree with the contents of this worksheet.
3. We understand our responsibilities for implementing the recommended actions assigned to us.
4. We acknowledge that this HAZOP study has been conducted in accordance with {{standard_reference}}.

**HAZOP Leader:**

Signature: _________________________ Date: _________________

Name: {{leader_name}}

**Process Engineer:**

Signature: _________________________ Date: _________________

Name: {{pe_name}}

**Operations Representative:**

Signature: _________________________ Date: _________________

Name: {{ops_name}}

### Management Approval

I have reviewed this HAZOP study and approve the recommendations. I commit to providing the necessary resources for implementation.

**Facility Manager:**

Signature: _________________________ Date: _________________

Name: {{facility_manager_name}}

Title: {{facility_manager_title}}

---

## Revision History

| Revision | Date | Description | Author | Approved By |
|----------|------|-------------|--------|-------------|
{{#each revisions}}
| {{number}} | {{date}} | {{description}} | {{author}} | {{approver}} |
{{/each}}

---

## Next Review

**Scheduled Review Date:** {{next_review_date}}

**Trigger for Earlier Review:**
- [ ] Incident investigation requires
- [ ] Major process change
- [ ] New regulatory requirement
- [ ] Operating experience indicates
- [ ] Other: {{other_trigger}}

---

*This document is confidential and proprietary. Distribution is limited to authorized personnel.*

**Document Control:**
- Document Number: {{document_number}}
- Revision: {{revision}}
- Effective Date: {{effective_date}}
- Supersedes: {{supersedes}}