---
name: Oil Refinery & Oil Field Development AI
slug: oil-refinery-ai-skill
author: Ho Ba
source: https://github.com/openclaw/skills/oil-refinery-ai-skill
description: Comprehensive AI assistant for oil refinery operations and oil field development. Supports geological analysis, drilling optimization, refinery design, safety compliance, and financial modeling for upstream and downstream oil & gas operations.
version: 1.0.0
---

# Oil Refinery & Oil Field Development AI

This skill provides specialized AI assistance for the complete oil & gas lifecycle — from exploration and extraction to refining and distribution.

## Capabilities

### 1. Geological Analysis
- Seismic data interpretation (2D/3D/4D)
- Reservoir characterization and modeling
- Reserve estimation (deterministic and probabilistic)
- Basin analysis and prospect evaluation
- Well log analysis and petrophysics

**See:** [prompts/geology.txt](prompts/geology.txt) for detailed interpretation workflows

### 2. Drilling Operations
- Well planning and trajectory design
- Drilling parameter optimization
- Real-time drilling analysis
- BHA design and optimization
- Wellbore stability analysis
- Cost estimation and AFE preparation

**See:** [prompts/drilling.txt](prompts/drilling.txt) for operational guidance

### 3. Refinery Design & Operations
- Process unit design (CDU, VDU, FCC, hydrocracker, reformer)
- Heat exchanger network optimization
- Utility system design (steam, power, cooling water)
- Capacity planning and debottlenecking
- Process simulation and optimization

**See:** [prompts/refinery_design.txt](prompts/refinery_design.txt)

### 4. Safety & Compliance
- HAZOP (Hazard and Operability) analysis
- LOPA (Layer of Protection Analysis)
- Safety system design (SIS, PSD)
- Regulatory compliance (API, ASME, OSHA, EPA)
- Environmental impact assessment

**See:** [prompts/safety.txt](prompts/safety.txt)

### 5. Financial Modeling
- CAPEX/OPEX estimation
- Feasibility studies and economic analysis
- NPV/IRR/ROI calculations
- Risk analysis and Monte Carlo simulation
- Portfolio optimization

**See:** [prompts/finance.txt](prompts/finance.txt)

## Workflows

### Reserve Estimation Workflow
**File:** [workflows/reserve_estimation.yaml](workflows/reserve_estimation.yaml)

Comprehensive 8-step workflow for estimating oil/gas reserves following SPE-PRMS guidelines:
1. Data Quality Validation
2. Reservoir Characterization
3. Bulk Rock Volume Calculation
4. Original Hydrocarbons In Place (OOIP/OGIP)
5. Recovery Factor Analysis
6. Monte Carlo Probabilistic Assessment
7. Uncertainty Documentation
8. Report Generation

Includes deterministic and probabilistic methods with full uncertainty quantification.

### Extraction Strategy Workflow
**File:** [workflows/extraction_strategy.yaml](workflows/extraction_strategy.yaml)

Optimize production strategies including:
- Primary depletion planning
- Secondary recovery (waterflood design)
- Enhanced Oil Recovery (EOR) screening
- Gas injection strategies
- Artificial lift selection and optimization

### Refinery Planning Workflow
**File:** [workflows/refinery_planning.yaml](workflows/refinery_planning.yaml)

Plan refinery configurations for different crude slates:
- Crude unit design (CDU/VDU)
- Conversion unit selection (FCC, hydrocracker, coker)
- Product slate optimization
- Hydrogen balance and production
- Utility system sizing

### Compliance Workflow
**File:** [workflows/compliance_workflow.yaml](workflows/compliance_workflow.yaml)

Ensure operations meet safety and environmental regulations:
- Regulatory requirement mapping
- Compliance gap analysis
- Permit application support
- Inspection preparation
- Incident investigation

## Integrations

### ArcGIS Connector
**File:** [integrations/arcgis.py](integrations/arcgis.py)

Full-featured Python connector for ArcGIS Online/Enterprise:
- Well data search and visualization
- Seismic survey management
- Structure map generation
- Cross-section creation
- Area calculations for lease/closures
- Export to Petrel and other platforms

**Features:**
- Authentication via API key or named user
- Spatial queries with attribute filtering
- Hosted feature service creation
- GeoJSON and shapefile support
- Coordinate system handling

### Petrel API
**File:** [integrations/petrel_api.py](integrations/petrel_api.py)

Interface with Schlumberger Petrel for reservoir modeling:
- Import/export of grid models
- Well data synchronization
- Property modeling workflows
- Simulation case management

### SCADA Connector
**File:** [integrations/scada_connector.py](integrations/scada_connector.py)

Real-time data integration from refinery SCADA systems:
- Tag browsing and subscription
- Historical data retrieval
- Alarm management
- Trend analysis

### Refinery Simulator
**File:** [integrations/refinery_simulator.py](integrations/refinery_simulator.py)

Process simulation integration:
- Aspen HYSYS/Aspen Plus connectivity
- Pro/II interface
- Unisim Design integration
- Case study management

## Templates

### Drilling Report
**File:** [templates/drilling_report.md](templates/drilling_report.md)

