"""
FortiAnalyzer API endpoint: cli.global.system.log-fetch.server-settings

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogFetchServerSettings:
    """
    FortiAnalyzer endpoint: cli.global.system.log-fetch.server-settings
    
    
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
        url = "/cli/global/system/log-fetch/server-settings"
        
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
        max_conn_per_session: int | None = None,
        max_sessions: int | None = None,
        session_timeout: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            max_conn_per_session: max-conn-per-session parameter
            max_sessions: max-sessions parameter
            session_timeout: session-timeout parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-fetch/server-settings"
        
        # Build data payload
        data = {}
        if max_conn_per_session is not None:
            data["max-conn-per-session"] = max_conn_per_session
        if max_sessions is not None:
            data["max-sessions"] = max_sessions
        if session_timeout is not None:
            data["session-timeout"] = session_timeout
        
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
        max_conn_per_session: int | None = None,
        max_sessions: int | None = None,
        session_timeout: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            max_conn_per_session: max-conn-per-session parameter
            max_sessions: max-sessions parameter
            session_timeout: session-timeout parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-fetch/server-settings"
        
        # Build data payload
        data = {}
        if max_conn_per_session is not None:
            data["max-conn-per-session"] = max_conn_per_session
        if max_sessions is not None:
            data["max-sessions"] = max_sessions
        if session_timeout is not None:
            data["session-timeout"] = session_timeout
        
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
