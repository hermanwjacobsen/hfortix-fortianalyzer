"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .history import TaskTaskLineHistory

__all__ = ["TaskTaskLine"]


from ..line_base import TaskTaskLine as TaskTaskLineBase

class TaskTaskLine(TaskTaskLineBase):
    """TaskTaskLine endpoints."""

    history: TaskTaskLineHistory

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
