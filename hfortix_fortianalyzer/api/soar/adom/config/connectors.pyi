"""Type stubs for soar.adom.config.connectors"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomConfigConnectors:
    """FortiAnalyzer endpoint: soar.adom.config.connectors"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        data: list[dict[str, Any]],
        connector_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def update(
        self,
        adom: str,
        data: list[dict[str, Any]],
        connector_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        adom: str,
        connector_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        connector_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomConfigConnectors"]