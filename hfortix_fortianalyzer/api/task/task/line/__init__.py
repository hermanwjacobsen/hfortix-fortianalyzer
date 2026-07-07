"""FortiAnalyzer line task API endpoints."""

from __future__ import annotations

from ..line_base import TaskTaskLine as TaskTaskLineBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import history

__all__ = ["TaskTaskLine"]


class TaskTaskLine(TaskTaskLineBase):
    """FortiAnalyzer line task API endpoints."""

    history: "history.TaskTaskLineHistory"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize TaskTaskLine with endpoint methods and child modules."""
        super().__init__(client)

        from . import history as history_module

        self.history = history_module.TaskTaskLineHistory(client)
