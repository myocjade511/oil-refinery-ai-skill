"""
ArcGIS Connector for Petroleum Geoscience Workflows

Provides integration with ArcGIS Online and ArcGIS Enterprise for:
- Geological mapping and spatial analysis
- Well data visualization
- Seismic survey management
- Contour mapping and surface generation
- Cross-section creation

Requirements:
    - ArcGIS API for Python (arcgis package)
    - Valid ArcGIS Online or Enterprise license
    - API key or named user credentials
"""

import json
import logging
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class WellLocation:
    """Represents a well location with spatial and attribute data."""
    api_number: str
    well_name: str
    operator: str
    surface_latitude: float
    surface_longitude: float
    bottom_latitude: Optional[float] = None
    bottom_longitude: Optional[float] = None
    total_depth: Optional[float] = None
    elevation: Optional[float] = None
    status: Optional[str] = None
    completion_date: Optional[str] = None
    formation: Optional[str] = None


@dataclass
class SeismicSurvey:
    """Represents a seismic survey with metadata."""
    survey_name: str
    survey_type: str  # 2D, 3D, 4D
    acquisition_date: str
    line_km: Optional[float] = None
    area_km2: Optional[float] = None
    bin_size: Optional[Tuple[float, float]] = None  # inline, crossline
    frequency_range: Optional[Tuple[float, float]] = None
    processing_status: Optional[str] = None


