"""
FortiAnalyzer API endpoint: incidentmgmt.adom.epeu-history

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IncidentmgmtAdomEpeuHistory:
    """
    FortiAnalyzer endpoint: incidentmgmt.adom.epeu-history
    
    Add new incident epeu-history.
    
    Available methods: add, delete, get, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def add(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        attachid: str | None = None,
        dvid: float | None = None,
        endpoint: str | None = None,
        epid: float | None = None,
        epip: str | None = None,
        euid: float | None = None,
        euname: str | None = None,
        eventid: str | None = None,
        fctuid: str | None = None,
        mac: str | None = None,
        notes: str | None = None,
        osname: str | None = None,
        osversion: str | None = None,
        srcinfo: str | None = None,
        srctype: Literal["manual-input", "auto-event-attachement", "manual-event-attachment", "auto-incident", "manual-incident"] | None = None,
        tags: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Add new incident epeu-history.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/epeu-history"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "incid": incid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if attachid is not None:
            params[0]["attachid"] = attachid
        if dvid is not None:
            params[0]["dvid"] = dvid
        if endpoint is not None:
            params[0]["endpoint"] = endpoint
        if epid is not None:
            params[0]["epid"] = epid
        if epip is not None:
            params[0]["epip"] = epip
        if euid is not None:
            params[0]["euid"] = euid
        if euname is not None:
            params[0]["euname"] = euname
        if eventid is not None:
            params[0]["eventid"] = eventid
        if fctuid is not None:
            params[0]["fctuid"] = fctuid
        if mac is not None:
            params[0]["mac"] = mac
        if notes is not None:
            params[0]["notes"] = notes
        if osname is not None:
            params[0]["osname"] = osname
        if osversion is not None:
            params[0]["osversion"] = osversion
        if srcinfo is not None:
            params[0]["srcinfo"] = srcinfo
        if srctype is not None:
            params[0]["srctype"] = srctype
        if tags is not None:
            params[0]["tags"] = tags
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        seqid: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Add new incident epeu-history.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/epeu-history"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "incid": incid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if seqid is not None:
            params[0]["seqid"] = seqid
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def get(
        self,
        adom: str,
        incid: str,
        apiver: int = 3,
        limit: float | None = None,
        offset: float | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Add new incident epeu-history.
        
        Args:
            adom: adom path parameter.
            apiver: Current API version.
            incid: The incident ID.
            limit: The maximun number of records to get.
            offset: The offset of records to get.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/epeu-history"
        url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        request_params = {}
        request_params["apiver"] = apiver
        if incid is not None:
            request_params["incid"] = incid
        if limit is not None:
            request_params["limit"] = limit
        if offset is not None:
            request_params["offset"] = offset
        
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

    def update(
        self,
        adom: str,
        seqid: str,
        apiver: int = 3,
        attachid: str | None = None,
        dvid: float | None = None,
        endpoint: str | None = None,
        epid: float | None = None,
        epip: str | None = None,
        euid: float | None = None,
        euname: str | None = None,
        eventid: str | None = None,
        fctuid: str | None = None,
        mac: str | None = None,
        notes: str | None = None,
        osname: str | None = None,
        osversion: str | None = None,
        srcinfo: str | None = None,
        srctype: Literal["manual-input", "auto-event-attachement", "manual-event-epeu-history", "auto-incident", "manual-incident"] | None = None,
        tags: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Add new incident epeu-history.
        
        Args:
            adom: adom path parameter.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/incidentmgmt/adom/{adom}/epeu-history"
        url = url.replace("{adom}", adom)
        
        # Execute JSON-RPC API call
        # Params-level properties go alongside url
        params = [{
            "url": url,
            "seqid": seqid
        }]
        if apiver is not None:
            params[0]["apiver"] = apiver
        if attachid is not None:
            params[0]["attachid"] = attachid
        if dvid is not None:
            params[0]["dvid"] = dvid
        if endpoint is not None:
            params[0]["endpoint"] = endpoint
        if epid is not None:
            params[0]["epid"] = epid
        if epip is not None:
            params[0]["epip"] = epip
        if euid is not None:
            params[0]["euid"] = euid
        if euname is not None:
            params[0]["euname"] = euname
        if eventid is not None:
            params[0]["eventid"] = eventid
        if fctuid is not None:
            params[0]["fctuid"] = fctuid
        if mac is not None:
            params[0]["mac"] = mac
        if notes is not None:
            params[0]["notes"] = notes
        if osname is not None:
            params[0]["osname"] = osname
        if osversion is not None:
            params[0]["osversion"] = osversion
        if srcinfo is not None:
            params[0]["srcinfo"] = srcinfo
        if srctype is not None:
            params[0]["srctype"] = srctype
        if tags is not None:
            params[0]["tags"] = tags
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)
