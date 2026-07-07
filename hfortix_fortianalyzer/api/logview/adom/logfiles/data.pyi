"""Type stubs for logview.adom.logfiles.data"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfilesData:
    """FortiAnalyzer endpoint: logview.adom.logfiles.data"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        devid: str,
        filename: str,
        vdom: str,
        apiver: int = 3,
        data_type: Literal["base64", "csv/gzip/base64", "text/gzip/base64"] | None = None,
        length: float | None = None,
        offset: float | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogfilesData"]