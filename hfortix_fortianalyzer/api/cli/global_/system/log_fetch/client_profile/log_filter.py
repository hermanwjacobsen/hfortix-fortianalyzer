"""
FortiAnalyzer API endpoint: cli.global.system.log-fetch.client-profile.log-filter

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogFetchClientProfileLogFilter:
    """
    FortiAnalyzer endpoint: cli.global.system.log-fetch.client-profile.log-filter
    
    
    Available methods: get, add, set, update, delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        client_profile: str,
        log_filter: int | str | None = None,
        fields: list[Literal["field", "id", "oper", "value"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            client_profile: client-profile parameter
            log_filter: log-filter parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None and log_filter is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log-filter}"
            url = url.replace("{client-profile}", client_profile)
            url = url.replace("{log-filter}", str(log_filter))
        else:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter"
            url = url.replace("{client-profile}", client_profile)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if option is not None:
            request_params["option"] = option
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            **request_params
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def add(
        self,
        client_profile: str,
        log_filter: int | str | None = None,
        id: int | None = None,
        oper: Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None = None,
        field: str | None = None,
        value: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            client_profile: client-profile parameter
            log_filter: log-filter parameter
            field: field parameter
            id: id parameter
            oper: oper parameter
            value: value parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter"
        url = url.replace("{client-profile}", client_profile)
        
        # Build data payload
        data = {}
        if field is not None:
            data["field"] = field
        if id is not None:
            data["id"] = id
        if oper is not None:
            data["oper"] = oper
        if value is not None:
            data["value"] = value
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        client_profile: str,
        log_filter: int | str | None = None,
        id: int | None = None,
        oper: Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None = None,
        field: str | None = None,
        value: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            client_profile: client-profile parameter
            log_filter: log-filter parameter
            field: field parameter
            id: id parameter
            oper: oper parameter
            value: value parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None and log_filter is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log-filter}"
            url = url.replace("{client-profile}", client_profile)
            url = url.replace("{log-filter}", str(log_filter))
        else:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter"
            url = url.replace("{client-profile}", client_profile)
        
        # Build data payload
        data = {}
        if field is not None:
            data["field"] = field
        if id is not None:
            data["id"] = id
        if oper is not None:
            data["oper"] = oper
        if value is not None:
            data["value"] = value
        
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
        client_profile: str,
        log_filter: int | str | None = None,
        id: int | None = None,
        oper: Literal["=", "!=", "<", ">", "<=", ">=", "contain", "not-contain", "match"] | None = None,
        field: str | None = None,
        value: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            client_profile: client-profile parameter
            log_filter: log-filter parameter
            field: field parameter
            id: id parameter
            oper: oper parameter
            value: value parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None and log_filter is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log-filter}"
            url = url.replace("{client-profile}", client_profile)
            url = url.replace("{log-filter}", str(log_filter))
        else:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter"
            url = url.replace("{client-profile}", client_profile)
        
        # Build data payload
        data = {}
        if field is not None:
            data["field"] = field
        if id is not None:
            data["id"] = id
        if oper is not None:
            data["oper"] = oper
        if value is not None:
            data["value"] = value
        
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

    def delete(self, client_profile: str, log_filter: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            client_profile: client-profile parameter
            log_filter: log-filter parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None and log_filter is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log-filter}"
            url = url.replace("{client-profile}", client_profile)
            url = url.replace("{log-filter}", str(log_filter))
        else:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter"
            url = url.replace("{client-profile}", client_profile)
        
        data = {}
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)
