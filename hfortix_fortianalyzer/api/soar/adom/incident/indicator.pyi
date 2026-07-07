"""Type stubs for soar.adom.incident.indicator"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIncidentIndicator:
    """FortiAnalyzer endpoint: soar.adom.incident.indicator"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        incident_id: str,
        indicator_uuid: str,
        apiver: int = 3,
        enrichment_uuid: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        apiver: int = 3,
        enrichment_uuid: str | None = None,
        incident_id: str | None = None,
        indicator_uuid: str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        incident_id: str,
        apiver: int = 3,
        filter: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...

    def update(
        self,
        adom: str,
        incident_id: str,
        indicator_uuid: str,
        apiver: int = 3,
        enrichment_uuid: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["SoarAdomIncidentIndicator"]