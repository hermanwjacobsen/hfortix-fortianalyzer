"""
FortiAnalyzer API endpoint: cli.global.system.alertemail

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertemail:
    """
    FortiAnalyzer endpoint: cli.global.system.alertemail
    
    
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
        url = "/cli/global/system/alertemail"
        
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
        authentication: Literal["disable", "enable"] | None = None,
        smtpport: int | None = None,
        fromaddress: str | None = None,
        fromname: str | None = None,
        smtppassword: list[Any] | None = None,
        smtpserver: str | None = None,
        smtpuser: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            authentication: authentication parameter
            fromaddress: fromaddress parameter
            fromname: fromname parameter
            smtppassword: smtppassword parameter
            smtpport: smtpport parameter
            smtpserver: smtpserver parameter
            smtpuser: smtpuser parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/alertemail"
        
        # Build data payload
        data = {}
        if authentication is not None:
            data["authentication"] = authentication
        if fromaddress is not None:
            data["fromaddress"] = fromaddress
        if fromname is not None:
            data["fromname"] = fromname
        if smtppassword is not None:
            data["smtppassword"] = smtppassword
        if smtpport is not None:
            data["smtpport"] = smtpport
        if smtpserver is not None:
            data["smtpserver"] = smtpserver
        if smtpuser is not None:
            data["smtpuser"] = smtpuser
        
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
        authentication: Literal["disable", "enable"] | None = None,
        smtpport: int | None = None,
        fromaddress: str | None = None,
        fromname: str | None = None,
        smtppassword: list[Any] | None = None,
        smtpserver: str | None = None,
        smtpuser: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            authentication: authentication parameter
            fromaddress: fromaddress parameter
            fromname: fromname parameter
            smtppassword: smtppassword parameter
            smtpport: smtpport parameter
            smtpserver: smtpserver parameter
            smtpuser: smtpuser parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/alertemail"
        
        # Build data payload
        data = {}
        if authentication is not None:
            data["authentication"] = authentication
        if fromaddress is not None:
            data["fromaddress"] = fromaddress
        if fromname is not None:
            data["fromname"] = fromname
        if smtppassword is not None:
            data["smtppassword"] = smtppassword
        if smtpport is not None:
            data["smtpport"] = smtpport
        if smtpserver is not None:
            data["smtpserver"] = smtpserver
        if smtpuser is not None:
            data["smtpuser"] = smtpuser
        
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
