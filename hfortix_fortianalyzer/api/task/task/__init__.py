"""FortiAnalyzer task API endpoints."""

from __future__ import annotations

from ..task_base import TaskTask as TaskTaskBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import line

__all__ = ["TaskTask"]


class TaskTask(TaskTaskBase):
    """FortiAnalyzer task API endpoints."""

    line: "line.TaskTaskLine"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize TaskTask with endpoint methods and child modules."""
        super().__init__(client)

        from . import line as line_module

        self.line = line_module.TaskTaskLine(client)
