"""Type stubs for logview.adom.logfiles.state"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class LogviewAdomLogfilesState:
    """FortiAnalyzer endpoint: logview.adom.logfiles.state"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str,
        apiver: int = 3,
        devid: Literal["device-id", "All_FortiGate", "All_FortiMail", "All_FortiWeb", "All_FortiManager", "All_Syslog", "All_FortiClient", "All_FortiCache", "All_FortiProxy", "All_FortiAnalyzer", "All_FortiSandbox", "All_FortiAuthenticator", "All_FortiDDoS"] | None = None,
        filename: str | None = None,
        time_range: dict[str, Any] | None = None,
        timezone: str | None = None,
        vdom: str | None = None,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["LogviewAdomLogfilesState"]