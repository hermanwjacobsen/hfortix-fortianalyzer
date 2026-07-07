"""Type stubs for cli.global.system.csf"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCsfGetItem:
    """Item yielded when iterating over CliGlobalSystemCsfGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def accept_auth_by_cert(self) -> Literal["disable", "enable"]: ...
    @property
    def authorization_request_type(self) -> Literal["certificate", "serial"]: ...
    @property
    def certificate(self) -> str: ...
    @property
    def downstream_access(self) -> Literal["disable", "enable"]: ...
    @property
    def downstream_accprofile(self) -> str: ...
    @property
    def fabric_connector(self) -> list[FabricConnectorItem]: ...
    @property
    def fabric_workers(self) -> int: ...
    @property
    def fixed_key(self) -> list[Any]: ...
    @property
    def forticloud_account_enforcement(self) -> Literal["disable", "enable"]: ...
    @property
    def group_name(self) -> str: ...
    @property
    def group_password(self) -> list[Any]: ...
    @property
    def log_unification(self) -> Literal["disable", "enable"]: ...
    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def trusted_list(self) -> list[TrustedListItem]: ...
    @property
    def upstream(self) -> str: ...
    @property
    def upstream_confirm(self) -> Literal["discover", "confirm"]: ...
    @property
    def upstream_port(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class FabricConnectorItem:
    """Nested item type for fabric-connector array."""

    @property
    def accprofile(self) -> str: ...
    @property
    def configuration_write_access(self) -> Literal["disable", "enable"]: ...
    @property
    def serial(self) -> str: ...

class TrustedListItem:
    """Nested item type for trusted-list array."""

    @property
    def action(self) -> Literal["accept", "deny"]: ...
    @property
    def adom(self) -> list[AdomItem]: ...
    @property
    def adom_access(self) -> Literal["all", "specify"]: ...
    @property
    def authorization_type(self) -> Literal["serial", "certificate"]: ...
    @property
    def certificate(self) -> str: ...
    @property
    def downstream_authorization(self) -> Literal["disable", "enable"]: ...
    @property
    def ha_members(self) -> str: ...
    @property
    def index(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def serial(self) -> str: ...


class CliGlobalSystemCsfGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemCsfGet endpoint with autocomplete support."""

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
    def accept_auth_by_cert(self) -> Literal["disable", "enable"] | None:
        """Field: accept-auth-by-cert"""
        ...

    @property
    def authorization_request_type(self) -> Literal["certificate", "serial"] | None:
        """Field: authorization-request-type"""
        ...

    @property
    def certificate(self) -> str | None:
        """Field: certificate"""
        ...

    @property
    def downstream_access(self) -> Literal["disable", "enable"] | None:
        """Field: downstream-access"""
        ...

    @property
    def downstream_accprofile(self) -> str | None:
        """Field: downstream-accprofile"""
        ...

    @property
    def fabric_connector(self) -> list[FabricConnectorItem]:
        """Field: fabric-connector"""
        ...

    @property
    def fabric_workers(self) -> int | None:
        """Field: fabric-workers"""
        ...

    @property
    def fixed_key(self) -> list[Any] | None:
        """Field: fixed-key"""
        ...

    @property
    def forticloud_account_enforcement(self) -> Literal["disable", "enable"] | None:
        """Field: forticloud-account-enforcement"""
        ...

    @property
    def group_name(self) -> str | None:
        """Field: group-name"""
        ...

    @property
    def group_password(self) -> list[Any] | None:
        """Field: group-password"""
        ...

    @property
    def log_unification(self) -> Literal["disable", "enable"] | None:
        """Field: log-unification"""
        ...

    @property
    def ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: ssl-protocol"""
        ...

    @property
    def status(self) -> Literal["disable", "enable"] | None:
        """Field: status"""
        ...

    @property
    def trusted_list(self) -> list[TrustedListItem]:
        """Field: trusted-list"""
        ...

    @property
    def upstream(self) -> str | None:
        """Field: upstream"""
        ...

    @property
    def upstream_confirm(self) -> Literal["discover", "confirm"] | None:
        """Field: upstream-confirm"""
        ...

    @property
    def upstream_port(self) -> int | None:
        """Field: upstream-port"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemCsfGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemCsf:
    """FortiAnalyzer endpoint: cli.global.system.csf"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemCsfGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        accept_auth_by_cert: Literal["disable", "enable"] | None = None,
        authorization_request_type: Literal["certificate", "serial"] | None = None,
        certificate: str | None = None,
        downstream_access: Literal["disable", "enable"] | None = None,
        downstream_accprofile: str | None = None,
        fabric_connector: list[dict[str, Any]] | None = None,
        fabric_workers: int | None = None,
        fixed_key: list[Any] | None = None,
        forticloud_account_enforcement: Literal["disable", "enable"] | None = None,
        group_name: str | None = None,
        group_password: list[Any] | None = None,
        log_unification: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trusted_list: list[dict[str, Any]] | None = None,
        upstream: str | None = None,
        upstream_confirm: Literal["discover", "confirm"] | None = None,
        upstream_port: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        accept_auth_by_cert: Literal["disable", "enable"] | None = None,
        authorization_request_type: Literal["certificate", "serial"] | None = None,
        certificate: str | None = None,
        downstream_access: Literal["disable", "enable"] | None = None,
        downstream_accprofile: str | None = None,
        fabric_connector: list[dict[str, Any]] | None = None,
        fabric_workers: int | None = None,
        fixed_key: list[Any] | None = None,
        forticloud_account_enforcement: Literal["disable", "enable"] | None = None,
        group_name: str | None = None,
        group_password: list[Any] | None = None,
        log_unification: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        trusted_list: list[dict[str, Any]] | None = None,
        upstream: str | None = None,
        upstream_confirm: Literal["discover", "confirm"] | None = None,
        upstream_port: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemCsf", "CliGlobalSystemCsfGetResponse"]