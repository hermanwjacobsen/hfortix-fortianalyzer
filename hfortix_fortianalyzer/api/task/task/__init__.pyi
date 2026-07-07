"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .line import TaskTaskLine

__all__ = ["TaskTask"]


from ..task_base import TaskTask as TaskTaskBase

class TaskTask(TaskTaskBase):
    """TaskTask endpoints."""

    line: TaskTaskLine

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
