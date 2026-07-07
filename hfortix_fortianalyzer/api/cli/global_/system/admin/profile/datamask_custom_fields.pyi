"""Type stubs for cli.global.system.admin.profile.datamask-custom-fields"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminProfileDatamaskCustomFieldsGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminProfileDatamaskCustomFieldsGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def field_category(self) -> list[Any]: ...
    @property
    def field_name(self) -> str: ...
    @property
    def field_status(self) -> Literal["disable", "enable"]: ...
    @property
    def field_type(self) -> Literal["string", "ip", "mac", "email", "unknown"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemAdminProfileDatamaskCustomFieldsGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminProfileDatamaskCustomFieldsGet endpoint with autocomplete support."""

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
    def field_category(self) -> list[Any] | None:
        """Field: field-category"""
        ...

    @property
    def field_name(self) -> str | None:
        """Field: field-name"""
        ...

    @property
    def field_status(self) -> Literal["disable", "enable"] | None:
        """Field: field-status"""
        ...

    @property
    def field_type(self) -> Literal["string", "ip", "mac", "email", "unknown"] | None:
        """Field: field-type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminProfileDatamaskCustomFieldsGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminProfileDatamaskCustomFields:
    """FortiAnalyzer endpoint: cli.global.system.admin.profile.datamask-custom-fields"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        profile: str,
        datamask_custom_fields: int | str | None = None,
        fields: list[Literal["field-category", "field-name", "field-status", "field-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminProfileDatamaskCustomFieldsGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        profile: str,
        datamask_custom_fields: int | str | None = None,
        field_category: list[Any] | None = None,
        field_name: str | None = None,
        field_status: Literal["disable", "enable"] | None = None,
        field_type: Literal["string", "ip", "mac", "email", "unknown"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        profile: str,
        datamask_custom_fields: int | str | None = None,
        field_category: list[Any] | None = None,
        field_name: str | None = None,
        field_status: Literal["disable", "enable"] | None = None,
        field_type: Literal["string", "ip", "mac", "email", "unknown"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        profile: str,
        datamask_custom_fields: int | str | None = None,
        field_category: list[Any] | None = None,
        field_name: str | None = None,
        field_status: Literal["disable", "enable"] | None = None,
        field_type: Literal["string", "ip", "mac", "email", "unknown"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        profile: str,
        datamask_custom_fields: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminProfileDatamaskCustomFields", "CliGlobalSystemAdminProfileDatamaskCustomFieldsGetResponse"]