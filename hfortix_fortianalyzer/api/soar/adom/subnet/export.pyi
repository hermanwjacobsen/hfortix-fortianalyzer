"""Type stubs for soar.adom.subnet.export"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomSubnetExport:
    """FortiAnalyzer endpoint: soar.adom.subnet.export"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        data_format: Literal["zip", "txt"] | None = None,
        filter: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomSubnetExport"]