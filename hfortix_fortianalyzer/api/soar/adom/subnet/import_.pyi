"""Type stubs for soar.adom.subnet.import"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomSubnetImport:
    """FortiAnalyzer endpoint: soar.adom.subnet.import"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        data: dict[str, Any],
        apiver: int = 3,
        conflict_option: Literal["rename", "replace", "skip"] | None = None,
        data_type: Literal["zip/base64", "txt"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["SoarAdomSubnetImport"]