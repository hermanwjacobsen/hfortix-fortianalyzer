"""
FortiAnalyzer API endpoint: cli.global.system.connector

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemConnector:
    """
    FortiAnalyzer endpoint: cli.global.system.connector
    
    
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
        url = "/cli/global/system/connector"
        
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
        cloud_orchest_refresh_interval: int | None = None,
        conn_refresh_interval: int | None = None,
        conn_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        faznotify_msg_queue_max: int | None = None,
        faznotify_msg_timeout: int | None = None,
        fsso_refresh_interval: int | None = None,
        fsso_sess_timeout: int | None = None,
        px_svr_timeout: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            cloud_orchest_refresh_interval: cloud-orchest-refresh-interval parameter
            conn_refresh_interval: conn-refresh-interval parameter
            conn_ssl_protocol: conn-ssl-protocol parameter
            faznotify_msg_queue_max: faznotify-msg-queue-max parameter
            faznotify_msg_timeout: faznotify-msg-timeout parameter
            fsso_refresh_interval: fsso-refresh-interval parameter
            fsso_sess_timeout: fsso-sess-timeout parameter
            px_svr_timeout: px-svr-timeout parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/connector"
        
        # Build data payload
        data = {}
        if cloud_orchest_refresh_interval is not None:
            data["cloud-orchest-refresh-interval"] = cloud_orchest_refresh_interval
        if conn_refresh_interval is not None:
            data["conn-refresh-interval"] = conn_refresh_interval
        if conn_ssl_protocol is not None:
            data["conn-ssl-protocol"] = conn_ssl_protocol
        if faznotify_msg_queue_max is not None:
            data["faznotify-msg-queue-max"] = faznotify_msg_queue_max
        if faznotify_msg_timeout is not None:
            data["faznotify-msg-timeout"] = faznotify_msg_timeout
        if fsso_refresh_interval is not None:
            data["fsso-refresh-interval"] = fsso_refresh_interval
        if fsso_sess_timeout is not None:
            data["fsso-sess-timeout"] = fsso_sess_timeout
        if px_svr_timeout is not None:
            data["px-svr-timeout"] = px_svr_timeout
        
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
        cloud_orchest_refresh_interval: int | None = None,
        conn_refresh_interval: int | None = None,
        conn_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        faznotify_msg_queue_max: int | None = None,
        faznotify_msg_timeout: int | None = None,
        fsso_refresh_interval: int | None = None,
        fsso_sess_timeout: int | None = None,
        px_svr_timeout: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            cloud_orchest_refresh_interval: cloud-orchest-refresh-interval parameter
            conn_refresh_interval: conn-refresh-interval parameter
            conn_ssl_protocol: conn-ssl-protocol parameter
            faznotify_msg_queue_max: faznotify-msg-queue-max parameter
            faznotify_msg_timeout: faznotify-msg-timeout parameter
            fsso_refresh_interval: fsso-refresh-interval parameter
            fsso_sess_timeout: fsso-sess-timeout parameter
            px_svr_timeout: px-svr-timeout parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/connector"
        
        # Build data payload
        data = {}
        if cloud_orchest_refresh_interval is not None:
            data["cloud-orchest-refresh-interval"] = cloud_orchest_refresh_interval
        if conn_refresh_interval is not None:
            data["conn-refresh-interval"] = conn_refresh_interval
        if conn_ssl_protocol is not None:
            data["conn-ssl-protocol"] = conn_ssl_protocol
        if faznotify_msg_queue_max is not None:
            data["faznotify-msg-queue-max"] = faznotify_msg_queue_max
        if faznotify_msg_timeout is not None:
            data["faznotify-msg-timeout"] = faznotify_msg_timeout
        if fsso_refresh_interval is not None:
            data["fsso-refresh-interval"] = fsso_refresh_interval
        if fsso_sess_timeout is not None:
            data["fsso-sess-timeout"] = fsso_sess_timeout
        if px_svr_timeout is not None:
            data["px-svr-timeout"] = px_svr_timeout
        
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
