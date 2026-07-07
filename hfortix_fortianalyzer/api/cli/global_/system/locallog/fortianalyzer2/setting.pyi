"""Type stubs for cli.global.system.locallog.fortianalyzer2.setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogFortianalyzer2SettingGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogFortianalyzer2SettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def peer_cert_cn(self) -> str: ...
    @property
    def reliable(self) -> Literal["disable", "enable"]: ...
    @property
    def secure_connection(self) -> Literal["enable"]: ...
    @property
    def server(self) -> str: ...
    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"]: ...
    @property
    def status(self) -> Literal["disable", "realtime", "upload"]: ...
    @property
    def upload_time(self) -> str: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogFortianalyzer2SettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogFortianalyzer2SettingGet endpoint with autocomplete support."""

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
    def peer_cert_cn(self) -> str | None:
        """Field: peer-cert-cn"""
        ...

    @property
    def reliable(self) -> Literal["disable", "enable"] | None:
        """Field: reliable"""
        ...

    @property
    def secure_connection(self) -> Literal["enable"] | None:
        """Field: secure-connection"""
        ...

    @property
    def server(self) -> str | None:
        """Field: server"""
        ...

    @property
    def severity(self) -> Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None:
        """Field: severity"""
        ...

    @property
    def status(self) -> Literal["disable", "realtime", "upload"] | None:
        """Field: status"""
        ...

    @property
    def upload_time(self) -> str | None:
        """Field: upload-time"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogFortianalyzer2SettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogFortianalyzer2Setting:
    """FortiAnalyzer endpoint: cli.global.system.locallog.fortianalyzer2.setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogFortianalyzer2SettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        peer_cert_cn: str | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["enable"] | None = None,
        server: str | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "realtime", "upload"] | None = None,
        upload_time: str | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        peer_cert_cn: str | None = None,
        reliable: Literal["disable", "enable"] | None = None,
        secure_connection: Literal["enable"] | None = None,
        server: str | None = None,
        severity: Literal["emergency", "alert", "critical", "error", "warning", "notification", "information", "debug"] | None = None,
        status: Literal["disable", "realtime", "upload"] | None = None,
        upload_time: str | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogFortianalyzer2Setting", "CliGlobalSystemLocallogFortianalyzer2SettingGetResponse"]