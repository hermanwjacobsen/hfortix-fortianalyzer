"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .approval_matrix import CliGlobalSystemWorkflowApprovalMatrix

__all__ = ["Workflow"]


class Workflow:
    """Workflow endpoints."""

    approval_matrix: CliGlobalSystemWorkflowApprovalMatrix

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
