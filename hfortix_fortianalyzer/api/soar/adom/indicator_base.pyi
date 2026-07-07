"""Type stubs for soar.adom.indicator"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomIndicator:
    """FortiAnalyzer endpoint: soar.adom.indicator"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        indicator_type: Literal["IP", "URL", "Domain"],
        indicator_value: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def delete(
        self,
        adom: str,
        indicator_uuid: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        filter: str | None = None,
        limit: float | None = None,
        offset: float | None = None,
        option: list[Literal["referenced-by-incident", "referenced-by-alert"]] | None = None,
        time_range: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...

    def update(
        self,
        adom: str,
        indicator_uuid: str,
        apiver: int = 3,
        country: str | None = None,
        description: str | None = None,
        status: Literal["TBD", "Unblocked", "Excluded", "Blocked", "Isolated"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["SoarAdomIndicator"]