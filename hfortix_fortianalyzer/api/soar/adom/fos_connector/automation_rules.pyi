"""Type stubs for soar.adom.fos-connector.automation-rules"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomFosConnectorAutomationRules:
    """FortiAnalyzer endpoint: soar.adom.fos-connector.automation-rules"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomFosConnectorAutomationRules"]