"""
SCADA Connector for Real-Time Operations

Provides integration with refinery and production SCADA systems for:
- Real-time tag monitoring and subscription
- Historical data retrieval
- Alarm management
- Control system integration
- Trend analysis

Requirements:
    - OPC UA or OPC Classic connectivity
    - SCADA system API access (OSIsoft PI, Wonderware, etc.)
    - Network access to SCADA historians
    - Valid credentials and permissions
"""

import logging
from typing import Dict, List, Optional, Union, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TagType(Enum):
    """SCADA tag data types."""
    ANALOG = "analog"
    DIGITAL = "digital"
    STRING = "string"
    INTEGER = "integer"


@dataclass
class TagValue:
    """Represents a SCADA tag value with timestamp."""
    tag_name: str
    value: Union[float, int, str, bool]
    timestamp: datetime
    quality: str  # GOOD, BAD, UNCERTAIN
    units: Optional[str] = None


@dataclass
class Alarm:
    """Represents a SCADA alarm event."""
    alarm_id: str
    tag_name: str
    description: str
    priority: int  # 1=Critical, 2=High, 3=Medium, 4=Low
    state: str  # ACTIVE, ACKNOWLEDGED, CLEARED
    timestamp_active: datetime
    timestamp_ack: Optional[datetime] = None
    timestamp_clear: Optional[datetime] = None
    operator_comment: Optional[str] = None


@dataclass
class TrendData:
    """Represents time-series trend data."""
    tag_name: str
    timestamps: List[datetime]
    values: List[Union[float, int]]
    aggregation: str  # RAW, AVERAGE, MINIMUM, MAXIMUM
    interval: timedelta


