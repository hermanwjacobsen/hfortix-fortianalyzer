"""Type stubs for cli.global.system.workflow.approval-matrix"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemWorkflowApprovalMatrixGetItem:
    """Item yielded when iterating over CliGlobalSystemWorkflowApprovalMatrixGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom_name(self) -> str: ...
    @property
    def approver(self) -> list[ApproverItem]: ...
    @property
    def mail_server(self) -> str: ...
    @property
    def notify(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class ApproverItem:
    """Nested item type for approver array."""

    @property
    def member(self) -> str: ...
    @property
    def seq_num(self) -> int: ...


class CliGlobalSystemWorkflowApprovalMatrixGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemWorkflowApprovalMatrixGet endpoint with autocomplete support."""

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
    def adom_name(self) -> str | None:
        """Field: adom-name"""
        ...

    @property
    def approver(self) -> list[ApproverItem]:
        """Field: approver"""
        ...

    @property
    def mail_server(self) -> str | None:
        """Field: mail-server"""
        ...

    @property
    def notify(self) -> str | None:
        """Field: notify"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemWorkflowApprovalMatrixGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemWorkflowApprovalMatrix:
    """FortiAnalyzer endpoint: cli.global.system.workflow.approval-matrix"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        approval_matrix: int | str | None = None,
        fields: list[Literal["adom-name", "mail-server", "notify"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemWorkflowApprovalMatrixGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        approval_matrix: int | str | None = None,
        adom_name: str | None = None,
        approver: list[dict[str, Any]] | None = None,
        mail_server: str | None = None,
        notify: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        approval_matrix: int | str | None = None,
        adom_name: str | None = None,
        approver: list[dict[str, Any]] | None = None,
        mail_server: str | None = None,
        notify: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        approval_matrix: int | str | None = None,
        adom_name: str | None = None,
        approver: list[dict[str, Any]] | None = None,
        mail_server: str | None = None,
        notify: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        approval_matrix: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemWorkflowApprovalMatrix", "CliGlobalSystemWorkflowApprovalMatrixGetResponse"]