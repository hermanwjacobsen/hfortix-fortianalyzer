"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .filter import CliGlobalSystemLocallogTacacsAccountingFilter
    from .setting import CliGlobalSystemLocallogTacacsAccountingSetting

__all__ = ["Tacacsaccounting"]


class Tacacsaccounting:
    """Tacacsaccounting endpoints."""

    filter: CliGlobalSystemLocallogTacacsAccountingFilter
    setting: CliGlobalSystemLocallogTacacsAccountingSetting

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
