"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .approver import CliGlobalSystemWorkflowApprovalMatrixApprover

__all__ = ["CliGlobalSystemWorkflowApprovalMatrix"]


from ..approval_matrix_base import CliGlobalSystemWorkflowApprovalMatrix as CliGlobalSystemWorkflowApprovalMatrixBase

class CliGlobalSystemWorkflowApprovalMatrix(CliGlobalSystemWorkflowApprovalMatrixBase):
    """CliGlobalSystemWorkflowApprovalMatrix endpoints."""

    approver: CliGlobalSystemWorkflowApprovalMatrixApprover

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
