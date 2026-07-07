"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .indicator import SoarAdomAlertIndicator

__all__ = ["Alert"]


class Alert:
    """Alert endpoints."""

    indicator: SoarAdomAlertIndicator

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
