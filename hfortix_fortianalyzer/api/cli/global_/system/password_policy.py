"""
FortiAnalyzer API endpoint: cli.global.system.password-policy

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemPasswordPolicy:
    """
    FortiAnalyzer endpoint: cli.global.system.password-policy
    
    
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
        url = "/cli/global/system/password-policy"
        
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
        change_4_characters: Literal["disable", "enable"] | None = None,
        expire: int | None = None,
        login_lockout_upon_downgrade: Literal["disable", "enable"] | None = None,
        minimum_length: int | None = None,
        password_history: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        must_contain: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            change_4_characters: change-4-characters parameter
            expire: expire parameter
            login_lockout_upon_downgrade: login-lockout-upon-downgrade parameter
            minimum_length: minimum-length parameter
            must_contain: must-contain parameter
            password_history: password-history parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/password-policy"
        
        # Build data payload
        data = {}
        if change_4_characters is not None:
            data["change-4-characters"] = change_4_characters
        if expire is not None:
            data["expire"] = expire
        if login_lockout_upon_downgrade is not None:
            data["login-lockout-upon-downgrade"] = login_lockout_upon_downgrade
        if minimum_length is not None:
            data["minimum-length"] = minimum_length
        if must_contain is not None:
            data["must-contain"] = must_contain
        if password_history is not None:
            data["password-history"] = password_history
        if status is not None:
            data["status"] = status
        
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
        change_4_characters: Literal["disable", "enable"] | None = None,
        expire: int | None = None,
        login_lockout_upon_downgrade: Literal["disable", "enable"] | None = None,
        minimum_length: int | None = None,
        password_history: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        must_contain: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            change_4_characters: change-4-characters parameter
            expire: expire parameter
            login_lockout_upon_downgrade: login-lockout-upon-downgrade parameter
            minimum_length: minimum-length parameter
            must_contain: must-contain parameter
            password_history: password-history parameter
            status: status parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/password-policy"
        
        # Build data payload
        data = {}
        if change_4_characters is not None:
            data["change-4-characters"] = change_4_characters
        if expire is not None:
            data["expire"] = expire
        if login_lockout_upon_downgrade is not None:
            data["login-lockout-upon-downgrade"] = login_lockout_upon_downgrade
        if minimum_length is not None:
            data["minimum-length"] = minimum_length
        if must_contain is not None:
            data["must-contain"] = must_contain
        if password_history is not None:
            data["password-history"] = password_history
        if status is not None:
            data["status"] = status
        
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
