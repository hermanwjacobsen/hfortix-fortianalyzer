"""Type stubs for cli.global.system.connector"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemConnectorGetItem:
    """Item yielded when iterating over CliGlobalSystemConnectorGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def cloud_orchest_refresh_interval(self) -> int: ...
    @property
    def conn_refresh_interval(self) -> int: ...
    @property
    def conn_ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def faznotify_msg_queue_max(self) -> int: ...
    @property
    def faznotify_msg_timeout(self) -> int: ...
    @property
    def fsso_refresh_interval(self) -> int: ...
    @property
    def fsso_sess_timeout(self) -> int: ...
    @property
    def px_svr_timeout(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemConnectorGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemConnectorGet endpoint with autocomplete support."""

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
    def cloud_orchest_refresh_interval(self) -> int | None:
        """Field: cloud-orchest-refresh-interval"""
        ...

    @property
    def conn_refresh_interval(self) -> int | None:
        """Field: conn-refresh-interval"""
        ...

    @property
    def conn_ssl_protocol(self) -> Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: conn-ssl-protocol"""
        ...

    @property
    def faznotify_msg_queue_max(self) -> int | None:
        """Field: faznotify-msg-queue-max"""
        ...

    @property
    def faznotify_msg_timeout(self) -> int | None:
        """Field: faznotify-msg-timeout"""
        ...

    @property
    def fsso_refresh_interval(self) -> int | None:
        """Field: fsso-refresh-interval"""
        ...

    @property
    def fsso_sess_timeout(self) -> int | None:
        """Field: fsso-sess-timeout"""
        ...

    @property
    def px_svr_timeout(self) -> int | None:
        """Field: px-svr-timeout"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemConnectorGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemConnector:
    """FortiAnalyzer endpoint: cli.global.system.connector"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemConnectorGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        cloud_orchest_refresh_interval: int | None = None,
        conn_refresh_interval: int | None = None,
        conn_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        faznotify_msg_queue_max: int | None = None,
        faznotify_msg_timeout: int | None = None,
        fsso_refresh_interval: int | None = None,
        fsso_sess_timeout: int | None = None,
        px_svr_timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        cloud_orchest_refresh_interval: int | None = None,
        conn_refresh_interval: int | None = None,
        conn_ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        faznotify_msg_queue_max: int | None = None,
        faznotify_msg_timeout: int | None = None,
        fsso_refresh_interval: int | None = None,
        fsso_sess_timeout: int | None = None,
        px_svr_timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemConnector", "CliGlobalSystemConnectorGetResponse"]