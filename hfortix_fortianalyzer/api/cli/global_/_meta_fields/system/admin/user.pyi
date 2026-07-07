"""Type stubs for cli.global._meta_fields.system.admin.user"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalMetaFieldsSystemAdminUserGetItem:
    """Item yielded when iterating over CliGlobalMetaFieldsSystemAdminUserGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def importance(self) -> Literal["optional", "required"]: ...
    @property
    def length(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalMetaFieldsSystemAdminUserGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalMetaFieldsSystemAdminUserGet endpoint with autocomplete support."""

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
    def importance(self) -> Literal["optional", "required"] | None:
        """Field: importance"""
        ...

    @property
    def length(self) -> int | None:
        """Field: length"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
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
    def __iter__(self) -> Iterator[CliGlobalMetaFieldsSystemAdminUserGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalMetaFieldsSystemAdminUser:
    """FortiAnalyzer endpoint: cli.global._meta_fields.system.admin.user"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalMetaFieldsSystemAdminUserGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        importance: Literal["optional", "required"] | None = None,
        length: int | None = None,
        name: str | None = None,
        status: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalMetaFieldsSystemAdminUser", "CliGlobalMetaFieldsSystemAdminUserGetResponse"]