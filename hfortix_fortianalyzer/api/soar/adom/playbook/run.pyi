"""Type stubs for soar.adom.playbook.run"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomPlaybookRun:
    """FortiAnalyzer endpoint: soar.adom.playbook.run"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        playbook_uuid: str,
        apiver: int = 3,
        incident_id: str | None = None,
        playbook_input: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        apiver: int = 3,
        playbook_runs: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        playbook_uuid: str | None = None,
        sort_by: list[dict[str, Any]] | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomPlaybookRun"]