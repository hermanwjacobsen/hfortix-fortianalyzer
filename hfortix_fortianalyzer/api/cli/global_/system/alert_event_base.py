"""
FortiAnalyzer API endpoint: cli.global.system.alert-event

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertEvent:
    """
    FortiAnalyzer endpoint: cli.global.system.alert-event
    
    
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
        alert_event: int | str | None = None,
        fields: list[Literal["enable-generic-text", "enable-severity-filter", "event-time-period", "generic-text", "name", "num-events", "severity-filter", "severity-level-comp", "severity-level-logs"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            alert_event: alert-event parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None:
            url = "/cli/global/system/alert-event/{alert-event}"
            url = url.replace("{alert-event}", str(alert_event))
        else:
            url = "/cli/global/system/alert-event"
        
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
        alert_event: int | str | None = None,
        enable_generic_text: Literal["disable", "enable"] | None = None,
        enable_severity_filter: Literal["disable", "enable"] | None = None,
        event_time_period: Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None = None,
        num_events: Literal["1", "5", "10", "50", "100"] | None = None,
        severity_filter: Literal["high", "medium-high", "medium", "medium-low", "low"] | None = None,
        severity_level_comp: Literal["=", ">=", "<="] | None = None,
        alert_destination: list[Any] | None = None,
        generic_text: str | None = None,
        name: str | None = None,
        severity_level_logs: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            enable_generic_text: enable-generic-text parameter
            enable_severity_filter: enable-severity-filter parameter
            event_time_period: event-time-period parameter
            generic_text: generic-text parameter
            name: name parameter
            num_events: num-events parameter
            severity_filter: severity-filter parameter
            severity_level_comp: severity-level-comp parameter
            severity_level_logs: severity-level-logs parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/alert-event"
        
        # Build data payload
        data = {}
        if alert_destination is not None:
            data["alert-destination"] = alert_destination
        if enable_generic_text is not None:
            data["enable-generic-text"] = enable_generic_text
        if enable_severity_filter is not None:
            data["enable-severity-filter"] = enable_severity_filter
        if event_time_period is not None:
            data["event-time-period"] = event_time_period
        if generic_text is not None:
            data["generic-text"] = generic_text
        if name is not None:
            data["name"] = name
        if num_events is not None:
            data["num-events"] = num_events
        if severity_filter is not None:
            data["severity-filter"] = severity_filter
        if severity_level_comp is not None:
            data["severity-level-comp"] = severity_level_comp
        if severity_level_logs is not None:
            data["severity-level-logs"] = severity_level_logs
        
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
        alert_event: int | str | None = None,
        enable_generic_text: Literal["disable", "enable"] | None = None,
        enable_severity_filter: Literal["disable", "enable"] | None = None,
        event_time_period: Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None = None,
        num_events: Literal["1", "5", "10", "50", "100"] | None = None,
        severity_filter: Literal["high", "medium-high", "medium", "medium-low", "low"] | None = None,
        severity_level_comp: Literal["=", ">=", "<="] | None = None,
        alert_destination: list[Any] | None = None,
        generic_text: str | None = None,
        name: str | None = None,
        severity_level_logs: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            enable_generic_text: enable-generic-text parameter
            enable_severity_filter: enable-severity-filter parameter
            event_time_period: event-time-period parameter
            generic_text: generic-text parameter
            name: name parameter
            num_events: num-events parameter
            severity_filter: severity-filter parameter
            severity_level_comp: severity-level-comp parameter
            severity_level_logs: severity-level-logs parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None:
            url = "/cli/global/system/alert-event/{alert-event}"
            url = url.replace("{alert-event}", str(alert_event))
        else:
            url = "/cli/global/system/alert-event"
        
        # Build data payload
        data = {}
        if alert_destination is not None:
            data["alert-destination"] = alert_destination
        if enable_generic_text is not None:
            data["enable-generic-text"] = enable_generic_text
        if enable_severity_filter is not None:
            data["enable-severity-filter"] = enable_severity_filter
        if event_time_period is not None:
            data["event-time-period"] = event_time_period
        if generic_text is not None:
            data["generic-text"] = generic_text
        if name is not None:
            data["name"] = name
        if num_events is not None:
            data["num-events"] = num_events
        if severity_filter is not None:
            data["severity-filter"] = severity_filter
        if severity_level_comp is not None:
            data["severity-level-comp"] = severity_level_comp
        if severity_level_logs is not None:
            data["severity-level-logs"] = severity_level_logs
        
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
        alert_event: int | str | None = None,
        enable_generic_text: Literal["disable", "enable"] | None = None,
        enable_severity_filter: Literal["disable", "enable"] | None = None,
        event_time_period: Literal["0.5", "1", "3", "6", "12", "24", "72", "168"] | None = None,
        num_events: Literal["1", "5", "10", "50", "100"] | None = None,
        severity_filter: Literal["high", "medium-high", "medium", "medium-low", "low"] | None = None,
        severity_level_comp: Literal["=", ">=", "<="] | None = None,
        alert_destination: list[Any] | None = None,
        generic_text: str | None = None,
        name: str | None = None,
        severity_level_logs: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            enable_generic_text: enable-generic-text parameter
            enable_severity_filter: enable-severity-filter parameter
            event_time_period: event-time-period parameter
            generic_text: generic-text parameter
            name: name parameter
            num_events: num-events parameter
            severity_filter: severity-filter parameter
            severity_level_comp: severity-level-comp parameter
            severity_level_logs: severity-level-logs parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None:
            url = "/cli/global/system/alert-event/{alert-event}"
            url = url.replace("{alert-event}", str(alert_event))
        else:
            url = "/cli/global/system/alert-event"
        
        # Build data payload
        data = {}
        if alert_destination is not None:
            data["alert-destination"] = alert_destination
        if enable_generic_text is not None:
            data["enable-generic-text"] = enable_generic_text
        if enable_severity_filter is not None:
            data["enable-severity-filter"] = enable_severity_filter
        if event_time_period is not None:
            data["event-time-period"] = event_time_period
        if generic_text is not None:
            data["generic-text"] = generic_text
        if name is not None:
            data["name"] = name
        if num_events is not None:
            data["num-events"] = num_events
        if severity_filter is not None:
            data["severity-filter"] = severity_filter
        if severity_level_comp is not None:
            data["severity-level-comp"] = severity_level_comp
        if severity_level_logs is not None:
            data["severity-level-logs"] = severity_level_logs
        
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

    def delete(self, alert_event: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            alert_event: alert-event parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None:
            url = "/cli/global/system/alert-event/{alert-event}"
            url = url.replace("{alert-event}", str(alert_event))
        else:
            url = "/cli/global/system/alert-event"
        
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
