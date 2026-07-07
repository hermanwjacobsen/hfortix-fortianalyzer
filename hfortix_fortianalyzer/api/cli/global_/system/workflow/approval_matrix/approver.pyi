"""Type stubs for cli.global.system.workflow.approval-matrix.approver"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemWorkflowApprovalMatrixApproverGetItem:
    """Item yielded when iterating over CliGlobalSystemWorkflowApprovalMatrixApproverGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def member(self) -> str: ...
    @property
    def seq_num(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemWorkflowApprovalMatrixApproverGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemWorkflowApprovalMatrixApproverGet endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def oid(self) -> int | None:
        """Object ID (dynamically added by FortiAnalyzer API, not in Swagger schema)"""
        ...

    @property
    def member(self) -> str | None:
        """Field: member"""
        ...

    @property
    def seq_num(self) -> int | None:
        """Field: seq_num"""
        ...


    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[CliGlobalSystemWorkflowApprovalMatrixApproverGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemWorkflowApprovalMatrixApprover:
    """FortiAnalyzer endpoint: cli.global.system.workflow.approval-matrix.approver"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        approval_matrix: str,
        approver: int | str | None = None,
        fields: list[Literal["member", "seq_num"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemWorkflowApprovalMatrixApproverGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        approval_matrix: str,
        approver: int | str | None = None,
        member: str | None = None,
        seq_num: int | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        approval_matrix: str,
        approver: int | str | None = None,
        member: str | None = None,
        seq_num: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        approval_matrix: str,
        approver: int | str | None = None,
        member: str | None = None,
        seq_num: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        approval_matrix: str,
        approver: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemWorkflowApprovalMatrixApprover", "CliGlobalSystemWorkflowApprovalMatrixApproverGetResponse"]