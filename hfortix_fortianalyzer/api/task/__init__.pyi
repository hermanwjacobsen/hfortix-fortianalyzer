"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .task import TaskTask

__all__ = ["Task"]


class Task:
    """Task endpoints."""

    task: TaskTask

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
