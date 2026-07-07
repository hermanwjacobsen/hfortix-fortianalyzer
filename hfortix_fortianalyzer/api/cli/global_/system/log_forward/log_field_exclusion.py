"""
FortiAnalyzer API endpoint: cli.global.system.log-forward.log-field-exclusion

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForwardLogFieldExclusion:
    """
    FortiAnalyzer endpoint: cli.global.system.log-forward.log-field-exclusion
    
    
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
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        fields: list[Literal["dev-type", "field-list", "id", "log-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            log_forward: log-forward parameter
            log_field_exclusion: log-field-exclusion parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None and log_field_exclusion is not None:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion/{log-field-exclusion}"
            url = url.replace("{log-forward}", log_forward)
            url = url.replace("{log-field-exclusion}", str(log_field_exclusion))
        else:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion"
            url = url.replace("{log-forward}", log_forward)
        
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
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        dev_type: Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None = None,
        field_list: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            log_forward: log-forward parameter
            log_field_exclusion: log-field-exclusion parameter
            dev_type: dev-type parameter
            field_list: field-list parameter
            id: id parameter
            log_type: log-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion"
        url = url.replace("{log-forward}", log_forward)
        
        # Build data payload
        data = {}
        if dev_type is not None:
            data["dev-type"] = dev_type
        if field_list is not None:
            data["field-list"] = field_list
        if id is not None:
            data["id"] = id
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
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        dev_type: Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None = None,
        field_list: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            log_forward: log-forward parameter
            log_field_exclusion: log-field-exclusion parameter
            dev_type: dev-type parameter
            field_list: field-list parameter
            id: id parameter
            log_type: log-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None and log_field_exclusion is not None:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion/{log-field-exclusion}"
            url = url.replace("{log-forward}", log_forward)
            url = url.replace("{log-field-exclusion}", str(log_field_exclusion))
        else:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion"
            url = url.replace("{log-forward}", log_forward)
        
        # Build data payload
        data = {}
        if dev_type is not None:
            data["dev-type"] = dev_type
        if field_list is not None:
            data["field-list"] = field_list
        if id is not None:
            data["id"] = id
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
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        dev_type: Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None = None,
        field_list: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            log_forward: log-forward parameter
            log_field_exclusion: log-field-exclusion parameter
            dev_type: dev-type parameter
            field_list: field-list parameter
            id: id parameter
            log_type: log-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None and log_field_exclusion is not None:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion/{log-field-exclusion}"
            url = url.replace("{log-forward}", log_forward)
            url = url.replace("{log-field-exclusion}", str(log_field_exclusion))
        else:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion"
            url = url.replace("{log-forward}", log_forward)
        
        # Build data payload
        data = {}
        if dev_type is not None:
            data["dev-type"] = dev_type
        if field_list is not None:
            data["field-list"] = field_list
        if id is not None:
            data["id"] = id
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

    def delete(self, log_forward: str, log_field_exclusion: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            log_forward: log-forward parameter
            log_field_exclusion: log-field-exclusion parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if log_forward is not None and log_field_exclusion is not None:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion/{log-field-exclusion}"
            url = url.replace("{log-forward}", log_forward)
            url = url.replace("{log-field-exclusion}", str(log_field_exclusion))
        else:
            url = "/cli/global/system/log-forward/{log-forward}/log-field-exclusion"
            url = url.replace("{log-forward}", log_forward)
        
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
