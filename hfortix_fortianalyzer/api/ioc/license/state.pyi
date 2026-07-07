"""Type stubs for ioc.license.state"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class IocLicenseState:
    """FortiAnalyzer endpoint: ioc.license.state"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["IocLicenseState"]