class ArcGISConnector:
    """
    Connector for ArcGIS Online and Enterprise.
    
    Handles authentication, data upload, map services, and spatial analysis
    for petroleum geoscience applications.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        portal_url: str = "https://www.arcgis.com",
        username: Optional[str] = None,
        password: Optional[str] = None,
        profile: Optional[str] = None
    ):
        """
        Initialize ArcGIS connection.
        
        Args:
            api_key: ArcGIS API key (for app authentication)
            portal_url: ArcGIS Enterprise URL or ArcGIS Online
            username: Named user username
            password: Named user password
            profile: Saved profile name for credential reuse
        """
        self.portal_url = portal_url
        self.api_key = api_key
        self.username = username
        self._gis = None
        
        # Lazy import to avoid dependency issues
        try:
            from arcgis.gis import GIS
            self._GIS = GIS
        except ImportError:
            logger.warning("arcgis package not installed. Running in mock mode.")
            self._GIS = None
        
    def connect(self) -> bool:
        """
        Establish connection to ArcGIS.
        
        Returns:
            True if connection successful, False otherwise
        """
        if self._GIS is None:
            logger.error("ArcGIS API not available. Install with: pip install arcgis")
            return False
        
        try:
            if self.api_key:
                self._gis = self._GIS(self.portal_url, api_key=self.api_key)
            elif self.username:
                self._gis = self._GIS(
                    self.portal_url,
                    username=self.username,
                    password=self.password
                )
            else:
                # Anonymous connection (limited functionality)
                self._gis = self._GIS(self.portal_url)
            
            logger.info(f"Connected to {self.portal_url} as {self._gis.users.me}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            return False
    
    def search_well_data(
        self,
        bounds: Optional[Dict[str, float]] = None,
        operator: Optional[str] = None,
        status: Optional[str] = None,
        formation: Optional[str] = None,
        max_results: int = 1000
    ) -> List[WellLocation]:
        """
        Search for wells within geographic or attribute criteria.
        
        Args:
            bounds: {'xmin': -103.5, 'ymin': 31.2, 'xmax': -103.0, 'ymax': 31.8}
            operator: Filter by operator name
            status: Filter by well status (active, plugged, etc.)
            formation: Filter by producing formation
            max_results: Maximum number of results to return
            
        Returns:
            List of WellLocation objects
        """
        if not self._gis:
            raise ConnectionError("Not connected to ArcGIS. Call connect() first.")
        
        # Build query
        query_parts = []
        
        if bounds:
            extent = f"{bounds['xmin']},{bounds['ymin']},{bounds['xmax']},{bounds['ymax']}"
            query_parts.append(f"geometry={extent}")
        
        where_clauses = []
        if operator:
            where_clauses.append(f"operator = '{operator}'")
        if status:
            where_clauses.append(f"status = '{status}'")
        if formation:
            where_clauses.append(f"formation = '{formation}'")
        
        if where_clauses:
            query_parts.append(" AND ".join(where_clauses))
        
        # Execute search (mock implementation for now)
        logger.info(f"Searching wells with query: {query_parts}")
        
        # Return mock data for demonstration
        return [
            WellLocation(
                api_number="42-001-12345",
                well_name="Test Well 1",
                operator="Example Operator",
                surface_latitude=31.5,
                surface_longitude=-103.2,
                total_depth=8500,
                status="Active"
            )
        ]
    
    def upload_well_survey(
        self,
        wells: List[WellLocation],
        service_name: str = "well_survey",
        folder: Optional[str] = None
    ) -> str:
        """
        Upload well locations as a hosted feature service.
        
        Args:
            wells: List of WellLocation objects
            service_name: Name for the hosted feature service
            folder: ArcGIS Online/Enterprise folder name
            
        Returns:
            URL of the created feature service
        """
        if not self._gis:
            raise ConnectionError("Not connected to ArcGIS")
        
        # Convert wells to GeoJSON format
        features = []
        for well in wells:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [well.surface_longitude, well.surface_latitude]
                },
                "properties": {
                    "api_number": well.api_number,
                    "well_name": well.well_name,
                    "operator": well.operator,
                    "total_depth": well.total_depth,
                    "status": well.status
                }
            }
            features.append(feature)
        
        geojson = {
            "type": "FeatureCollection",
            "features": features
        }
        
        logger.info(f"Uploading {len(wells)} wells to service: {service_name}")
        
        # Return mock URL
        return f"https://services.arcgis.com/.../{service_name}/FeatureServer"
    
    def upload_seismic_survey(
        self,
        survey: SeismicSurvey,
        survey_path: str,
        coordinate_system: str = "EPSG:4326"
    ) -> str:
        """
        Upload seismic survey geometry as a feature service.
        
        Args:
            survey: SeismicSurvey metadata object
            survey_path: Path to survey geometry file (Shapefile, GeoJSON)
            coordinate_system: EPSG code for coordinate reference system
            
        Returns:
            URL of the created feature service
        """
        logger.info(f"Uploading seismic survey: {survey.survey_name}")
        return f"https://services.arcgis.com/.../seismic_{survey.survey_name}"
    
    def generate_structure_map(
        self,
        well_tops: List[Dict],
        horizon_name: str,
        contour_interval: float = 50,
        method: str = "kriging"
    ) -> str:
        """
        Generate structural contour map from well tops.
        
        Args:
            well_tops: List of {'x': lon, 'y': lat, 'z': tvd_ss}
            horizon_name: Name of the mapped horizon
            contour_interval: Contour interval in feet or meters
            method: Interpolation method (kriging, IDW, spline)
            
        Returns:
            URL to the generated map service
        """
        logger.info(f"Generating structure map for {horizon_name}")
        
        # Spatial interpolation would happen here
        # Using ArcGIS Spatial Analyst or GeoAnalytics
        
        return f"https://services.arcgis.com/.../structure_{horizon_name}"
    
    def create_cross_section(
        self,
        line: List[Tuple[float, float]],
        wells: List[str],
        horizons: List[str],
        width: float = 1000,
        vertical_exaggeration: float = 5.0
    ) -> str:
        """
        Create geological cross-section along a defined line.
        
        Args:
            line: List of (longitude, latitude) points defining section line
            wells: List of API numbers for wells to project
            horizons: List of horizon names to display
            width: Swath width for well projection (feet/meters)
            vertical_exaggeration: Vertical exaggeration factor
            
        Returns:
            URL to cross-section image or web map
        """
        logger.info(f"Creating cross-section with {len(wells)} wells")
        return "https://maps.arcgis.com/.../cross_section"
    
    def calculate_areas(
        self,
        polygon_features: str,
        field_name: str = "area_acres"
    ) -> Dict[str, float]:
        """
        Calculate areas for polygon features (closures, leases, etc.).
        
        Args:
            polygon_features: Feature service URL or layer ID
            field_name: Name of field to populate with area values
            
        Returns:
            Dictionary mapping feature IDs to areas
        """
        logger.info(f"Calculating areas for {polygon_features}")
        
        # Mock results
        return {
            "closure_1": 1250.5,
            "closure_2": 890.3,
            "closure_3": 2100.7
        }
    
    def export_to_petrel(
        self,
        feature_service: str,
        output_path: str,
        format: str = "csv"
    ) -> str:
        """
        Export ArcGIS data to Petrel-compatible format.
        
        Args:
            feature_service: Source feature service URL
            output_path: Destination file path
            format: Export format (csv, xyz, segy)
            
        Returns:
            Path to exported file
        """
        logger.info(f"Exporting {feature_service} to {output_path}")
        return output_path
    
    def get_well_symbols(self) -> Dict:
        """
        Get standard well symbol definitions for mapping.
        
        Returns:
            Dictionary of symbol definitions by well type/status
        """
        return {
            "oil_producer": {"color": "#006400", "shape": "circle"},
            "gas_producer": {"color": "#FF0000", "shape": "circle"},
            "water_injector": {"color": "#0000FF", "shape": "triangle"},
            "gas_injector": {"color": "#FFA500", "shape": "triangle"},
            "observation": {"color": "#808080", "shape": "square"},
            "plugged": {"color": "#000000", "shape": "x"}
        }


# Example usage
if __name__ == "__main__":
    # Initialize connector
    connector = ArcGISConnector(
        api_key="your_api_key_here",
        portal_url="https://www.arcgis.com"
    )
    
    # Connect
    if connector.connect():
        print("Connected successfully")
        
        # Search wells
        wells = connector.search_well_data(
            bounds={"xmin": -103.5, "ymin": 31.2, "xmax": -103.0, "ymax": 31.8}
        )
        print(f"Found {len(wells)} wells")
        
        # Upload wells
        service_url = connector.upload_well_survey(wells, "permian_wells")
        print(f"Uploaded to: {service_url}")
    else:
        print("Connection failed")