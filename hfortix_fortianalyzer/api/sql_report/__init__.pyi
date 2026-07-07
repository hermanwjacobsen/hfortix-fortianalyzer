"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .layout import Layout
    from .schedule import Schedule

__all__ = ["Sqlreport"]


class Sqlreport:
    """Sqlreport endpoints."""

    layout: Layout
    schedule: Schedule

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
