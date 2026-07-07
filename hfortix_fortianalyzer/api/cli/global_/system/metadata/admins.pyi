"""Type stubs for cli.global.system.metadata.admins"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemMetadataAdminsGetItem:
    """Item yielded when iterating over CliGlobalSystemMetadataAdminsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def fieldlength(self) -> Literal["20", "50", "255"]: ...
    @property
    def fieldname(self) -> str: ...
    @property
    def importance(self) -> Literal["optional", "required"]: ...
    @property
    def status(self) -> Literal["disabled", "enabled"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemMetadataAdminsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemMetadataAdminsGet endpoint with autocomplete support."""

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
    def fieldlength(self) -> Literal["20", "50", "255"] | None:
        """Field: fieldlength"""
        ...

    @property
    def fieldname(self) -> str | None:
        """Field: fieldname"""
        ...

    @property
    def importance(self) -> Literal["optional", "required"] | None:
        """Field: importance"""
        ...

    @property
    def status(self) -> Literal["disabled", "enabled"] | None:
        """Field: status"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemMetadataAdminsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemMetadataAdmins:
    """FortiAnalyzer endpoint: cli.global.system.metadata.admins"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        admins: int | str | None = None,
        fields: list[Literal["fieldlength", "fieldname", "importance", "status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemMetadataAdminsGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        admins: int | str | None = None,
        fieldlength: Literal["20", "50", "255"] | None = None,
        fieldname: str | None = None,
        importance: Literal["optional", "required"] | None = None,
        status: Literal["disabled", "enabled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        admins: int | str | None = None,
        fieldlength: Literal["20", "50", "255"] | None = None,
        fieldname: str | None = None,
        importance: Literal["optional", "required"] | None = None,
        status: Literal["disabled", "enabled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        admins: int | str | None = None,
        fieldlength: Literal["20", "50", "255"] | None = None,
        fieldname: str | None = None,
        importance: Literal["optional", "required"] | None = None,
        status: Literal["disabled", "enabled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        admins: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemMetadataAdmins", "CliGlobalSystemMetadataAdminsGetResponse"]