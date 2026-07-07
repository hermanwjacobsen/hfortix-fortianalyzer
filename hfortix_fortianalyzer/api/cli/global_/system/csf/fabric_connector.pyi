"""Type stubs for cli.global.system.csf.fabric-connector"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCsfFabricConnectorGetItem:
    """Item yielded when iterating over CliGlobalSystemCsfFabricConnectorGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def accprofile(self) -> str: ...
    @property
    def configuration_write_access(self) -> Literal["disable", "enable"]: ...
    @property
    def serial(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemCsfFabricConnectorGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCsfFabricConnectorGet endpoint with autocomplete support."""

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
    def accprofile(self) -> str | None:
        """Field: accprofile"""
        ...

    @property
    def configuration_write_access(self) -> Literal["disable", "enable"] | None:
        """Field: configuration-write-access"""
        ...

    @property
    def serial(self) -> str | None:
        """Field: serial"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCsfFabricConnectorGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCsfFabricConnector:
    """FortiAnalyzer endpoint: cli.global.system.csf.fabric-connector"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        fabric_connector: int | str | None = None,
        fields: list[Literal["accprofile", "configuration-write-access", "serial"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemCsfFabricConnectorGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        fabric_connector: int | str | None = None,
        accprofile: str | None = None,
        configuration_write_access: Literal["disable", "enable"] | None = None,
        serial: str | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        fabric_connector: int | str | None = None,
        accprofile: str | None = None,
        configuration_write_access: Literal["disable", "enable"] | None = None,
        serial: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        fabric_connector: int | str | None = None,
        accprofile: str | None = None,
        configuration_write_access: Literal["disable", "enable"] | None = None,
        serial: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        fabric_connector: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemCsfFabricConnector", "CliGlobalSystemCsfFabricConnectorGetResponse"]