"""FortiAnalyzer approval_matrix workflow API endpoints."""

from __future__ import annotations

from ..approval_matrix_base import CliGlobalSystemWorkflowApprovalMatrix as CliGlobalSystemWorkflowApprovalMatrixBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import approver

__all__ = ["CliGlobalSystemWorkflowApprovalMatrix"]


class CliGlobalSystemWorkflowApprovalMatrix(CliGlobalSystemWorkflowApprovalMatrixBase):
    """FortiAnalyzer approval_matrix workflow API endpoints."""

    approver: "approver.CliGlobalSystemWorkflowApprovalMatrixApprover"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemWorkflowApprovalMatrix with endpoint methods and child modules."""
        super().__init__(client)

        from . import approver as approver_module

        self.approver = approver_module.CliGlobalSystemWorkflowApprovalMatrixApprover(client)
