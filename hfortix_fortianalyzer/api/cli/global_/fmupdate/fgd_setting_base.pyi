"""Type stubs for cli.global.fmupdate.fgd-setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFgdSettingGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFgdSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def as_cache(self) -> int: ...
    @property
    def as_log(self) -> Literal["disable", "nospam", "all"]: ...
    @property
    def as_preload(self) -> Literal["disable", "enable"]: ...
    @property
    def av_cache(self) -> int: ...
    @property
    def av_log(self) -> Literal["disable", "novirus", "all"]: ...
    @property
    def av_preload(self) -> Literal["disable", "enable"]: ...
    @property
    def av2_cache(self) -> int: ...
    @property
    def av2_log(self) -> Literal["disable", "noav2", "all"]: ...
    @property
    def av2_preload(self) -> Literal["disable", "enable"]: ...
    @property
    def delta_ratio(self) -> int: ...
    @property
    def eventlog_query(self) -> Literal["disable", "enable"]: ...
    @property
    def fgd_pull_interval(self) -> int: ...
    @property
    def fq_cache(self) -> int: ...
    @property
    def fq_log(self) -> Literal["disable", "nofilequery", "all"]: ...
    @property
    def fq_preload(self) -> Literal["disable", "enable"]: ...
    @property
    def iot_cache(self) -> int: ...
    @property
    def iot_log(self) -> Literal["disable", "noiot", "all"]: ...
    @property
    def iot_preload(self) -> Literal["disable", "enable"]: ...
    @property
    def iotv_preload(self) -> Literal["disable", "enable"]: ...
    @property
    def linkd_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"]: ...
    @property
    def max_client_worker(self) -> int: ...
    @property
    def max_log_quota(self) -> int: ...
    @property
    def max_unrated_site(self) -> int: ...
    @property
    def restrict_as1_dbver(self) -> str: ...
    @property
    def restrict_as2_dbver(self) -> str: ...
    @property
    def restrict_as4_dbver(self) -> str: ...
    @property
    def restrict_av_dbver(self) -> str: ...
    @property
    def restrict_av2_dbver(self) -> str: ...
    @property
    def restrict_fq_dbver(self) -> str: ...
    @property
    def restrict_iots_dbver(self) -> str: ...
    @property
    def restrict_wf_dbver(self) -> str: ...
    @property
    def server_override(self) -> dict[str, Any]: ...
    @property
    def stat_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"]: ...
    @property
    def stat_log_interval(self) -> int: ...
    @property
    def stat_sync_interval(self) -> int: ...
    @property
    def update_interval(self) -> int: ...
    @property
    def update_log(self) -> Literal["disable", "enable"]: ...
    @property
    def wf_cache(self) -> int: ...
    @property
    def wf_dn_cache_expire_time(self) -> int: ...
    @property
    def wf_dn_cache_max_number(self) -> int: ...
    @property
    def wf_log(self) -> Literal["disable", "nourl", "all"]: ...
    @property
    def wf_preload(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateFgdSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFgdSettingGet endpoint with autocomplete support."""

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
    def as_cache(self) -> int | None:
        """Field: as-cache"""
        ...

    @property
    def as_log(self) -> Literal["disable", "nospam", "all"] | None:
        """Field: as-log"""
        ...

    @property
    def as_preload(self) -> Literal["disable", "enable"] | None:
        """Field: as-preload"""
        ...

    @property
    def av_cache(self) -> int | None:
        """Field: av-cache"""
        ...

    @property
    def av_log(self) -> Literal["disable", "novirus", "all"] | None:
        """Field: av-log"""
        ...

    @property
    def av_preload(self) -> Literal["disable", "enable"] | None:
        """Field: av-preload"""
        ...

    @property
    def av2_cache(self) -> int | None:
        """Field: av2-cache"""
        ...

    @property
    def av2_log(self) -> Literal["disable", "noav2", "all"] | None:
        """Field: av2-log"""
        ...

    @property
    def av2_preload(self) -> Literal["disable", "enable"] | None:
        """Field: av2-preload"""
        ...

    @property
    def delta_ratio(self) -> int | None:
        """Field: delta-ratio"""
        ...

    @property
    def eventlog_query(self) -> Literal["disable", "enable"] | None:
        """Field: eventlog-query"""
        ...

    @property
    def fgd_pull_interval(self) -> int | None:
        """Field: fgd-pull-interval"""
        ...

    @property
    def fq_cache(self) -> int | None:
        """Field: fq-cache"""
        ...

    @property
    def fq_log(self) -> Literal["disable", "nofilequery", "all"] | None:
        """Field: fq-log"""
        ...

    @property
    def fq_preload(self) -> Literal["disable", "enable"] | None:
        """Field: fq-preload"""
        ...

    @property
    def iot_cache(self) -> int | None:
        """Field: iot-cache"""
        ...

    @property
    def iot_log(self) -> Literal["disable", "noiot", "all"] | None:
        """Field: iot-log"""
        ...

    @property
    def iot_preload(self) -> Literal["disable", "enable"] | None:
        """Field: iot-preload"""
        ...

    @property
    def iotv_preload(self) -> Literal["disable", "enable"] | None:
        """Field: iotv-preload"""
        ...

    @property
    def linkd_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None:
        """Field: linkd-log"""
        ...

    @property
    def max_client_worker(self) -> int | None:
        """Field: max-client-worker"""
        ...

    @property
    def max_log_quota(self) -> int | None:
        """Field: max-log-quota"""
        ...

    @property
    def max_unrated_site(self) -> int | None:
        """Field: max-unrated-site"""
        ...

    @property
    def restrict_as1_dbver(self) -> str | None:
        """Field: restrict-as1-dbver"""
        ...

    @property
    def restrict_as2_dbver(self) -> str | None:
        """Field: restrict-as2-dbver"""
        ...

    @property
    def restrict_as4_dbver(self) -> str | None:
        """Field: restrict-as4-dbver"""
        ...

    @property
    def restrict_av_dbver(self) -> str | None:
        """Field: restrict-av-dbver"""
        ...

    @property
    def restrict_av2_dbver(self) -> str | None:
        """Field: restrict-av2-dbver"""
        ...

    @property
    def restrict_fq_dbver(self) -> str | None:
        """Field: restrict-fq-dbver"""
        ...

    @property
    def restrict_iots_dbver(self) -> str | None:
        """Field: restrict-iots-dbver"""
        ...

    @property
    def restrict_wf_dbver(self) -> str | None:
        """Field: restrict-wf-dbver"""
        ...

    @property
    def server_override(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.fmupdate.fgd-setting.server-override)."""
        ...

    @property
    def stat_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None:
        """Field: stat-log"""
        ...

    @property
    def stat_log_interval(self) -> int | None:
        """Field: stat-log-interval"""
        ...

    @property
    def stat_sync_interval(self) -> int | None:
        """Field: stat-sync-interval"""
        ...

    @property
    def update_interval(self) -> int | None:
        """Field: update-interval"""
        ...

    @property
    def update_log(self) -> Literal["disable", "enable"] | None:
        """Field: update-log"""
        ...

    @property
    def wf_cache(self) -> int | None:
        """Field: wf-cache"""
        ...

    @property
    def wf_dn_cache_expire_time(self) -> int | None:
        """Field: wf-dn-cache-expire-time"""
        ...

    @property
    def wf_dn_cache_max_number(self) -> int | None:
        """Field: wf-dn-cache-max-number"""
        ...

    @property
    def wf_log(self) -> Literal["disable", "nourl", "all"] | None:
        """Field: wf-log"""
        ...

    @property
    def wf_preload(self) -> Literal["disable", "enable"] | None:
        """Field: wf-preload"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFgdSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFgdSetting:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fgd-setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFgdSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        as_cache: int | None = None,
        as_log: Literal["disable", "nospam", "all"] | None = None,
        as_preload: Literal["disable", "enable"] | None = None,
        av_cache: int | None = None,
        av_log: Literal["disable", "novirus", "all"] | None = None,
        av_preload: Literal["disable", "enable"] | None = None,
        av2_cache: int | None = None,
        av2_log: Literal["disable", "noav2", "all"] | None = None,
        av2_preload: Literal["disable", "enable"] | None = None,
        delta_ratio: int | None = None,
        eventlog_query: Literal["disable", "enable"] | None = None,
        fgd_pull_interval: int | None = None,
        fq_cache: int | None = None,
        fq_log: Literal["disable", "nofilequery", "all"] | None = None,
        fq_preload: Literal["disable", "enable"] | None = None,
        iot_cache: int | None = None,
        iot_log: Literal["disable", "noiot", "all"] | None = None,
        iot_preload: Literal["disable", "enable"] | None = None,
        iotv_preload: Literal["disable", "enable"] | None = None,
        linkd_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        max_client_worker: int | None = None,
        max_log_quota: int | None = None,
        max_unrated_site: int | None = None,
        restrict_as1_dbver: str | None = None,
        restrict_as2_dbver: str | None = None,
        restrict_as4_dbver: str | None = None,
        restrict_av_dbver: str | None = None,
        restrict_av2_dbver: str | None = None,
        restrict_fq_dbver: str | None = None,
        restrict_iots_dbver: str | None = None,
        restrict_wf_dbver: str | None = None,
        server_override: dict[str, Any] | None = None,
        stat_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        stat_log_interval: int | None = None,
        stat_sync_interval: int | None = None,
        update_interval: int | None = None,
        update_log: Literal["disable", "enable"] | None = None,
        wf_cache: int | None = None,
        wf_dn_cache_expire_time: int | None = None,
        wf_dn_cache_max_number: int | None = None,
        wf_log: Literal["disable", "nourl", "all"] | None = None,
        wf_preload: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        as_cache: int | None = None,
        as_log: Literal["disable", "nospam", "all"] | None = None,
        as_preload: Literal["disable", "enable"] | None = None,
        av_cache: int | None = None,
        av_log: Literal["disable", "novirus", "all"] | None = None,
        av_preload: Literal["disable", "enable"] | None = None,
        av2_cache: int | None = None,
        av2_log: Literal["disable", "noav2", "all"] | None = None,
        av2_preload: Literal["disable", "enable"] | None = None,
        delta_ratio: int | None = None,
        eventlog_query: Literal["disable", "enable"] | None = None,
        fgd_pull_interval: int | None = None,
        fq_cache: int | None = None,
        fq_log: Literal["disable", "nofilequery", "all"] | None = None,
        fq_preload: Literal["disable", "enable"] | None = None,
        iot_cache: int | None = None,
        iot_log: Literal["disable", "noiot", "all"] | None = None,
        iot_preload: Literal["disable", "enable"] | None = None,
        iotv_preload: Literal["disable", "enable"] | None = None,
        linkd_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        max_client_worker: int | None = None,
        max_log_quota: int | None = None,
        max_unrated_site: int | None = None,
        restrict_as1_dbver: str | None = None,
        restrict_as2_dbver: str | None = None,
        restrict_as4_dbver: str | None = None,
        restrict_av_dbver: str | None = None,
        restrict_av2_dbver: str | None = None,
        restrict_fq_dbver: str | None = None,
        restrict_iots_dbver: str | None = None,
        restrict_wf_dbver: str | None = None,
        server_override: dict[str, Any] | None = None,
        stat_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        stat_log_interval: int | None = None,
        stat_sync_interval: int | None = None,
        update_interval: int | None = None,
        update_log: Literal["disable", "enable"] | None = None,
        wf_cache: int | None = None,
        wf_dn_cache_expire_time: int | None = None,
        wf_dn_cache_max_number: int | None = None,
        wf_log: Literal["disable", "nourl", "all"] | None = None,
        wf_preload: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFgdSetting", "CliGlobalFmupdateFgdSettingGetResponse"]