Comprehensive daily drilling report template including:
- Well information and objectives
- Daily operations summary with time breakdown
- Drilling parameters and mud properties
- Formation evaluation (lithology, gas, shows)
- Directional survey data
- Casing and cementing details
- BHA and drill string specifications
- Safety statistics and incidents
- Personnel tracking
- Equipment status
- Weather and environmental data
- 24-hour look-ahead plans

### Permit Application
**File:** [templates/permit_report.md](templates/permit_report.md)

Regulatory permit application template for:
- Drilling permits
- Workover permits
- Production facility permits
- Environmental permits

### Feasibility Study
**File:** [templates/feasibility_study.md](templates/feasibility_study.md)

Full project feasibility study including:
- Executive summary
- Technical description
- Market analysis
- Economic evaluation
- Risk assessment
- Implementation plan

## Usage Examples

### Geological Analysis
```
"Analyze this seismic line for potential structural traps. 
The data shows a prominent anticline at 2.5 seconds TWT 
with amplitude dimming on the flanks."
```

### Reserve Estimation
```
"Run a reserve estimation for the following:
- Area: 2,500 acres
- Net pay: 45 feet
- Porosity: 18% (from core)
- Water saturation: 25%
- Oil gravity: 38° API
- Bubble point: 2,500 psi
- Need P10/P50/P90 estimates"
```

### Drilling Optimization
```
"Optimize drilling parameters for a 12¼" section 
in the Wolfcamp shale at 12,500 ft MD:
- Current ROP: 45 ft/hr
- Current WOB: 35 kips
- Current RPM: 120
- Mud weight: 14.2 ppg"
```

### Refinery Design
```
"Design a crude distillation unit for 150,000 bpd 
of mixed Middle Eastern crudes:
- 50% Arab Light
- 30% Arab Medium  
- 20% Arab Heavy
Target products: LPG, naphtha, jet, diesel, VGO, resid"
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ARCGIS_API_KEY` | Optional | ArcGIS Online/Enterprise API key |
| `ARCGIS_PORTAL_URL` | Optional | Enterprise portal URL (default: ArcGIS Online) |
| `PETREL_LICENSE` | Optional | Petrel license server |
| `SCADA_ENDPOINT` | Optional | SCADA system API endpoint |
| `SCADA_USERNAME` | Optional | SCADA credentials |
| `SCADA_PASSWORD` | Optional | SCADA credentials |
| `REFINERY_SIM_URL` | Optional | Process simulator API |

### Example .env file

```bash
# ArcGIS Configuration
ARCGIS_API_KEY=your_arcgis_api_key_here
ARCGIS_PORTAL_URL=https://your-org.maps.arcgis.com

# Petrel Configuration
PETREL_LICENSE=27000@petrel-license-server

# SCADA Configuration
SCADA_ENDPOINT=https://scada.yourcompany.com/api/v1
SCADA_USERNAME=openclaw_user
SCADA_PASSWORD=secure_password

# Refinery Simulator
REFINERY_SIM_URL=https://simulator.yourcompany.com/api
```

## Safety & Compliance Notes

⚠️ **Critical Warnings:**

1. **This skill provides analytical support only.** All operational decisions must be validated by qualified petroleum engineers and geoscientists.

2. **Regulatory Compliance:** Generated reports and analyses are starting points. Final submissions must be reviewed by regulatory specialists.

3. **Safety-Critical Systems:** Never use this skill for real-time well control decisions, emergency shutdown procedures, or safety system programming.

4. **Data Security:** Well locations, production data, and reservoir characteristics may be sensitive. Ensure compliance with data protection requirements.

5. **Professional Judgment:** AI cannot replace the experience and judgment of qualified professionals. Always apply appropriate skepticism to AI-generated recommendations.

## Best Practices

### Data Quality
- Always validate input data before analysis
- Document data sources and quality flags
- Apply appropriate uncertainty ranges
- Cross-check results with analog fields

### Uncertainty Management
- Use probabilistic methods when data is limited
- Document all assumptions clearly
- Perform sensitivity analysis on key parameters
- Present results with appropriate confidence intervals

### Integration
- Test API connections before production use
- Implement proper error handling
- Monitor rate limits and quotas
- Cache results where appropriate

## References

### Industry Standards
- SPE Petroleum Resources Management System (PRMS) 2018
- API RP 14C - Analysis, Design, Installation, and Testing of Safety Systems
- API 510 - Pressure Vessel Inspection Code
- ASME BPVC Section VIII - Pressure Vessels
- ISO 13628 - Petroleum and natural gas industries

### Recommended Reading
- "Petroleum Geoscience" by Jon Gluyas and Richard Swarbrick
- "Petroleum Reservoir Engineering" by Amyx, Bass, and Whiting
- "Petroleum Refining: Technology and Economics" by Gary, Handwerk, and Kaiser
- "Standard Handbook of Petroleum and Natural Gas Engineering" by Lyons and Plisga

## Support

For issues or feature requests:
- Review the [README.md](README.md) for troubleshooting
- Check integration-specific documentation in `integrations/`
- Consult workflow documentation in `workflows/`

## Version History

- **1.0.0** - Initial release
  - Core geological analysis workflows
  - Reserve estimation with SPE-PRMS compliance
  - Drilling operations support
  - Refinery design capabilities
  - ArcGIS integration
  - Comprehensive drilling report template