"""
FortiAnalyzer API endpoint: cli.global.system.sql

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemSql:
    """
    FortiAnalyzer endpoint: cli.global.system.sql
    
    
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
        url = "/cli/global/system/sql"
        
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
        background_rebuild: Literal["disable", "enable"] | None = None,
        compress_table_min_age: int | None = None,
        database_type: Literal["mysql", "postgres"] | None = None,
        device_count_high: Literal["disable", "enable"] | None = None,
        event_table_partition_time: int | None = None,
        fct_table_partition_time: int | None = None,
        prompt_sql_upgrade: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "local"] | None = None,
        text_search_index: Literal["disable", "enable"] | None = None,
        traffic_table_partition_time: int | None = None,
        utm_table_partition_time: int | None = None,
        custom_index: list[Any] | None = None,
        custom_skipidx: list[Any] | None = None,
        database_name: str | None = None,
        logtype: list[Any] | None = None,
        password: list[Any] | None = None,
        server: str | None = None,
        start_time: list[Any] | None = None,
        ts_index_field: list[Any] | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            background_rebuild: background-rebuild parameter
            compress_table_min_age: compress-table-min-age parameter
            custom_index: custom-index parameter
            custom_skipidx: custom-skipidx parameter
            database_name: database-name parameter
            database_type: database-type parameter
            device_count_high: device-count-high parameter
            event_table_partition_time: event-table-partition-time parameter
            fct_table_partition_time: fct-table-partition-time parameter
            logtype: logtype parameter
            ... (10 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/sql"
        
        # Build data payload
        data = {}
        if background_rebuild is not None:
            data["background-rebuild"] = background_rebuild
        if compress_table_min_age is not None:
            data["compress-table-min-age"] = compress_table_min_age
        if custom_index is not None:
            data["custom-index"] = custom_index
        if custom_skipidx is not None:
            data["custom-skipidx"] = custom_skipidx
        if database_name is not None:
            data["database-name"] = database_name
        if database_type is not None:
            data["database-type"] = database_type
        if device_count_high is not None:
            data["device-count-high"] = device_count_high
        if event_table_partition_time is not None:
            data["event-table-partition-time"] = event_table_partition_time
        if fct_table_partition_time is not None:
            data["fct-table-partition-time"] = fct_table_partition_time
        if logtype is not None:
            data["logtype"] = logtype
        if password is not None:
            data["password"] = password
        if prompt_sql_upgrade is not None:
            data["prompt-sql-upgrade"] = prompt_sql_upgrade
        if server is not None:
            data["server"] = server
        if start_time is not None:
            data["start-time"] = start_time
        if status is not None:
            data["status"] = status
        if text_search_index is not None:
            data["text-search-index"] = text_search_index
        if traffic_table_partition_time is not None:
            data["traffic-table-partition-time"] = traffic_table_partition_time
        if ts_index_field is not None:
            data["ts-index-field"] = ts_index_field
        if username is not None:
            data["username"] = username
        if utm_table_partition_time is not None:
            data["utm-table-partition-time"] = utm_table_partition_time
        
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
        background_rebuild: Literal["disable", "enable"] | None = None,
        compress_table_min_age: int | None = None,
        database_type: Literal["mysql", "postgres"] | None = None,
        device_count_high: Literal["disable", "enable"] | None = None,
        event_table_partition_time: int | None = None,
        fct_table_partition_time: int | None = None,
        prompt_sql_upgrade: Literal["disable", "enable"] | None = None,
        status: Literal["disable", "local"] | None = None,
        text_search_index: Literal["disable", "enable"] | None = None,
        traffic_table_partition_time: int | None = None,
        utm_table_partition_time: int | None = None,
        custom_index: list[Any] | None = None,
        custom_skipidx: list[Any] | None = None,
        database_name: str | None = None,
        logtype: list[Any] | None = None,
        password: list[Any] | None = None,
        server: str | None = None,
        start_time: list[Any] | None = None,
        ts_index_field: list[Any] | None = None,
        username: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            background_rebuild: background-rebuild parameter
            compress_table_min_age: compress-table-min-age parameter
            custom_index: custom-index parameter
            custom_skipidx: custom-skipidx parameter
            database_name: database-name parameter
            database_type: database-type parameter
            device_count_high: device-count-high parameter
            event_table_partition_time: event-table-partition-time parameter
            fct_table_partition_time: fct-table-partition-time parameter
            logtype: logtype parameter
            ... (10 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/sql"
        
        # Build data payload
        data = {}
        if background_rebuild is not None:
            data["background-rebuild"] = background_rebuild
        if compress_table_min_age is not None:
            data["compress-table-min-age"] = compress_table_min_age
        if custom_index is not None:
            data["custom-index"] = custom_index
        if custom_skipidx is not None:
            data["custom-skipidx"] = custom_skipidx
        if database_name is not None:
            data["database-name"] = database_name
        if database_type is not None:
            data["database-type"] = database_type
        if device_count_high is not None:
            data["device-count-high"] = device_count_high
        if event_table_partition_time is not None:
            data["event-table-partition-time"] = event_table_partition_time
        if fct_table_partition_time is not None:
            data["fct-table-partition-time"] = fct_table_partition_time
        if logtype is not None:
            data["logtype"] = logtype
        if password is not None:
            data["password"] = password
        if prompt_sql_upgrade is not None:
            data["prompt-sql-upgrade"] = prompt_sql_upgrade
        if server is not None:
            data["server"] = server
        if start_time is not None:
            data["start-time"] = start_time
        if status is not None:
            data["status"] = status
        if text_search_index is not None:
            data["text-search-index"] = text_search_index
        if traffic_table_partition_time is not None:
            data["traffic-table-partition-time"] = traffic_table_partition_time
        if ts_index_field is not None:
            data["ts-index-field"] = ts_index_field
        if username is not None:
            data["username"] = username
        if utm_table_partition_time is not None:
            data["utm-table-partition-time"] = utm_table_partition_time
        
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
