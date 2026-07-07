"""
FortiAnalyzer API endpoint: cli.global.system.sql.custom-skipidx

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSqlCustomSkipidx:
    """
    FortiAnalyzer endpoint: cli.global.system.sql.custom-skipidx
    
    
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
        custom_skipidx: int | str | None = None,
        fields: list[Literal["device-type", "id", "index-field", "log-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            custom_skipidx: custom-skipidx parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if custom_skipidx is not None:
            url = "/cli/global/system/sql/custom-skipidx/{custom-skipidx}"
            url = url.replace("{custom-skipidx}", str(custom_skipidx))
        else:
            url = "/cli/global/system/sql/custom-skipidx"
        
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
        custom_skipidx: int | str | None = None,
        device_type: Literal["FortiGate", "FortiManager", "FortiClient", "FortiMail", "FortiWeb", "FortiSandbox", "FortiProxy"] | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None = None,
        index_field: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            custom_skipidx: custom-skipidx parameter
            device_type: device-type parameter
            id: id parameter
            index_field: index-field parameter
            log_type: log-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/sql/custom-skipidx"
        
        # Build data payload
        data = {}
        if device_type is not None:
            data["device-type"] = device_type
        if id is not None:
            data["id"] = id
        if index_field is not None:
            data["index-field"] = index_field
        if log_type is not None:
            data["log-type"] = log_type
        
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
        custom_skipidx: int | str | None = None,
        device_type: Literal["FortiGate", "FortiManager", "FortiClient", "FortiMail", "FortiWeb", "FortiSandbox", "FortiProxy"] | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None = None,
        index_field: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            custom_skipidx: custom-skipidx parameter
            device_type: device-type parameter
            id: id parameter
            index_field: index-field parameter
            log_type: log-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if custom_skipidx is not None:
            url = "/cli/global/system/sql/custom-skipidx/{custom-skipidx}"
            url = url.replace("{custom-skipidx}", str(custom_skipidx))
        else:
            url = "/cli/global/system/sql/custom-skipidx"
        
        # Build data payload
        data = {}
        if device_type is not None:
            data["device-type"] = device_type
        if id is not None:
            data["id"] = id
        if index_field is not None:
            data["index-field"] = index_field
        if log_type is not None:
            data["log-type"] = log_type
        
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
        custom_skipidx: int | str | None = None,
        device_type: Literal["FortiGate", "FortiManager", "FortiClient", "FortiMail", "FortiWeb", "FortiSandbox", "FortiProxy"] | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "asset", "protocol", "siem", "ztna", "security"] | None = None,
        index_field: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            custom_skipidx: custom-skipidx parameter
            device_type: device-type parameter
            id: id parameter
            index_field: index-field parameter
            log_type: log-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if custom_skipidx is not None:
            url = "/cli/global/system/sql/custom-skipidx/{custom-skipidx}"
            url = url.replace("{custom-skipidx}", str(custom_skipidx))
        else:
            url = "/cli/global/system/sql/custom-skipidx"
        
        # Build data payload
        data = {}
        if device_type is not None:
            data["device-type"] = device_type
        if id is not None:
            data["id"] = id
        if index_field is not None:
            data["index-field"] = index_field
        if log_type is not None:
            data["log-type"] = log_type
        
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

    def delete(self, custom_skipidx: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            custom_skipidx: custom-skipidx parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if custom_skipidx is not None:
            url = "/cli/global/system/sql/custom-skipidx/{custom-skipidx}"
            url = url.replace("{custom-skipidx}", str(custom_skipidx))
        else:
            url = "/cli/global/system/sql/custom-skipidx"
        
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
