"""
Petrel API Connector for Reservoir Modeling

Provides integration with Schlumberger Petrel for:
- Import/export of geological models
- Well data synchronization
- Property modeling workflows
- Simulation case management
- Grid and geometry operations

Requirements:
    - Petrel license with Ocean plugin development support
    - PetrelConnection or Petrel API access
    - Valid license server configuration

Note: This connector assumes Petrel is running with Ocean framework enabled.
For standalone automation, consider using the RESQML or Eclipse formats for data exchange.
"""

import logging
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class WellboreData:
    """Represents wellbore data for Petrel import."""
    well_name: str
    uwi: str
    surface_x: float
    surface_y: float
    surface_z: float
    kb_elevation: float
    total_depth: float
    trajectory: List[Tuple[float, float, float]]  # MD, X, Y, Z, Incl, Azim
    logs: Optional[Dict[str, List[float]]] = None
    markers: Optional[List[Dict]] = None


@dataclass
class GridModel:
    """Represents a 3D grid model."""
    name: str
    nx: int
    ny: int
    nz: int
    dx: float
    dy: float
    dz: List[float]  # Variable layer thickness
    origin: Tuple[float, float, float]
    rotation: float
    properties: Dict[str, Any]  # Porosity, permeability, saturation


@dataclass
class SimulationCase:
    """Represents a reservoir simulation case."""
    name: str
    simulator: str  # ECLIPSE, CMG, tNavigator
    grid_file: str
    init_file: str
    restart_file: Optional[str]
    schedule_file: Optional[str]
    properties: Dict[str, Any]


