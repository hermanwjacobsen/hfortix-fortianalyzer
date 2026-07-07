"""
FortiAnalyzer API endpoint: cli.global.system.central-management

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCentralManagement:
    """
    FortiAnalyzer endpoint: cli.global.system.central-management
    
    
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
        url = "/cli/global/system/central-management"
        
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
        allow_monitor: Literal["disable", "enable"] | None = None,
        authorized_manager_only: Literal["disable", "enable"] | None = None,
        elite_service: Literal["disable", "enable"] | None = None,
        enc_algorithm: Literal["default", "low", "high"] | None = None,
        socaas_remote_access: Literal["disable", "enable"] | None = None,
        type: Literal["fortimanager", "cloud-management", "none"] | None = None,
        acctid: str | None = None,
        fmg: str | None = None,
        mgmtid: str | None = None,
        serial_number: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            acctid: acctid parameter
            allow_monitor: allow-monitor parameter
            authorized_manager_only: authorized-manager-only parameter
            elite_service: elite-service parameter
            enc_algorithm: enc-algorithm parameter
            fmg: fmg parameter
            mgmtid: mgmtid parameter
            serial_number: serial-number parameter
            socaas_remote_access: socaas-remote-access parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/central-management"
        
        # Build data payload
        data = {}
        if acctid is not None:
            data["acctid"] = acctid
        if allow_monitor is not None:
            data["allow-monitor"] = allow_monitor
        if authorized_manager_only is not None:
            data["authorized-manager-only"] = authorized_manager_only
        if elite_service is not None:
            data["elite-service"] = elite_service
        if enc_algorithm is not None:
            data["enc-algorithm"] = enc_algorithm
        if fmg is not None:
            data["fmg"] = fmg
        if mgmtid is not None:
            data["mgmtid"] = mgmtid
        if serial_number is not None:
            data["serial-number"] = serial_number
        if socaas_remote_access is not None:
            data["socaas-remote-access"] = socaas_remote_access
        if type is not None:
            data["type"] = type
        
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
        allow_monitor: Literal["disable", "enable"] | None = None,
        authorized_manager_only: Literal["disable", "enable"] | None = None,
        elite_service: Literal["disable", "enable"] | None = None,
        enc_algorithm: Literal["default", "low", "high"] | None = None,
        socaas_remote_access: Literal["disable", "enable"] | None = None,
        type: Literal["fortimanager", "cloud-management", "none"] | None = None,
        acctid: str | None = None,
        fmg: str | None = None,
        mgmtid: str | None = None,
        serial_number: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            acctid: acctid parameter
            allow_monitor: allow-monitor parameter
            authorized_manager_only: authorized-manager-only parameter
            elite_service: elite-service parameter
            enc_algorithm: enc-algorithm parameter
            fmg: fmg parameter
            mgmtid: mgmtid parameter
            serial_number: serial-number parameter
            socaas_remote_access: socaas-remote-access parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/central-management"
        
        # Build data payload
        data = {}
        if acctid is not None:
            data["acctid"] = acctid
        if allow_monitor is not None:
            data["allow-monitor"] = allow_monitor
        if authorized_manager_only is not None:
            data["authorized-manager-only"] = authorized_manager_only
        if elite_service is not None:
            data["elite-service"] = elite_service
        if enc_algorithm is not None:
            data["enc-algorithm"] = enc_algorithm
        if fmg is not None:
            data["fmg"] = fmg
        if mgmtid is not None:
            data["mgmtid"] = mgmtid
        if serial_number is not None:
            data["serial-number"] = serial_number
        if socaas_remote_access is not None:
            data["socaas-remote-access"] = socaas_remote_access
        if type is not None:
            data["type"] = type
        
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
