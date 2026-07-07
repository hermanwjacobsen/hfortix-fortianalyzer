"""Type stubs for eventmgmt.adom.mitre-attack-matrix"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class EventmgmtAdomMitreAttackMatrix:
    """FortiAnalyzer endpoint: eventmgmt.adom.mitre-attack-matrix"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        mitre_domain: str,
        apiver: int = 3,
        option: Literal["metadata", "event-count", "incident-count", "handler-count"] | None = None,
        time_range: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["EventmgmtAdomMitreAttackMatrix"]