"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ack import IocAdomEventsAck

__all__ = ["Events"]


class Events:
    """Events endpoints."""

    ack: IocAdomEventsAck

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
