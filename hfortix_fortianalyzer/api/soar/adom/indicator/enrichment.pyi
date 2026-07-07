"""Type stubs for soar.adom.indicator.enrichment"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIndicatorEnrichment:
    """FortiAnalyzer endpoint: soar.adom.indicator.enrichment"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        enrichment: list[dict[str, Any]],
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
        indicator_type: Literal["IP", "URL", "Domain"] | None = None,
        indicator_uuid: str | None = None,
        indicator_value: str | None = None,
        referenced_by: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
        detail_level: Literal["standard", "extended"] | None = None,
        indicator_type: Literal["IP", "URL", "Domain"] | None = None,
        indicator_uuid: str | None = None,
        indicator_value: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...

    def update(
        self,
        adom: str,
        enrichment_uuid: int | str | None = None,
        apiver: int = 3,
        enrichment_confidence: float | None = None,
        enrichment_expired: Literal["Yes", "No"] | None = None,
        enrichment_reputation: Literal["Suspicious", "Malicious", "NoReputationAvailable", "TBD", "Good"] | None = None,
        enrichment_status: Literal["InProcess", "Completed", "Failed"] | None = None,
        enrichment_tlp: Literal["Red", "Amber", "Green", "White"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["SoarAdomIndicatorEnrichment"]