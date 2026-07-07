"""
FortiAnalyzer API endpoint: cli.global.system.alert-event.alert-destination

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAlertEventAlertDestination:
    """
    FortiAnalyzer endpoint: cli.global.system.alert-event.alert-destination
    
    
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
        alert_event: str,
        alert_destination: int | str | None = None,
        fields: list[Literal["from", "smtp-name", "snmp-name", "syslog-name", "to", "type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None and alert_destination is not None:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination/{alert-destination}"
            url = url.replace("{alert-event}", alert_event)
            url = url.replace("{alert-destination}", str(alert_destination))
        else:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination"
            url = url.replace("{alert-event}", alert_event)
        
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
        alert_event: str,
        alert_destination: int | str | None = None,
        type: Literal["mail", "snmp", "syslog"] | None = None,
        from_: str | None = None,
        smtp_name: str | None = None,
        snmp_name: str | None = None,
        syslog_name: str | None = None,
        to: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            from_: from parameter
            smtp_name: smtp-name parameter
            snmp_name: snmp-name parameter
            syslog_name: syslog-name parameter
            to: to parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/alert-event/{alert-event}/alert-destination"
        url = url.replace("{alert-event}", alert_event)
        
        # Build data payload
        data = {}
        if from_ is not None:
            data["from"] = from_
        if smtp_name is not None:
            data["smtp-name"] = smtp_name
        if snmp_name is not None:
            data["snmp-name"] = snmp_name
        if syslog_name is not None:
            data["syslog-name"] = syslog_name
        if to is not None:
            data["to"] = to
        if type is not None:
            data["type"] = type
        
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
        alert_event: str,
        alert_destination: int | str | None = None,
        type: Literal["mail", "snmp", "syslog"] | None = None,
        from_: str | None = None,
        smtp_name: str | None = None,
        snmp_name: str | None = None,
        syslog_name: str | None = None,
        to: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            from_: from parameter
            smtp_name: smtp-name parameter
            snmp_name: snmp-name parameter
            syslog_name: syslog-name parameter
            to: to parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None and alert_destination is not None:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination/{alert-destination}"
            url = url.replace("{alert-event}", alert_event)
            url = url.replace("{alert-destination}", str(alert_destination))
        else:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination"
            url = url.replace("{alert-event}", alert_event)
        
        # Build data payload
        data = {}
        if from_ is not None:
            data["from"] = from_
        if smtp_name is not None:
            data["smtp-name"] = smtp_name
        if snmp_name is not None:
            data["snmp-name"] = snmp_name
        if syslog_name is not None:
            data["syslog-name"] = syslog_name
        if to is not None:
            data["to"] = to
        if type is not None:
            data["type"] = type
        
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
        alert_event: str,
        alert_destination: int | str | None = None,
        type: Literal["mail", "snmp", "syslog"] | None = None,
        from_: str | None = None,
        smtp_name: str | None = None,
        snmp_name: str | None = None,
        syslog_name: str | None = None,
        to: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
            from_: from parameter
            smtp_name: smtp-name parameter
            snmp_name: snmp-name parameter
            syslog_name: syslog-name parameter
            to: to parameter
            type: type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None and alert_destination is not None:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination/{alert-destination}"
            url = url.replace("{alert-event}", alert_event)
            url = url.replace("{alert-destination}", str(alert_destination))
        else:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination"
            url = url.replace("{alert-event}", alert_event)
        
        # Build data payload
        data = {}
        if from_ is not None:
            data["from"] = from_
        if smtp_name is not None:
            data["smtp-name"] = smtp_name
        if snmp_name is not None:
            data["snmp-name"] = snmp_name
        if syslog_name is not None:
            data["syslog-name"] = syslog_name
        if to is not None:
            data["to"] = to
        if type is not None:
            data["type"] = type
        
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

    def delete(self, alert_event: str, alert_destination: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            alert_event: alert-event parameter
            alert_destination: alert-destination parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if alert_event is not None and alert_destination is not None:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination/{alert-destination}"
            url = url.replace("{alert-event}", alert_event)
            url = url.replace("{alert-destination}", str(alert_destination))
        else:
            url = "/cli/global/system/alert-event/{alert-event}/alert-destination"
            url = url.replace("{alert-event}", alert_event)
        
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
