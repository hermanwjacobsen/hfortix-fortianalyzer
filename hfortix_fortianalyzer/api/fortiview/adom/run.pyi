"""Type stubs for fortiview.adom.run"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class FortiviewAdomRun:
    """FortiAnalyzer endpoint: fortiview.adom.run"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        view_name: str,
        adom: str,
        time_range: dict[str, Any],
        tid: int | str | None = None,
        apiver: int = 3,
        count_total: bool | None = None,
        device: list[dict[str, Any]] | None = None,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        sort_by: list[dict[str, Any]] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        view_name: str,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        view_name: str,
        adom: str,
        tid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["FortiviewAdomRun"]