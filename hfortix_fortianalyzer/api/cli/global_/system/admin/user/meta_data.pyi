"""Type stubs for cli.global.system.admin.user.meta-data"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUserMetaDataGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminUserMetaDataGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def fieldlength(self) -> int: ...
    @property
    def fieldname(self) -> str: ...
    @property
    def fieldvalue(self) -> str: ...
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


class CliGlobalSystemAdminUserMetaDataGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminUserMetaDataGet endpoint with autocomplete support."""

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
    def fieldlength(self) -> int | None:
        """Field: fieldlength"""
        ...

    @property
    def fieldname(self) -> str | None:
        """Field: fieldname"""
        ...

    @property
    def fieldvalue(self) -> str | None:
        """Field: fieldvalue"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminUserMetaDataGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminUserMetaData:
    """FortiAnalyzer endpoint: cli.global.system.admin.user.meta-data"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        user: str,
        meta_data: int | str | None = None,
        fields: list[Literal["fieldlength", "fieldname", "fieldvalue", "importance", "status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminUserMetaDataGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        user: str,
        meta_data: int | str | None = None,
        fieldlength: int | None = None,
        fieldname: str | None = None,
        fieldvalue: str | None = None,
        importance: Literal["optional", "required"] | None = None,
        status: Literal["disabled", "enabled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        user: str,
        meta_data: int | str | None = None,
        fieldlength: int | None = None,
        fieldname: str | None = None,
        fieldvalue: str | None = None,
        importance: Literal["optional", "required"] | None = None,
        status: Literal["disabled", "enabled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        user: str,
        meta_data: int | str | None = None,
        fieldlength: int | None = None,
        fieldname: str | None = None,
        fieldvalue: str | None = None,
        importance: Literal["optional", "required"] | None = None,
        status: Literal["disabled", "enabled"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        user: str,
        meta_data: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminUserMetaData", "CliGlobalSystemAdminUserMetaDataGetResponse"]