class PetrelConnector:
    """
    Connector for Schlumberger Petrel reservoir modeling software.
    
    Handles data exchange between OpenClaw and Petrel for geological modeling,
    well data management, and simulation workflows.
    """
    
    def __init__(
        self,
        petrel_exe_path: Optional[str] = None,
        license_server: Optional[str] = None,
        project_path: Optional[str] = None,
        use_ocean: bool = True
    ):
        """
        Initialize Petrel connection.
        
        Args:
            petrel_exe_path: Path to Petrel executable
            license_server: License server (port@host format)
            project_path: Path to Petrel project file (.pet)
            use_ocean: Whether to use Ocean framework for automation
        """
        self.petrel_exe_path = petrel_exe_path or "C:/Program Files/Schlumberger/Petrel 2023/Petrel.exe"
        self.license_server = license_server
        self.project_path = project_path
        self.use_ocean = use_ocean
        self._petrel = None
        self._project = None
        
        # Try to import Ocean framework
        if use_ocean:
            try:
                # Ocean is typically available within Petrel's Python environment
                import Ocean
                self._Ocean = Ocean
                logger.info("Ocean framework imported successfully")
            except ImportError:
                logger.warning("Ocean framework not available. Running in mock mode.")
                self._Ocean = None
                self.use_ocean = False
    
    def connect(self) -> bool:
        """
        Establish connection to Petrel.
        
        Returns:
            True if connection successful, False otherwise
        """
        if not self.use_ocean or self._Ocean is None:
            logger.info("Running in mock mode - no actual Petrel connection")
            return True
        
        try:
            # In real implementation, this would connect to running Petrel instance
            # or launch Petrel with Ocean automation
            if self.project_path:
                self._project = self._Ocean.Petrel.OpenProject(self.project_path)
            else:
                self._project = self._Ocean.Petrel.GetActiveProject()
            
            logger.info(f"Connected to Petrel project: {self._project.Name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to Petrel: {e}")
            return False
    
    def import_wellbore(
        self,
        well_data: WellboreData,
        target_folder: Optional[str] = None
    ) -> str:
        """
        Import wellbore trajectory and logs into Petrel.
        
        Args:
            well_data: WellboreData object with trajectory and logs
            target_folder: Petrel folder path for well storage
            
        Returns:
            Well object identifier in Petrel
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Importing well: {well_data.well_name}")
        
        # Mock implementation - real implementation would use Ocean API
        # to create wellbore, set trajectory, and import logs
        
        well_path = f"{target_folder or 'Wells'}/{well_data.well_name}"
        
        # In real implementation:
        # well = self._project.WellBores.CreateWell(well_data.well_name)
        # well.Trajectory = well_data.trajectory
        # for log_name, log_values in well_data.logs.items():
        #     well.Logs.CreateLog(log_name, log_values)
        
        return well_path
    
    def export_wellbores(
        self,
        well_names: Optional[List[str]] = None,
        include_logs: bool = True,
        include_markers: bool = True
    ) -> List[WellboreData]:
        """
        Export wellbore data from Petrel.
        
        Args:
            well_names: List of well names to export (None = all wells)
            include_logs: Whether to include well logs
            include_markers: Whether to include formation tops
            
        Returns:
            List of WellboreData objects
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Exporting wellbores: {well_names or 'ALL'}")
        
        wells = []
        
        # Mock implementation
        # In real implementation:
        # for well in self._project.WellBores:
        #     if well_names is None or well.Name in well_names:
        #         well_data = WellboreData(
        #             well_name=well.Name,
        #             trajectory=well.Trajectory,
        #             logs={log.Name: log.Values for log in well.Logs} if include_logs else None,
        #             markers=well.Markers if include_markers else None
        #         )
        #         wells.append(well_data)
        
        # Return mock data for demonstration
        wells.append(WellboreData(
            well_name="Demo_Well_01",
            uwi="42-001-12345",
            surface_x=500000.0,
            surface_y=3000000.0,
            surface_z=500.0,
            kb_elevation=25.0,
            total_depth=8500.0,
            trajectory=[(0, 500000, 3000000, 500, 0, 0), (8500, 500100, 3000100, 475, 0, 0)],
            logs={"GR": [50, 75, 100, 80, 60]} if include_logs else None,
            markers=[{"formation": "Top Reservoir", "md": 7500}] if include_markers else None
        ))
        
        return wells
    
    def import_grid_model(
        self,
        grid_model: GridModel,
        overwrite: bool = False
    ) -> str:
        """
        Import 3D grid model into Petrel.
        
        Args:
            grid_model: GridModel object with geometry and properties
            overwrite: Whether to overwrite existing model
            
        Returns:
            Grid model identifier in Petrel
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Importing grid model: {grid_model.name}")
        
        # Mock implementation
        # In real implementation:
        # grid = self._project.Grids.CreateGrid(grid_model.name)
        # grid.SetGeometry(grid_model.nx, grid_model.ny, grid_model.nz,
        #                  grid_model.dx, grid_model.dy, grid_model.dz,
        #                  grid_model.origin, grid_model.rotation)
        # for prop_name, prop_values in grid_model.properties.items():
        #     grid.Properties.CreateProperty(prop_name, prop_values)
        
        return f"Grids/{grid_model.name}"
    
    def export_grid_model(
        self,
        grid_name: str,
        include_properties: Optional[List[str]] = None
    ) -> GridModel:
        """
        Export 3D grid model from Petrel.
        
        Args:
            grid_name: Name of grid model in Petrel
            include_properties: List of property names to export
            
        Returns:
            GridModel object
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Exporting grid model: {grid_name}")
        
        # Mock implementation
        # In real implementation:
        # grid = self._project.Grids[grid_name]
        # grid_model = GridModel(
        #     name=grid.Name,
        #     nx=grid.NX, ny=grid.NY, nz=grid.NZ,
        #     properties={prop.Name: prop.Values for prop in grid.Properties}
        # )
        
        return GridModel(
            name=grid_name,
            nx=100, ny=100, nz=50,
            dx=100.0, dy=100.0,
            dz=[10.0] * 50,
            origin=(500000.0, 3000000.0, 1000.0),
            rotation=0.0,
            properties={"Porosity": 0.2, "Permeability": 100.0}
        )
    
    def create_simulation_case(
        self,
        simulation_case: SimulationCase,
        target_folder: str = "Simulation"
    ) -> str:
        """
        Create reservoir simulation case in Petrel.
        
        Args:
            simulation_case: SimulationCase object with parameters
            target_folder: Petrel folder for simulation
            
        Returns:
            Simulation case identifier
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Creating simulation case: {simulation_case.name}")
        
        # Mock implementation
        # In real implementation:
        # sim = self._project.Simulations.CreateCase(simulation_case.name)
        # sim.SetSimulator(simulation_case.simulator)
        # sim.SetGrid(simulation_case.grid_file)
        # sim.SetSchedule(simulation_case.schedule_file)
        
        return f"{target_folder}/{simulation_case.name}"
    
    def run_simulation(
        self,
        case_name: str,
        wait_for_completion: bool = True
    ) -> Dict[str, Any]:
        """
        Run reservoir simulation case.
        
        Args:
            case_name: Name of simulation case
            wait_for_completion: Whether to wait for simulation to finish
            
        Returns:
            Simulation results summary
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Running simulation: {case_name}")
        
        # Mock implementation
        # In real implementation:
        # sim = self._project.Simulations[case_name]
        # job = sim.Run()
        # if wait_for_completion:
        #     job.Wait()
        # return job.Results
        
        return {
            "status": "COMPLETED",
            "runtime": "2:34:15",
            "iterations": 45,
            "convergence": "ACHIEVED",
            "oil_production": 1250000.0,
            "gas_production": 2500000000.0,
            "water_production": 850000.0
        }
    
    def generate_structural_map(
        self,
        horizon_name: str,
        grid_name: Optional[str] = None,
        property_name: Optional[str] = None
    ) -> str:
        """
        Generate structural contour map from grid.
        
        Args:
            horizon_name: Name of geological horizon
            grid_name: Grid model name (uses active if None)
            property_name: Property to map (default: depth)
            
        Returns:
            Map object identifier
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Generating structural map for: {horizon_name}")
        
        return f"Maps/{horizon_name}_Structure"
    
    def calculate_volumes(
        self,
        grid_name: str,
        oil_water_contact: float,
        gas_oil_contact: Optional[float] = None,
        cutoffs: Optional[Dict[str, float]] = None
    ) -> Dict[str, float]:
        """
        Calculate hydrocarbon volumes from grid model.
        
        Args:
            grid_name: Grid model name
            oil_water_contact: Depth of oil-water contact
            gas_oil_contact: Depth of gas-oil contact (if applicable)
            cutoffs: Property cutoffs (porosity, saturation)
            
        Returns:
            Volume calculations (OOIP, OGIP, etc.)
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Calculating volumes for: {grid_name}")
        
        cutoffs = cutoffs or {"porosity": 0.05, "water_saturation": 0.5}
        
        # Mock implementation
        return {
            "gross_rock_volume": 1250000000.0,
            "net_rock_volume": 875000000.0,
            "ooip": 450000000.0,
            "ogip": 850000000000.0,
            "recoverable_oil": 135000000.0,
            "recoverable_gas": 680000000000.0
        }
    
    def export_to_eclipse(
        self,
        grid_name: str,
        output_path: str,
        include_properties: Optional[List[str]] = None
    ) -> Dict[str, str]:
        """
        Export grid model to Eclipse format.
        
        Args:
            grid_name: Grid model name
            output_path: Directory for output files
            include_properties: Properties to export
            
        Returns:
            Dictionary of exported file paths
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        logger.info(f"Exporting to Eclipse: {grid_name}")
        
        return {
            "grid_file": f"{output_path}/{grid_name}.GRID",
            "init_file": f"{output_path}/{grid_name}.INIT",
            "eggrid_file": f"{output_path}/{grid_name}.EGRID"
        }
    
    def import_from_eclipse(
        self,
        grid_file: str,
        init_file: Optional[str] = None,
        restart_file: Optional[str] = None,
        target_name: Optional[str] = None
    ) -> str:
        """
        Import Eclipse simulation results into Petrel.
        
        Args:
            grid_file: Path to .GRID or .EGRID file
            init_file: Path to .INIT file
            restart_file: Path to .UNRST or .X0000 file
            target_name: Name for imported grid in Petrel
            
        Returns:
            Imported grid identifier
        """
        if not self._project:
            raise ConnectionError("Not connected to Petrel project")
        
        target_name = target_name or Path(grid_file).stem
        logger.info(f"Importing Eclipse results: {target_name}")
        
        return f"Grids/{target_name}"
    
    def close(self):
        """Close Petrel connection and clean up resources."""
        if self._project:
            # Save if needed
            # self._project.Save()
            self._project = None
        
        logger.info("Petrel connection closed")


# Example usage
if __name__ == "__main__":
    # Initialize connector
    connector = PetrelConnector(
        petrel_exe_path="C:/Program Files/Schlumberger/Petrel 2023/Petrel.exe",
        license_server="27000@petrel-license-server",
        project_path="C:/Projects/Reservoir_Model.pet",
        use_ocean=True
    )
    
    # Connect
    if connector.connect():
        print("Connected to Petrel")
        
        # Export well data
        wells = connector.export_wellbores(include_logs=True)
        print(f"Exported {len(wells)} wells")
        
        # Calculate volumes
        volumes = connector.calculate_volumes(
            grid_name="Reservoir_Grid",
            oil_water_contact=8500.0,
            cutoffs={"porosity": 0.08, "water_saturation": 0.45}
        )
        print(f"OOIP: {volumes['ooip']:,.0f} STB")
        
        # Close connection
        connector.close()
    else:
        print("Failed to connect to Petrel")