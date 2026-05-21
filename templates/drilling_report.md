# Daily Drilling Report

## Well Information

| Field | Value |
|-------|-------|
| **Well Name** | {{well_name}} |
| **API Number** | {{api_number}} |
| **Operator** | {{operator}} |
| **Contractor** | {{drilling_contractor}} |
| **Rig Name/Number** | {{rig_name}} |
| **Field/Prospect** | {{field_name}} |
| **Location** | {{surface_location}} |
| **Elevation (KB)** | {{elevation_kb}} ft {{elevation_datum}} |
| **Spud Date** | {{spud_date}} |
| **Report Date** | {{report_date}} |
| **Report Number** | {{report_number}} |

---

## Well Objectives

{{well_objectives}}

**Target Formation:** {{target_formation}}  
**Target Depth:** {{target_depth_md}} MD / {{target_depth_tvd}} TVD  
**Proposed Total Depth:** {{proposed_td_md}} MD / {{proposed_td_tvd}} TVD

---

## Daily Operations Summary

### Depth Progress

| Parameter | Value |
|-----------|-------|
| **Depth at Start of Day** | {{start_depth_md}} MD / {{start_depth_tvd}} TVD |
| **Depth at End of Day** | {{end_depth_md}} MD / {{end_depth_tvd}} TVD |
| **Footage Drilled Today** | {{footage_today}} ft |
| **Current Hole Size** | {{hole_size}} in |
| **Current Casing** | {{current_casing}} |

### Time Summary

| Activity | Hours | % of Day |
|----------|-------|----------|
| Drilling | {{hours_drilling}} | {{pct_drilling}}% |
| Connections | {{hours_connections}} | {{pct_connections}}% |
| Circulating | {{hours_circulating}} | {{pct_circulating}}% |
| Tripping | {{hours_tripping}} | {{pct_tripping}}% |
| Surveying | {{hours_surveying}} | {{pct_surveying}}% |
| Reaming | {{hours_reaming}} | {{pct_reaming}}% |
| Rig Maintenance | {{hours_maintenance}} | {{pct_maintenance}}% |
| **Non-Productive Time (NPT)** | **{{hours_npt}}** | **{{pct_npt}}%** |
| **Total** | **24.0** | **100%** |

### NPT Breakdown

