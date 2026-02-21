"""Type stubs for dvmdb.adom"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomAddResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbAdom endpoint with autocomplete support."""

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
    def name(self) -> str | None:
        """Field: name"""
        ...

    class DvmdbAdomItem:
        """Item yielded when iterating over DvmdbAdomResponse."""

        @property
        def name(self) -> str: ...

        # Inherited from FortiAnalyzerObject
        @property
        def raw(self) -> dict[str, Any]: ...
        @property
        def dict(self) -> dict[str, Any]: ...
        @property
        def json(self) -> str: ...
        def __getitem__(self, key: str) -> Any: ...

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
    def __iter__(self) -> Iterator[DvmdbAdomItem]: ...
    def __len__(self) -> int: ...


class DvmdbAdomGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbAdom endpoint with autocomplete support."""

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
    def create_time(self) -> int | None:
        """Field: create_time"""
        ...

    @property
    def desc(self) -> str | None:
        """Field: desc"""
        ...

    @property
    def flags(self) -> list[Any] | None:
        """Field: flags"""
        ...

    @property
    def lock_override(self) -> int | None:
        """Field: lock_override"""
        ...

    @property
    def log_db_retention_hours(self) -> int | None:
        """Field: log_db_retention_hours"""
        ...

    @property
    def log_disk_quota(self) -> int | None:
        """Field: log_disk_quota"""
        ...

    @property
    def log_disk_quota_alert_thres(self) -> int | None:
        """Field: log_disk_quota_alert_thres"""
        ...

    @property
    def log_disk_quota_split_ratio(self) -> int | None:
        """Field: log_disk_quota_split_ratio"""
        ...

    @property
    def log_file_retention_hours(self) -> int | None:
        """Field: log_file_retention_hours"""
        ...

    @property
    def meta_fields(self) -> dict[str, Any] | None:
        """Default metafields: none."""
        ...

    @property
    def mig_mr(self) -> int | None:
        """Field: mig_mr"""
        ...

    @property
    def mig_os_ver(self) -> Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None:
        """Field: mig_os_ver"""
        ...

    @property
    def mode(self) -> Literal["ems", "gms", "provider"] | None:
        """<b>ems</b> - (Value no longer used as of 4.3)<br/><b>provider</b> - Global da..."""
        ...

    @property
    def mr(self) -> int | None:
        """Field: mr"""
        ...

    @property
    def name(self) -> str | None:
        """Field: name"""
        ...

    @property
    def os_ver(self) -> Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None:
        """Field: os_ver"""
        ...

    @property
    def primary_dns_ip4(self) -> str | None:
        """Field: primary_dns_ip4"""
        ...

    @property
    def primary_dns_ip6_1(self) -> int | None:
        """Field: primary_dns_ip6_1"""
        ...

    @property
    def primary_dns_ip6_2(self) -> int | None:
        """Field: primary_dns_ip6_2"""
        ...

    @property
    def primary_dns_ip6_3(self) -> int | None:
        """Field: primary_dns_ip6_3"""
        ...

    @property
    def primary_dns_ip6_4(self) -> int | None:
        """Field: primary_dns_ip6_4"""
        ...

    @property
    def restricted_prds(self) -> Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None:
        """Field: restricted_prds"""
        ...

    @property
    def secondary_dns_ip4(self) -> str | None:
        """Field: secondary_dns_ip4"""
        ...

    @property
    def secondary_dns_ip6_1(self) -> int | None:
        """Field: secondary_dns_ip6_1"""
        ...

    @property
    def secondary_dns_ip6_2(self) -> int | None:
        """Field: secondary_dns_ip6_2"""
        ...

    @property
    def secondary_dns_ip6_3(self) -> int | None:
        """Field: secondary_dns_ip6_3"""
        ...

    @property
    def secondary_dns_ip6_4(self) -> int | None:
        """Field: secondary_dns_ip6_4"""
        ...

    @property
    def state(self) -> int | None:
        """Field: state"""
        ...

    @property
    def tz(self) -> int | None:
        """Field: tz"""
        ...

    @property
    def uuid(self) -> str | None:
        """Field: uuid"""
        ...

    @property
    def workspace_mode(self) -> int | None:
        """Field: workspace_mode"""
        ...

    class DvmdbAdomItem:
        """Item yielded when iterating over DvmdbAdomResponse."""

        @property
        def oid(self) -> int: ...
        @property
        def create_time(self) -> int: ...
        @property
        def desc(self) -> str: ...
        @property
        def flags(self) -> list[Any]: ...
        @property
        def lock_override(self) -> int: ...
        @property
        def log_db_retention_hours(self) -> int: ...
        @property
        def log_disk_quota(self) -> int: ...
        @property
        def log_disk_quota_alert_thres(self) -> int: ...
        @property
        def log_disk_quota_split_ratio(self) -> int: ...
        @property
        def log_file_retention_hours(self) -> int: ...
        @property
        def meta_fields(self) -> dict[str, Any]: ...
        @property
        def mig_mr(self) -> int: ...
        @property
        def mig_os_ver(self) -> Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"]: ...
        @property
        def mode(self) -> Literal["ems", "gms", "provider"]: ...
        @property
        def mr(self) -> int: ...
        @property
        def name(self) -> str: ...
        @property
        def os_ver(self) -> Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"]: ...
        @property
        def primary_dns_ip4(self) -> str: ...
        @property
        def primary_dns_ip6_1(self) -> int: ...
        @property
        def primary_dns_ip6_2(self) -> int: ...
        @property
        def primary_dns_ip6_3(self) -> int: ...
        @property
        def primary_dns_ip6_4(self) -> int: ...
        @property
        def restricted_prds(self) -> Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"]: ...
        @property
        def secondary_dns_ip4(self) -> str: ...
        @property
        def secondary_dns_ip6_1(self) -> int: ...
        @property
        def secondary_dns_ip6_2(self) -> int: ...
        @property
        def secondary_dns_ip6_3(self) -> int: ...
        @property
        def secondary_dns_ip6_4(self) -> int: ...
        @property
        def state(self) -> int: ...
        @property
        def tz(self) -> int: ...
        @property
        def uuid(self) -> str: ...
        @property
        def workspace_mode(self) -> int: ...

        # Inherited from FortiAnalyzerObject
        @property
        def raw(self) -> dict[str, Any]: ...
        @property
        def dict(self) -> dict[str, Any]: ...
        @property
        def json(self) -> str: ...
        def __getitem__(self, key: str) -> Any: ...

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
    def __iter__(self) -> Iterator[DvmdbAdomItem]: ...
    def __len__(self) -> int: ...



class DvmdbAdom:
    """FortiAnalyzer endpoint: dvmdb.adom"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None,
    ) -> DvmdbAdomAddResponse:
        """ADD operation."""
        ...

    def get(
        self,
        expand_member: str | None = None,
        fields: list[Literal["create_time", "desc", "flags", "lock_override", "log_db_retention_hours", "log_disk_quota", "log_disk_quota_alert_thres", "log_disk_quota_split_ratio", "log_file_retention_hours", "mig_mr", "mig_os_ver", "mode", "mr", "name", "os_ver", "primary_dns_ip4", "primary_dns_ip6_1", "primary_dns_ip6_2", "primary_dns_ip6_3", "primary_dns_ip6_4", "restricted_prds", "secondary_dns_ip4", "secondary_dns_ip6_1", "secondary_dns_ip6_2", "secondary_dns_ip6_3", "secondary_dns_ip6_4", "state", "tz", "uuid", "workspace_mode"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        meta_fields: list[str] | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbAdomGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None,
    ) -> DvmdbAdomAddResponse:
        """SET operation."""
        ...

    def update(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None,
    ) -> DvmdbAdomAddResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["DvmdbAdom", "DvmdbAdomAddResponse", "DvmdbAdomGetResponse"]