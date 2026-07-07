"""FortiAnalyzer task API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import task

__all__ = ["Task"]


class Task:
    """FortiAnalyzer task API endpoints."""

    task: "task.TaskTask"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Task namespace with JSON-RPC client."""
        from . import task as task_module

        self.task = task_module.TaskTask(client)