{{#each npt_events}}
| {{start_time}} | {{end_time}} | {{duration}} | {{category}} | {{description}} |
{{/each}}

**NPT Cumulative to Date:** {{npt_cumulative}} hours ({{npt_percentage}}%)

---

## Drilling Parameters

### Current Operations

| Parameter | Value | Unit |
|-----------|-------|------|
 **Weight on Bit (WOB)** | {{wob}} | kips |
| **Rotary RPM** | {{rpm}} | rev/min |
| **Torque** | {{torque}} | kft-lbs |
| **Standpipe Pressure** | {{spp}} | psi |
| **Flow Rate** | {{flow_rate}} | gpm |
| **Pump Strokes** | {{pump_strokes}} | spm |
| **Hook Load** | {{hook_load}} | kips |
| **Block Height** | {{block_height}} | ft |
| **ROP (Instantaneous)** | {{rop_instant}} | ft/hr |
| **ROP (Last Stand)** | {{rop_stand}} | ft/hr |

### Mud Properties

| Property | Value | Unit | Specification |
|----------|-------|------|---------------|
| **Mud Weight** | {{mud_weight}} | ppg | {{spec_mud_weight}} |
| **Funnel Viscosity** | {{funnel_visc}} | sec/qt | {{spec_funnel_visc}} |
| **Plastic Viscosity** | {{pv}} | cP | {{spec_pv}} |
| **Yield Point** | {{yp}} | lb/100ft² | {{spec_yp}} |
| **10-sec Gel** | {{gel_10s}} | lb/100ft² | {{spec_gel_10s}} |
| **10-min Gel** | {{gel_10m}} | lb/100ft² | {{spec_gel_10m}} |
| **Oil/Water Ratio** | {{oWR}} | % | {{spec_oWR}} |
| **H2S** | {{h2s}} | ppm | < {{spec_h2s}} |
| **Chlorides** | {{chlorides}} | mg/L | {{spec_chlorides}} |
| **Solids Content** | {{solids}} | % | < {{spec_solids}} |

### Hydraulics

| Parameter | Value | Unit |
|-----------|-------|------|
| **Annular Velocity** | {{annular_velocity}} | ft/min |
| **ECD at Casing Shoe** | {{ecd_casing}} | ppg |
| **ECD at TD** | {{ecd_td}} | ppg |
| **Surge Pressure** | {{surge_pressure}} | psi |
| **Swab Pressure** | {{swab_pressure}} | psi |

---

## Formation Evaluation

### Lithology

{{#each lithology_intervals}}
**Depth:** {{top_depth}} - {{base_depth}} ft  
**Formation:** {{formation_name}}  
**Lithology:** {{lithology_description}}  
**Show Description:** {{show_description}}  
**Cuttings Sample:** {{sample_depth}} ft

{{/each}}

### Gas Measurements

| Depth (ft) | C1 (ppm) | C2 (ppm) | C3 (ppm) | iC4 (ppm) | nC4 (ppm) | iC5 (ppm) | nC5 (ppm) | Total Gas (%) |
|------------|----------|----------|----------|-----------|-----------|-----------|-----------|---------------|
{{#each gas_readings}}
| {{depth}} | {{c1}} | {{c2}} | {{c3}} | {{ic4}} | {{nc4}} | {{ic5}} | {{nc5}} | {{total_gas}} |
{{/each}}

### Mud Logging Shows

{{#each shows}}
**Show #{{show_number}}**  
- **Depth:** {{show_top}} - {{show_base}} ft  
- **Type:** {{show_type}} (1-4 scale: {{show_intensity}})  
- **Description:** {{show_description}}  
- **Fluorescence:** {{fluorescence}}  
- **Cut:** {{cut_description}}

{{/each}}

### Wireline/LWD Logs

**Logs Run:** {{logs_run}}  
**Depth Range:** {{log_top}} - {{log_base}} ft  
**Key Observations:**
{{log_observations}}

---

## Directional Survey

### Well Trajectory

| MD (ft) | TVD (ft) | Inclination (°) | Azimuth (°) | N/S (ft) | E/W (ft) | DLS (°/100ft) |
|---------|----------|-----------------|-------------|----------|----------|---------------|
{{#each survey_stations}}
| {{md}} | {{tvd}} | {{inc}} | {{azm}} | {{ns}} | {{ew}} | {{dls}} |
{{/each}}

### Anti-Collision

**Current Separation from {{nearest_well}}:** {{separation_distance}} ft  
**Minimum Acceptable:** {{minimum_separation}} ft  
**Status:** {{anticollision_status}}

---

## Casing & Cementing

{{#if cementing_operations}}
### Cementing Summary

| Parameter | Value |
|-----------|-------|
| **Casing Size** | {{casing_size}} in |
| **Casing Weight** | {{casing_weight}} lb/ft |
| **Casing Grade** | {{casing_grade}} |
| **Setting Depth** | {{casing_setting_depth}} ft |
| **Shoe Track** | {{shoe_track_description}} |
| **Cement Slurry** | {{cement_slurry}} |
| **Lead Cement** | {{lead_cement_volume}} sx {{lead_cement_type}} |
| **Tail Cement** | {{tail_cement_volume}} sx {{tail_cement_type}} |
| **Cement Top (Planned)** | {{cement_top_planned}} ft |
| **Cement Top (Actual)** | {{cement_top_actual}} ft |
| **Cement Returns** | {{cement_returns}} |

**Cement Bond Log:** {{cbl_results}}
{{/if}}

---

## BHA & Drill String

### Current BHA

| Component | Description | Length (ft) | OD (in) | ID (in) | Weight (lb/ft) |
|-----------|-------------|-------------|---------|---------|----------------|
{{#each bha_components}}
| {{component}} | {{description}} | {{length}} | {{od}} | {{id}} | {{weight}} |
{{/each}}
| **Total BHA** | | **{{bha_total_length}}** | | | **{{bha_total_weight}}** |

### Drill Pipe

| Parameter | Value |
|-----------|-------|
| **Size** | {{dp_size}} in |
| **Weight** | {{dp_weight}} lb/ft |
| **Grade** | {{dp_grade}} |
| **Connection** | {{dp_connection}} |
| **Stand Length** | {{stand_length}} ft |
| **Total DP Length** | {{dp_total_length}} ft |

### Bit Record

| Parameter | Value |
|-----------|-------|
| **Bit Number** | {{bit_number}} |
| **Size** | {{bit_size}} in |
| **Manufacturer** | {{bit_manufacturer}} |
| **Model** | {{bit_model}} |
| **IADC Code** | {{bit_iadc}} |
| **Nozzles** | {{bit_nozzles}} |
| **TFA** | {{bit_tfa}} in² |
| **Footage** | {{bit_footage}} ft |
| **Hours** | {{bit_hours}} hrs |
| **ROP** | {{bit_rop}} ft/hr |
| **Dull Grade** | {{bit_dull_grade}} |
| **Dull Characteristics** | {{bit_dull_description}} |

---

## Safety & Incidents

### Safety Statistics

| Metric | Today | Cumulative |
|--------|-------|------------|
| **LTI** | {{lti_today}} | {{lti_cumulative}} |
| **TRI** | {{tri_today}} | {{tri_cumulative}} |
| **Near Misses** | {{near_miss_today}} | {{near_miss_cumulative}} |
| **Days Since LTI** | | {{days_since_lti}} |

### Incidents

{{#each incidents}}
**Incident #{{incident_number}}**  
- **Time:** {{incident_time}}  
- **Type:** {{incident_type}}  
- **Severity:** {{severity}}  
- **Description:** {{description}}  
- **Immediate Action:** {{immediate_action}}  
- **Investigation Required:** {{investigation_required}}

{{/each}}

### Safety Meetings

**Tool Box Talks:** {{toolbox_talks}}  
**Topics Covered:** {{safety_topics}}

---

## Personnel

| Company | On Duty | Off Duty | Total |
|---------|---------|----------|-------|
| Operator | {{operator_onduty}} | {{operator_offduty}} | {{operator_total}} |
| Drilling Contractor | {{contractor_onduty}} | {{contractor_offduty}} | {{contractor_total}} |
| Service Companies | {{service_onduty}} | {{service_offduty}} | {{service_total}} |
| **Total** | **{{total_onduty}}** | **{{total_offduty}}** | **{{total_personnel}}** |

**Key Personnel:**
- Company Man: {{company_man}}
- Toolpusher: {{toolpusher}}
- Driller: {{driller}}
- Mud Engineer: {{mud_engineer}}
- Mud Logger: {{mud_logger}}
- Directional Driller: {{directional_driller}}

---

## Equipment Status

| System | Status | Notes |
|--------|--------|-------|
| Drawworks | {{drawworks_status}} | {{drawworks_notes}} |
| Mud Pumps | {{pumps_status}} | {{pumps_notes}} |
| Top Drive/Rotary | {{rotary_status}} | {{rotary_notes}} |
| BOP | {{bop_status}} | {{bop_notes}} |
| Choke Manifold | {{choke_status}} | {{choke_notes}} |
| Mud System | {{mud_system_status}} | {{mud_system_notes}} |
| Solids Control | {{solids_control_status}} | {{solids_control_notes}} |
| Power Plant | {{power_status}} | {{power_notes}} |
| Derrick/Crown | {{derrick_status}} | {{derrick_notes}} |

---

## Weather & Environmental

| Parameter | Value |
|-----------|-------|
| **Weather** | {{weather_conditions}} |
| **Temperature** | {{temperature}} °F |
| **Wind** | {{wind_speed}} mph from {{wind_direction}} |
| **Barometric Pressure** | {{barometric_pressure}} inHg |
| **Sea State** | {{sea_state}} (if offshore) |
| **Visibility** | {{visibility}} miles |

**Environmental Incidents:** {{environmental_incidents}}  
**Discharges:** {{discharge_report}}

---

## Plans for Next 24 Hours

{{next_24h_plan}}

**Expected Depth:** {{expected_depth_md}} MD / {{expected_depth_tvd}} TVD  
**Critical Operations:** {{critical_operations}}

---

## Issues & Concerns

{{#each issues}}
**Issue #{{issue_number}}:** {{issue_description}}  
**Impact:** {{issue_impact}}  
**Mitigation:** {{issue_mitigation}}  
**Owner:** {{issue_owner}}

{{/each}}

---

## Approvals

| Role | Name | Signature | Date/Time |
|------|------|-----------|-----------|
| **Driller** | {{driller_name}} | _________________ | {{driller_datetime}} |
| **Toolpusher** | {{toolpusher_name}} | _________________ | {{toolpusher_datetime}} |
| **Company Man** | {{company_man_name}} | _________________ | {{company_man_datetime}} |

---

## Attachments

- [ ] Mud Report
- [ ] Survey Report
- [ ] Mud Log
- [ ] Wireline Logs
- [ ] CBL/VDL
- [ ] Daily Costs
- [ ] Incident Reports (if any)
- [ ] MWD/LWD Logs
- [ ] Cuttings Samples

---

**Report Prepared By:** {{preparer_name}}  
**Position:** {{preparer_position}}  
**Date/Time:** {{preparer_datetime}}  
**Contact:** {{preparer_contact}}