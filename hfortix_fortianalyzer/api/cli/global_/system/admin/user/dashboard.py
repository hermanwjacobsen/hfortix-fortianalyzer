"""
FortiAnalyzer API endpoint: cli.global.system.admin.user.dashboard

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUserDashboard:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.user.dashboard
    
    
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
        user: str,
        dashboard: int | str | None = None,
        fields: list[Literal["column", "diskio-content-type", "diskio-period", "log-rate-period", "log-rate-topn", "log-rate-type", "moduleid", "name", "num-entries", "refresh-interval", "res-cpu-display", "res-period", "res-view-type", "status", "tabid", "time-period", "widget-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            user: user parameter
            dashboard: dashboard parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None and dashboard is not None:
            url = "/cli/global/system/admin/user/{user}/dashboard/{dashboard}"
            url = url.replace("{user}", user)
            url = url.replace("{dashboard}", str(dashboard))
        else:
            url = "/cli/global/system/admin/user/{user}/dashboard"
            url = url.replace("{user}", user)
        
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
        user: str,
        dashboard: int | str | None = None,
        column: int | None = None,
        diskio_content_type: Literal["util", "iops", "blks"] | None = None,
        diskio_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_topn: Literal["1", "2", "3", "4", "5"] | None = None,
        log_rate_type: Literal["log", "device"] | None = None,
        moduleid: int | None = None,
        num_entries: int | None = None,
        refresh_interval: int | None = None,
        res_cpu_display: Literal["average ", "each"] | None = None,
        res_period: Literal["10min ", "hour", "day"] | None = None,
        res_view_type: Literal["real-time ", "history"] | None = None,
        status: Literal["close", "open"] | None = None,
        tabid: int | None = None,
        time_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_period: Literal["2min ", "1hour", "6hours"] | None = None,
        name: str | None = None,
        widget_type: Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            user: user parameter
            dashboard: dashboard parameter
            column: column parameter
            diskio_content_type: diskio-content-type parameter
            diskio_period: diskio-period parameter
            log_rate_period: log-rate-period parameter
            log_rate_topn: log-rate-topn parameter
            log_rate_type: log-rate-type parameter
            moduleid: moduleid parameter
            name: name parameter
            num_entries: num-entries parameter
            refresh_interval: refresh-interval parameter
            ... (7 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/user/{user}/dashboard"
        url = url.replace("{user}", user)
        
        # Build data payload
        data = {}
        if column is not None:
            data["column"] = column
        if diskio_content_type is not None:
            data["diskio-content-type"] = diskio_content_type
        if diskio_period is not None:
            data["diskio-period"] = diskio_period
        if log_rate_period is not None:
            data["log-rate-period"] = log_rate_period
        if log_rate_topn is not None:
            data["log-rate-topn"] = log_rate_topn
        if log_rate_type is not None:
            data["log-rate-type"] = log_rate_type
        if moduleid is not None:
            data["moduleid"] = moduleid
        if name is not None:
            data["name"] = name
        if num_entries is not None:
            data["num-entries"] = num_entries
        if refresh_interval is not None:
            data["refresh-interval"] = refresh_interval
        if res_cpu_display is not None:
            data["res-cpu-display"] = res_cpu_display
        if res_period is not None:
            data["res-period"] = res_period
        if res_view_type is not None:
            data["res-view-type"] = res_view_type
        if status is not None:
            data["status"] = status
        if tabid is not None:
            data["tabid"] = tabid
        if time_period is not None:
            data["time-period"] = time_period
        if widget_type is not None:
            data["widget-type"] = widget_type
        
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
        user: str,
        dashboard: int | str | None = None,
        column: int | None = None,
        diskio_content_type: Literal["util", "iops", "blks"] | None = None,
        diskio_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_topn: Literal["1", "2", "3", "4", "5"] | None = None,
        log_rate_type: Literal["log", "device"] | None = None,
        moduleid: int | None = None,
        num_entries: int | None = None,
        refresh_interval: int | None = None,
        res_cpu_display: Literal["average ", "each"] | None = None,
        res_period: Literal["10min ", "hour", "day"] | None = None,
        res_view_type: Literal["real-time ", "history"] | None = None,
        status: Literal["close", "open"] | None = None,
        tabid: int | None = None,
        time_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_period: Literal["2min ", "1hour", "6hours"] | None = None,
        name: str | None = None,
        widget_type: Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            user: user parameter
            dashboard: dashboard parameter
            column: column parameter
            diskio_content_type: diskio-content-type parameter
            diskio_period: diskio-period parameter
            log_rate_period: log-rate-period parameter
            log_rate_topn: log-rate-topn parameter
            log_rate_type: log-rate-type parameter
            moduleid: moduleid parameter
            name: name parameter
            num_entries: num-entries parameter
            refresh_interval: refresh-interval parameter
            ... (7 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None and dashboard is not None:
            url = "/cli/global/system/admin/user/{user}/dashboard/{dashboard}"
            url = url.replace("{user}", user)
            url = url.replace("{dashboard}", str(dashboard))
        else:
            url = "/cli/global/system/admin/user/{user}/dashboard"
            url = url.replace("{user}", user)
        
        # Build data payload
        data = {}
        if column is not None:
            data["column"] = column
        if diskio_content_type is not None:
            data["diskio-content-type"] = diskio_content_type
        if diskio_period is not None:
            data["diskio-period"] = diskio_period
        if log_rate_period is not None:
            data["log-rate-period"] = log_rate_period
        if log_rate_topn is not None:
            data["log-rate-topn"] = log_rate_topn
        if log_rate_type is not None:
            data["log-rate-type"] = log_rate_type
        if moduleid is not None:
            data["moduleid"] = moduleid
        if name is not None:
            data["name"] = name
        if num_entries is not None:
            data["num-entries"] = num_entries
        if refresh_interval is not None:
            data["refresh-interval"] = refresh_interval
        if res_cpu_display is not None:
            data["res-cpu-display"] = res_cpu_display
        if res_period is not None:
            data["res-period"] = res_period
        if res_view_type is not None:
            data["res-view-type"] = res_view_type
        if status is not None:
            data["status"] = status
        if tabid is not None:
            data["tabid"] = tabid
        if time_period is not None:
            data["time-period"] = time_period
        if widget_type is not None:
            data["widget-type"] = widget_type
        
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
        user: str,
        dashboard: int | str | None = None,
        column: int | None = None,
        diskio_content_type: Literal["util", "iops", "blks"] | None = None,
        diskio_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_topn: Literal["1", "2", "3", "4", "5"] | None = None,
        log_rate_type: Literal["log", "device"] | None = None,
        moduleid: int | None = None,
        num_entries: int | None = None,
        refresh_interval: int | None = None,
        res_cpu_display: Literal["average ", "each"] | None = None,
        res_period: Literal["10min ", "hour", "day"] | None = None,
        res_view_type: Literal["real-time ", "history"] | None = None,
        status: Literal["close", "open"] | None = None,
        tabid: int | None = None,
        time_period: Literal["1hour", "8hour", "24hour"] | None = None,
        log_rate_period: Literal["2min ", "1hour", "6hours"] | None = None,
        name: str | None = None,
        widget_type: Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            user: user parameter
            dashboard: dashboard parameter
            column: column parameter
            diskio_content_type: diskio-content-type parameter
            diskio_period: diskio-period parameter
            log_rate_period: log-rate-period parameter
            log_rate_topn: log-rate-topn parameter
            log_rate_type: log-rate-type parameter
            moduleid: moduleid parameter
            name: name parameter
            num_entries: num-entries parameter
            refresh_interval: refresh-interval parameter
            ... (7 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None and dashboard is not None:
            url = "/cli/global/system/admin/user/{user}/dashboard/{dashboard}"
            url = url.replace("{user}", user)
            url = url.replace("{dashboard}", str(dashboard))
        else:
            url = "/cli/global/system/admin/user/{user}/dashboard"
            url = url.replace("{user}", user)
        
        # Build data payload
        data = {}
        if column is not None:
            data["column"] = column
        if diskio_content_type is not None:
            data["diskio-content-type"] = diskio_content_type
        if diskio_period is not None:
            data["diskio-period"] = diskio_period
        if log_rate_period is not None:
            data["log-rate-period"] = log_rate_period
        if log_rate_topn is not None:
            data["log-rate-topn"] = log_rate_topn
        if log_rate_type is not None:
            data["log-rate-type"] = log_rate_type
        if moduleid is not None:
            data["moduleid"] = moduleid
        if name is not None:
            data["name"] = name
        if num_entries is not None:
            data["num-entries"] = num_entries
        if refresh_interval is not None:
            data["refresh-interval"] = refresh_interval
        if res_cpu_display is not None:
            data["res-cpu-display"] = res_cpu_display
        if res_period is not None:
            data["res-period"] = res_period
        if res_view_type is not None:
            data["res-view-type"] = res_view_type
        if status is not None:
            data["status"] = status
        if tabid is not None:
            data["tabid"] = tabid
        if time_period is not None:
            data["time-period"] = time_period
        if widget_type is not None:
            data["widget-type"] = widget_type
        
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

    def delete(self, user: str, dashboard: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            user: user parameter
            dashboard: dashboard parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if user is not None and dashboard is not None:
            url = "/cli/global/system/admin/user/{user}/dashboard/{dashboard}"
            url = url.replace("{user}", user)
            url = url.replace("{dashboard}", str(dashboard))
        else:
            url = "/cli/global/system/admin/user/{user}/dashboard"
            url = url.replace("{user}", user)
        
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
