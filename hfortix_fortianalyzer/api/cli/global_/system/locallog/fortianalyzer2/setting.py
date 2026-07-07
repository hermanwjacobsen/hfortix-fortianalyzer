"""
FortiAnalyzer API endpoint: cli.global.system.locallog.fortianalyzer2.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogFortianalyzer2Setting:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.fortianalyzer2.setting
    
    
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
        url = "/cli/global/system/locallog/fortianalyzer2/setting"
        
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
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["enable"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "realtime", "upload"] | None = None,
        peer_cert_cn: str | None = None,
        server: str | None = None,
        upload_time: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            peer_cert_cn: peer-cert-cn parameter
            reliable: reliable parameter
            secure_connection: secure-connection parameter
            server: server parameter
            severity: severity parameter
            status: status parameter
            upload_time: upload-time parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/fortianalyzer2/setting"
        
        # Build data payload
        data = {}
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if reliable is not None:
            data["reliable"] = reliable
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if server is not None:
            data["server"] = server
        if severity is not None:
            data["severity"] = severity
        if status is not None:
            data["status"] = status
        if upload_time is not None:
            data["upload-time"] = upload_time
        
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
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["enable"] | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "realtime", "upload"] | None = None,
        peer_cert_cn: str | None = None,
        server: str | None = None,
        upload_time: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            peer_cert_cn: peer-cert-cn parameter
            reliable: reliable parameter
            secure_connection: secure-connection parameter
            server: server parameter
            severity: severity parameter
            status: status parameter
            upload_time: upload-time parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/fortianalyzer2/setting"
        
        # Build data payload
        data = {}
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if reliable is not None:
            data["reliable"] = reliable
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if server is not None:
            data["server"] = server
        if severity is not None:
            data["severity"] = severity
        if status is not None:
            data["status"] = status
        if upload_time is not None:
            data["upload-time"] = upload_time
        
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
