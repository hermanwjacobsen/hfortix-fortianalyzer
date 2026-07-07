"""Type stubs for soar.adom.playbook.import"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomPlaybookImport:
    """FortiAnalyzer endpoint: soar.adom.playbook.import"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        data: str,
        apiver: int = 3,
        attachment: list[Literal["connector"]] | None = None,
        conflict_option: Literal["rename", "replace", "skip"] | None = None,
        data_type: Literal["zip/base64", "txt"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...


__all__ = ["SoarAdomPlaybookImport"]