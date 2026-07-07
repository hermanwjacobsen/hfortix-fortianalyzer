"""FortiAnalyzer workflow system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import approval_matrix

__all__ = ["Workflow"]


class Workflow:
    """FortiAnalyzer workflow system API endpoints."""

    approval_matrix: "approval_matrix.CliGlobalSystemWorkflowApprovalMatrix"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Workflow namespace with JSON-RPC client."""
        from . import approval_matrix as approval_matrix_module

        self.approval_matrix = approval_matrix_module.CliGlobalSystemWorkflowApprovalMatrix(client)