class SCADAConnector:
    """
    Generic SCADA connector supporting multiple protocols and systems.
    
    Supports:
    - OPC UA (Unified Architecture)
    - OPC DA (Data Access)
    - OSIsoft PI System
    - Wonderware System Platform
    - Ignition
    - Custom REST APIs
    """
    
    def __init__(
        self,
        system_type: str = "generic",
        host: str = "localhost",
        port: int = 4840,
        protocol: str = "opc_ua",
        username: Optional[str] = None,
        password: Optional[str] = None,
        use_tls: bool = True
    ):
        """
        Initialize SCADA connection.
        
        Args:
            system_type: SCADA system type (pi, wonderware, ignition, generic)
            host: SCADA server hostname or IP
            port: Connection port
            protocol: Communication protocol (opc_ua, opc_da, rest, pi_sdk)
            username: Authentication username
            password: Authentication password
            use_tls: Use TLS/SSL encryption
        """
        self.system_type = system_type
        self.host = host
        self.port = port
        self.protocol = protocol
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self._connection = None
        self._subscriptions = {}
        self._callbacks = {}
        
        logger.info(f"Initialized SCADA connector: {system_type} at {host}:{port}")
    
    def connect(self) -> bool:
        """
        Establish connection to SCADA system.
        
        Returns:
            True if connection successful
        """
        try:
            if self.protocol == "opc_ua":
                return self._connect_opcua()
            elif self.protocol == "rest":
                return self._connect_rest()
            else:
                # Mock connection for demonstration
                logger.info(f"Mock connection to {self.system_type}")
                self._connection = {"status": "connected", "mock": True}
                return True
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            return False
    
    def _connect_opcua(self) -> bool:
        """Connect using OPC UA protocol."""
        try:
            from opcua import Client
            
            url = f"opc.tcp://{self.host}:{self.port}"
            self._connection = Client(url)
            
            if self.username and self.password:
                self._connection.set_user(self.username)
                self._connection.set_password(self.password)
            
            self._connection.connect()
            logger.info(f"OPC UA connected to {url}")
            return True
            
        except ImportError:
            logger.warning("opcua library not installed, using mock mode")
            self._connection = {"status": "connected", "mock": True, "protocol": "opc_ua"}
            return True
    
    def _connect_rest(self) -> bool:
        """Connect using REST API."""
        import requests
        
        base_url = f"{'https' if self.use_tls else 'http'}://{self.host}:{self.port}/api"
        self._connection = {"base_url": base_url, "session": requests.Session()}
        
        if self.username and self.password:
            self._connection["session"].auth = (self.username, self.password)
        
        logger.info(f"REST API configured: {base_url}")
        return True
    
    def read_tag(self, tag_name: str) -> TagValue:
        """
        Read current value from SCADA tag.
        
        Args:
            tag_name: Fully qualified tag name
            
        Returns:
            TagValue with current data
        """
        if not self._connection:
            raise ConnectionError("Not connected to SCADA")
        
        # Mock implementation
        logger.debug(f"Reading tag: {tag_name}")
        
        return TagValue(
            tag_name=tag_name,
            value=125.5,
            timestamp=datetime.now(),
            quality="GOOD",
            units="PSI"
        )
    
    def read_multiple_tags(self, tag_names: List[str]) -> Dict[str, TagValue]:
        """
        Read multiple tags in single operation.
        
        Args:
            tag_names: List of tag names
            
        Returns:
            Dictionary mapping tag names to TagValues
        """
        results = {}
        for tag in tag_names:
            results[tag] = self.read_tag(tag)
        return results
    
    def write_tag(self, tag_name: str, value: Union[float, int, str, bool]) -> bool:
        """
        Write value to SCADA tag (if permitted).
        
        Args:
            tag_name: Tag to write
            value: New value
            
        Returns:
            True if write successful
        """
        if not self._connection:
            raise ConnectionError("Not connected to SCADA")
        
        logger.info(f"Writing {value} to {tag_name}")
        return True
    
    def subscribe_tag(
        self,
        tag_name: str,
        callback: Callable[[TagValue], None],
        update_rate_ms: int = 1000
    ) -> str:
        """
        Subscribe to tag value changes.
        
        Args:
            tag_name: Tag to monitor
            callback: Function to call on value change
            update_rate_ms: Polling interval in milliseconds
            
        Returns:
            Subscription ID
        """
        import uuid
        sub_id = str(uuid.uuid4())
        
        self._subscriptions[sub_id] = {
            "tag": tag_name,
            "callback": callback,
            "rate": update_rate_ms
        }
        
        logger.info(f"Subscribed to {tag_name} (ID: {sub_id})")
        return sub_id
    
    def unsubscribe(self, subscription_id: str) -> bool:
        """Cancel tag subscription."""
        if subscription_id in self._subscriptions:
            del self._subscriptions[subscription_id]
            logger.info(f"Unsubscribed: {subscription_id}")
            return True
        return False
    
    def get_historical_data(
        self,
        tag_name: str,
        start_time: datetime,
        end_time: datetime,
        interval: Optional[timedelta] = None,
        aggregation: str = "AVERAGE"
    ) -> TrendData:
        """
        Retrieve historical trend data.
        
        Args:
            tag_name: Tag to query
            start_time: Query start
            end_time: Query end
            interval: Sampling interval (None = raw data)
            aggregation: AVERAGE, MINIMUM, MAXIMUM, RAW
            
        Returns:
            TrendData with time series
        """
        if not self._connection:
            raise ConnectionError("Not connected to SCADA")
        
        logger.info(f"Querying history: {tag_name} from {start_time} to {end_time}")
        
        # Generate mock trend data
        interval = interval or timedelta(minutes=1)
        timestamps = []
        values = []
        
        current = start_time
        while current <= end_time:
            timestamps.append(current)
            values.append(100.0 + (current.hour * 2))  # Mock data
            current += interval
        
        return TrendData(
            tag_name=tag_name,
            timestamps=timestamps,
            values=values,
            aggregation=aggregation,
            interval=interval
        )
    
    def get_alarms(
        self,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        priorities: Optional[List[int]] = None,
        states: Optional[List[str]] = None
    ) -> List[Alarm]:
        """
        Retrieve alarm history or active alarms.
        
        Args:
            start_time: Query start (None = all history)
            end_time: Query end (None = now)
            priorities: Filter by priority levels
            states: Filter by alarm states
            
        Returns:
            List of Alarm objects
        """
        if not self._connection:
            raise ConnectionError("Not connected to SCADA")
        
        # Mock alarms
        alarms = [
            Alarm(
                alarm_id="ALM001",
                tag_name="PT-101",
                description="High Pressure",
                priority=2,
                state="ACTIVE",
                timestamp_active=datetime.now() - timedelta(hours=2)
            ),
            Alarm(
                alarm_id="ALM002",
                tag_name="TT-205",
                description="Low Temperature",
                priority=3,
                state="ACKNOWLEDGED",
                timestamp_active=datetime.now() - timedelta(hours=4),
                timestamp_ack=datetime.now() - timedelta(hours=3)
            )
        ]
        
        return alarms
    
    def acknowledge_alarm(self, alarm_id: str, comment: Optional[str] = None) -> bool:
        """
        Acknowledge active alarm.
        
        Args:
            alarm_id: Alarm to acknowledge
            comment: Optional operator comment
            
        Returns:
            True if successful
        """
        logger.info(f"Acknowledging alarm {alarm_id}: {comment}")
        return True
    
    def get_tag_list(
        self,
        filter_pattern: Optional[str] = None,
        tag_type: Optional[TagType] = None
    ) -> List[Dict[str, str]]:
        """
        Browse available tags in SCADA system.
        
        Args:
            filter_pattern: Wildcard filter (e.g., "Unit1.*")
            tag_type: Filter by tag type
            
        Returns:
            List of tag information dictionaries
        """
        # Mock tag list
        tags = [
            {"name": "Unit1.PT-101", "type": "ANALOG", "description": "Reactor Pressure"},
            {"name": "Unit1.TT-101", "type": "ANALOG", "description": "Reactor Temperature"},
            {"name": "Unit1.FT-101", "type": "ANALOG", "description": "Feed Flow"},
            {"name": "Unit1.Pump-101.Status", "type": "DIGITAL", "description": "Pump Running"},
            {"name": "Unit1.Pump-101.Alarm", "type": "DIGITAL", "description": "Pump Fault"}
        ]
        
        if filter_pattern:
            tags = [t for t in tags if filter_pattern.replace("*", "") in t["name"]]
        
        return tags
    
    def export_trend_data(
        self,
        tag_names: List[str],
        start_time: datetime,
        end_time: datetime,
        output_file: str,
        format: str = "csv"
    ) -> str:
        """
        Export trend data to file.
        
        Args:
            tag_names: Tags to export
            start_time: Start time
            end_time: End time
            output_file: Output file path
            format: csv, json, excel
            
        Returns:
            Path to exported file
        """
        logger.info(f"Exporting trend data to {output_file}")
        
        # Mock export
        with open(output_file, 'w') as f:
            f.write("Timestamp,Tag,Value,Quality\n")
            for tag in tag_names:
                f.write(f"{datetime.now()},{tag},100.0,GOOD\n")
        
        return output_file
    
    def close(self):
        """Close SCADA connection."""
        if self._connection:
            if hasattr(self._connection, 'disconnect'):
                self._connection.disconnect()
            self._connection = None
        logger.info("SCADA connection closed")


# Example usage
if __name__ == "__main__":
    # Initialize connector
    scada = SCADAConnector(
        system_type="pi",
        host="pi-server.company.com",
        port=443,
        protocol="rest",
        username="openclaw",
        password="secure_password"
    )
    
    # Connect
    if scada.connect():
        print("Connected to SCADA")
        
        # Read current values
        pressure = scada.read_tag("Unit1.PT-101")
        print(f"Reactor Pressure: {pressure.value} {pressure.units}")
        
        # Get historical data
        trend = scada.get_historical_data(
            tag_name="Unit1.TT-101",
            start_time=datetime.now() - timedelta(days=1),
            end_time=datetime.now(),
            interval=timedelta(hours=1)
        )
        print(f"Retrieved {len(trend.values)} data points")
        
        # Get active alarms
        alarms = scada.get_alarms(states=["ACTIVE"])
        print(f"Active alarms: {len(alarms)}")
        
        # Close connection
        scada.close()
    else:
        print("Failed to connect")