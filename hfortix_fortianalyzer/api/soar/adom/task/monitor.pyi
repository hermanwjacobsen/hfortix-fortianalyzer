"""Type stubs for soar.adom.task.monitor"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomTaskMonitor:
    """FortiAnalyzer endpoint: soar.adom.task.monitor"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        playbook_uuid: str,
        apiver: int = 3,
        filter: str | None = None,
        instance_id: str | None = None,
        run_id: str | None = None,
        sort_by: list[dict[str, Any]] | None = None,
        time_range: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomTaskMonitor"]