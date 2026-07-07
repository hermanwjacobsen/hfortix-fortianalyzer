"""Type stubs for cli.global.system.ha"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemHaGetItem:
    """Item yielded when iterating over CliGlobalSystemHaGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def cfg_sync_hb_interval(self) -> int: ...
    @property
    def group_id(self) -> int: ...
    @property
    def group_name(self) -> str: ...
    @property
    def hb_interface(self) -> str: ...
    @property
    def hb_interval(self) -> int: ...
    @property
    def healthcheck(self) -> list[Any]: ...
    @property
    def initial_sync(self) -> Literal["disable", "enable"]: ...
    @property
    def initial_sync_threads(self) -> int: ...
    @property
    def load_balance(self) -> Literal["disable", "round-robin"]: ...
    @property
    def local_cert(self) -> str: ...
    @property
    def log_sync(self) -> Literal["disable", "enable"]: ...
    @property
    def mode(self) -> Literal["standalone", "a-p", "a-a"]: ...
    @property
    def password(self) -> list[Any]: ...
    @property
    def peer(self) -> list[PeerItem]: ...
    @property
    def preferred_role(self) -> Literal["secondary", "primary"]: ...
    @property
    def priority(self) -> int: ...
    @property
    def private_clusterid(self) -> int: ...
    @property
    def private_file_quota(self) -> int: ...
    @property
    def private_hb_interval(self) -> int: ...
    @property
    def private_hb_lost_threshold(self) -> int: ...
    @property
    def private_mode(self) -> Literal["standalone", "primary", "secondary"]: ...
    @property
    def private_password(self) -> list[Any]: ...
    @property
    def private_peer(self) -> list[PrivatePeerItem]: ...
    @property
    def unicast(self) -> Literal["disable", "enable"]: ...
    @property
    def vip(self) -> list[VipItem]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class PeerItem:
    """Nested item type for peer array."""

    @property
    def addr(self) -> str: ...
    @property
    def addr_hb(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

class PrivatePeerItem:
    """Nested item type for private-peer array."""

    @property
    def id(self) -> int: ...
    @property
    def ip(self) -> str: ...
    @property
    def ip6(self) -> str: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...

class VipItem:
    """Nested item type for vip array."""

    @property
    def id(self) -> int: ...
    @property
    def status(self) -> Literal["disable", "enable"]: ...
    @property
    def vip(self) -> str: ...
    @property
    def vip_interface(self) -> str: ...


class CliGlobalSystemHaGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemHaGet endpoint with autocomplete support."""

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
    def cfg_sync_hb_interval(self) -> int | None:
        """Field: cfg-sync-hb-interval"""
        ...

    @property
    def group_id(self) -> int | None:
        """Field: group-id"""
        ...

    @property
    def group_name(self) -> str | None:
        """Field: group-name"""
        ...

    @property
    def hb_interface(self) -> str | None:
        """Field: hb-interface"""
        ...

    @property
    def hb_interval(self) -> int | None:
        """Field: hb-interval"""
        ...

    @property
    def healthcheck(self) -> list[Any] | None:
        """Field: healthcheck"""
        ...

    @property
    def initial_sync(self) -> Literal["disable", "enable"] | None:
        """Field: initial-sync"""
        ...

    @property
    def initial_sync_threads(self) -> int | None:
        """Field: initial-sync-threads"""
        ...

    @property
    def load_balance(self) -> Literal["disable", "round-robin"] | None:
        """Field: load-balance"""
        ...

    @property
    def local_cert(self) -> str | None:
        """Field: local-cert"""
        ...

    @property
    def log_sync(self) -> Literal["disable", "enable"] | None:
        """Field: log-sync"""
        ...

    @property
    def mode(self) -> Literal["standalone", "a-p", "a-a"] | None:
        """Field: mode"""
        ...

    @property
    def password(self) -> list[Any] | None:
        """Field: password"""
        ...

    @property
    def peer(self) -> list[PeerItem]:
        """Field: peer"""
        ...

    @property
    def preferred_role(self) -> Literal["secondary", "primary"] | None:
        """Field: preferred-role"""
        ...

    @property
    def priority(self) -> int | None:
        """Field: priority"""
        ...

    @property
    def private_clusterid(self) -> int | None:
        """Field: private-clusterid"""
        ...

    @property
    def private_file_quota(self) -> int | None:
        """Field: private-file-quota"""
        ...

    @property
    def private_hb_interval(self) -> int | None:
        """Field: private-hb-interval"""
        ...

    @property
    def private_hb_lost_threshold(self) -> int | None:
        """Field: private-hb-lost-threshold"""
        ...

    @property
    def private_mode(self) -> Literal["standalone", "primary", "secondary"] | None:
        """Field: private-mode"""
        ...

    @property
    def private_password(self) -> list[Any] | None:
        """Field: private-password"""
        ...

    @property
    def private_peer(self) -> list[PrivatePeerItem]:
        """Field: private-peer"""
        ...

    @property
    def unicast(self) -> Literal["disable", "enable"] | None:
        """Field: unicast"""
        ...

    @property
    def vip(self) -> list[VipItem]:
        """Field: vip"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemHaGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemHa:
    """FortiAnalyzer endpoint: cli.global.system.ha"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemHaGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        cfg_sync_hb_interval: int | None = None,
        group_id: int | None = None,
        group_name: str | None = None,
        hb_interface: str | None = None,
        hb_interval: int | None = None,
        healthcheck: list[Any] | None = None,
        initial_sync: Literal["disable", "enable"] | None = None,
        initial_sync_threads: int | None = None,
        load_balance: Literal["disable", "round-robin"] | None = None,
        local_cert: str | None = None,
        log_sync: Literal["disable", "enable"] | None = None,
        mode: Literal["standalone", "a-p", "a-a"] | None = None,
        password: list[Any] | None = None,
        peer: list[dict[str, Any]] | None = None,
        preferred_role: Literal["secondary", "primary"] | None = None,
        priority: int | None = None,
        private_clusterid: int | None = None,
        private_file_quota: int | None = None,
        private_hb_interval: int | None = None,
        private_hb_lost_threshold: int | None = None,
        private_mode: Literal["standalone", "primary", "secondary"] | None = None,
        private_password: list[Any] | None = None,
        private_peer: list[dict[str, Any]] | None = None,
        unicast: Literal["disable", "enable"] | None = None,
        vip: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        cfg_sync_hb_interval: int | None = None,
        group_id: int | None = None,
        group_name: str | None = None,
        hb_interface: str | None = None,
        hb_interval: int | None = None,
        healthcheck: list[Any] | None = None,
        initial_sync: Literal["disable", "enable"] | None = None,
        initial_sync_threads: int | None = None,
        load_balance: Literal["disable", "round-robin"] | None = None,
        local_cert: str | None = None,
        log_sync: Literal["disable", "enable"] | None = None,
        mode: Literal["standalone", "a-p", "a-a"] | None = None,
        password: list[Any] | None = None,
        peer: list[dict[str, Any]] | None = None,
        preferred_role: Literal["secondary", "primary"] | None = None,
        priority: int | None = None,
        private_clusterid: int | None = None,
        private_file_quota: int | None = None,
        private_hb_interval: int | None = None,
        private_hb_lost_threshold: int | None = None,
        private_mode: Literal["standalone", "primary", "secondary"] | None = None,
        private_password: list[Any] | None = None,
        private_peer: list[dict[str, Any]] | None = None,
        unicast: Literal["disable", "enable"] | None = None,
        vip: list[dict[str, Any]] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemHa", "CliGlobalSystemHaGetResponse"]