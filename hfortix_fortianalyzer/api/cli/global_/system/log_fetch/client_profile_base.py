"""
FortiAnalyzer API endpoint: cli.global.system.log-fetch.client-profile

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogFetchClientProfile:
    """
    FortiAnalyzer endpoint: cli.global.system.log-fetch.client-profile
    
    
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
        client_profile: int | str | None = None,
        fields: list[Literal["client-adom", "data-range", "data-range-value", "end-time", "id", "index-fetch-logs", "log-filter-logic", "log-filter-status", "name", "password", "peer-cert-cn", "secure-connection", "server-adom", "server-ip", "start-time", "sync-adom-config", "user"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            client_profile: client-profile parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}"
            url = url.replace("{client-profile}", str(client_profile))
        else:
            url = "/cli/global/system/log-fetch/client-profile"
        
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
        client_profile: int | str | None = None,
        data_range: Literal["custom"] | None = None,
        data_range_value: int | None = None,
        id: int | None = None,
        index_fetch_logs: Literal["disable", "enable"] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        server_ip: str | None = None,
        sync_adom_config: Literal["disable", "enable"] | None = None,
        client_adom: str | None = None,
        device_filter: list[Any] | None = None,
        end_time: list[Any] | None = None,
        log_filter: list[Any] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        peer_cert_cn: str | None = None,
        server_adom: str | None = None,
        start_time: list[Any] | None = None,
        user: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            client_profile: client-profile parameter
            client_adom: client-adom parameter
            data_range: data-range parameter
            data_range_value: data-range-value parameter
            device_filter: device-filter parameter
            end_time: end-time parameter
            id: id parameter
            index_fetch_logs: index-fetch-logs parameter
            log_filter: log-filter parameter
            log_filter_logic: log-filter-logic parameter
            log_filter_status: log-filter-status parameter
            ... (9 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/log-fetch/client-profile"
        
        # Build data payload
        data = {}
        if client_adom is not None:
            data["client-adom"] = client_adom
        if data_range is not None:
            data["data-range"] = data_range
        if data_range_value is not None:
            data["data-range-value"] = data_range_value
        if device_filter is not None:
            data["device-filter"] = device_filter
        if end_time is not None:
            data["end-time"] = end_time
        if id is not None:
            data["id"] = id
        if index_fetch_logs is not None:
            data["index-fetch-logs"] = index_fetch_logs
        if log_filter is not None:
            data["log-filter"] = log_filter
        if log_filter_logic is not None:
            data["log-filter-logic"] = log_filter_logic
        if log_filter_status is not None:
            data["log-filter-status"] = log_filter_status
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if server_adom is not None:
            data["server-adom"] = server_adom
        if server_ip is not None:
            data["server-ip"] = server_ip
        if start_time is not None:
            data["start-time"] = start_time
        if sync_adom_config is not None:
            data["sync-adom-config"] = sync_adom_config
        if user is not None:
            data["user"] = user
        
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
        client_profile: int | str | None = None,
        data_range: Literal["custom"] | None = None,
        data_range_value: int | None = None,
        id: int | None = None,
        index_fetch_logs: Literal["disable", "enable"] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        server_ip: str | None = None,
        sync_adom_config: Literal["disable", "enable"] | None = None,
        client_adom: str | None = None,
        device_filter: list[Any] | None = None,
        end_time: list[Any] | None = None,
        log_filter: list[Any] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        peer_cert_cn: str | None = None,
        server_adom: str | None = None,
        start_time: list[Any] | None = None,
        user: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            client_profile: client-profile parameter
            client_adom: client-adom parameter
            data_range: data-range parameter
            data_range_value: data-range-value parameter
            device_filter: device-filter parameter
            end_time: end-time parameter
            id: id parameter
            index_fetch_logs: index-fetch-logs parameter
            log_filter: log-filter parameter
            log_filter_logic: log-filter-logic parameter
            log_filter_status: log-filter-status parameter
            ... (9 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}"
            url = url.replace("{client-profile}", str(client_profile))
        else:
            url = "/cli/global/system/log-fetch/client-profile"
        
        # Build data payload
        data = {}
        if client_adom is not None:
            data["client-adom"] = client_adom
        if data_range is not None:
            data["data-range"] = data_range
        if data_range_value is not None:
            data["data-range-value"] = data_range_value
        if device_filter is not None:
            data["device-filter"] = device_filter
        if end_time is not None:
            data["end-time"] = end_time
        if id is not None:
            data["id"] = id
        if index_fetch_logs is not None:
            data["index-fetch-logs"] = index_fetch_logs
        if log_filter is not None:
            data["log-filter"] = log_filter
        if log_filter_logic is not None:
            data["log-filter-logic"] = log_filter_logic
        if log_filter_status is not None:
            data["log-filter-status"] = log_filter_status
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if server_adom is not None:
            data["server-adom"] = server_adom
        if server_ip is not None:
            data["server-ip"] = server_ip
        if start_time is not None:
            data["start-time"] = start_time
        if sync_adom_config is not None:
            data["sync-adom-config"] = sync_adom_config
        if user is not None:
            data["user"] = user
        
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
        client_profile: int | str | None = None,
        data_range: Literal["custom"] | None = None,
        data_range_value: int | None = None,
        id: int | None = None,
        index_fetch_logs: Literal["disable", "enable"] | None = None,
        log_filter_logic: Literal["and", "or"] | None = None,
        log_filter_status: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["disable", "enable"] | None = None,
        server_ip: str | None = None,
        sync_adom_config: Literal["disable", "enable"] | None = None,
        client_adom: str | None = None,
        device_filter: list[Any] | None = None,
        end_time: list[Any] | None = None,
        log_filter: list[Any] | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        peer_cert_cn: str | None = None,
        server_adom: str | None = None,
        start_time: list[Any] | None = None,
        user: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            client_profile: client-profile parameter
            client_adom: client-adom parameter
            data_range: data-range parameter
            data_range_value: data-range-value parameter
            device_filter: device-filter parameter
            end_time: end-time parameter
            id: id parameter
            index_fetch_logs: index-fetch-logs parameter
            log_filter: log-filter parameter
            log_filter_logic: log-filter-logic parameter
            log_filter_status: log-filter-status parameter
            ... (9 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}"
            url = url.replace("{client-profile}", str(client_profile))
        else:
            url = "/cli/global/system/log-fetch/client-profile"
        
        # Build data payload
        data = {}
        if client_adom is not None:
            data["client-adom"] = client_adom
        if data_range is not None:
            data["data-range"] = data_range
        if data_range_value is not None:
            data["data-range-value"] = data_range_value
        if device_filter is not None:
            data["device-filter"] = device_filter
        if end_time is not None:
            data["end-time"] = end_time
        if id is not None:
            data["id"] = id
        if index_fetch_logs is not None:
            data["index-fetch-logs"] = index_fetch_logs
        if log_filter is not None:
            data["log-filter"] = log_filter
        if log_filter_logic is not None:
            data["log-filter-logic"] = log_filter_logic
        if log_filter_status is not None:
            data["log-filter-status"] = log_filter_status
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if peer_cert_cn is not None:
            data["peer-cert-cn"] = peer_cert_cn
        if secure_connection is not None:
            data["secure-connection"] = secure_connection
        if server_adom is not None:
            data["server-adom"] = server_adom
        if server_ip is not None:
            data["server-ip"] = server_ip
        if start_time is not None:
            data["start-time"] = start_time
        if sync_adom_config is not None:
            data["sync-adom-config"] = sync_adom_config
        if user is not None:
            data["user"] = user
        
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

    def delete(self, client_profile: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            client_profile: client-profile parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if client_profile is not None:
            url = "/cli/global/system/log-fetch/client-profile/{client-profile}"
            url = url.replace("{client-profile}", str(client_profile))
        else:
            url = "/cli/global/system/log-fetch/client-profile"
        
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
