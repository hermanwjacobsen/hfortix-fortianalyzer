"""
FortiAnalyzer API endpoint: cli.global.system.snmp.sysinfo

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSnmpSysinfo:
    """
    FortiAnalyzer endpoint: cli.global.system.snmp.sysinfo
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/snmp/sysinfo"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        fortianalyzer_legacy_sysoid: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_cpu_high_exclude_nice_threshold: int | None = None,
        trap_high_cpu_threshold: int | None = None,
        trap_low_memory_threshold: int | None = None,
        contact_info: str | None = None,
        description: str | None = None,
        engine_id: str | None = None,
        location: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            contact_info: contact_info parameter
            description: description parameter
            engine_id: engine-id parameter
            fortianalyzer_legacy_sysoid: fortianalyzer-legacy-sysoid parameter
            location: location parameter
            status: status parameter
            trap_cpu_high_exclude_nice_threshold: trap-cpu-high-exclude-nice-threshold parameter
            trap_high_cpu_threshold: trap-high-cpu-threshold parameter
            trap_low_memory_threshold: trap-low-memory-threshold parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/snmp/sysinfo"
        
        # Build data payload
        data = {}
        if contact_info is not None:
            data["contact_info"] = contact_info
        if description is not None:
            data["description"] = description
        if engine_id is not None:
            data["engine-id"] = engine_id
        if fortianalyzer_legacy_sysoid is not None:
            data["fortianalyzer-legacy-sysoid"] = fortianalyzer_legacy_sysoid
        if location is not None:
            data["location"] = location
        if status is not None:
            data["status"] = status
        if trap_cpu_high_exclude_nice_threshold is not None:
            data["trap-cpu-high-exclude-nice-threshold"] = trap_cpu_high_exclude_nice_threshold
        if trap_high_cpu_threshold is not None:
            data["trap-high-cpu-threshold"] = trap_high_cpu_threshold
        if trap_low_memory_threshold is not None:
            data["trap-low-memory-threshold"] = trap_low_memory_threshold
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def update(
        self,
        fortianalyzer_legacy_sysoid: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trap_cpu_high_exclude_nice_threshold: int | None = None,
        trap_high_cpu_threshold: int | None = None,
        trap_low_memory_threshold: int | None = None,
        contact_info: str | None = None,
        description: str | None = None,
        engine_id: str | None = None,
        location: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            contact_info: contact_info parameter
            description: description parameter
            engine_id: engine-id parameter
            fortianalyzer_legacy_sysoid: fortianalyzer-legacy-sysoid parameter
            location: location parameter
            status: status parameter
            trap_cpu_high_exclude_nice_threshold: trap-cpu-high-exclude-nice-threshold parameter
            trap_high_cpu_threshold: trap-high-cpu-threshold parameter
            trap_low_memory_threshold: trap-low-memory-threshold parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/snmp/sysinfo"
        
        # Build data payload
        data = {}
        if contact_info is not None:
            data["contact_info"] = contact_info
        if description is not None:
            data["description"] = description
        if engine_id is not None:
            data["engine-id"] = engine_id
        if fortianalyzer_legacy_sysoid is not None:
            data["fortianalyzer-legacy-sysoid"] = fortianalyzer_legacy_sysoid
        if location is not None:
            data["location"] = location
        if status is not None:
            data["status"] = status
        if trap_cpu_high_exclude_nice_threshold is not None:
            data["trap-cpu-high-exclude-nice-threshold"] = trap_cpu_high_exclude_nice_threshold
        if trap_high_cpu_threshold is not None:
            data["trap-high-cpu-threshold"] = trap_high_cpu_threshold
        if trap_low_memory_threshold is not None:
            data["trap-low-memory-threshold"] = trap_low_memory_threshold
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)
