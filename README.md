# Oil Refinery & Oil Field Development AI

A comprehensive AI skill for oil & gas operations covering the complete value chain from exploration to refining.

## Installation

Copy the `oil-refinery-ai-skill` folder to your OpenClaw skills directory:

```bash
# Default location
cp -r oil-refinery-ai-skill /usr/local/lib/node_modules/openclaw/skills/

# Or user workspace
cp -r oil-refinery-ai-skill ~/.openclaw/workspace/skills/
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ARCGIS_API_KEY` | Optional | For ArcGIS geological mapping integration |
| `PETREL_LICENSE` | Optional | For Petrel reservoir modeling connection |
| `SCADA_ENDPOINT` | Optional | SCADA system URL for real-time data |
| `REFINERY_SIM_URL` | Optional | Refinery simulator API endpoint |

### Example .env file

```bash
ARCGIS_API_KEY=your_arcgis_key_here
PETREL_LICENSE=your_petrel_license
SCADA_ENDPOINT=https://scada.yourcompany.com/api
REFINERY_SIM_URL=https://simulator.yourcompany.com/v1
```

## Supported Commands

- **Geological analysis**: Seismic interpretation, reserve estimation
- **Drilling optimization**: Well planning, parameter recommendations
- **Refinery design**: Process unit design, heat integration
- **Safety compliance**: HAZOP support, regulatory checking
- **Financial modeling**: CAPEX/OPEX, feasibility studies

## Out of Scope

- Real-time well control decisions (requires human operator)
- Emergency shutdown procedures
- Regulatory permit filing (generates drafts only)
- Equipment procurement (provides specifications only)

## Safety & Compliance

⚠️ **Important**: This skill provides analytical support and recommendations only. All operational decisions must be:
- Validated by qualified petroleum engineers
- Reviewed against current regulations
- Approved through proper company procedures

## Version History

- **1.0.0** - Initial release with core workflows for exploration, drilling, refining, and compliance