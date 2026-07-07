"""Type stubs for cli.global.fmupdate.fwm-setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFwmSettingGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFwmSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def auto_scan_fgt_disk(self) -> Literal["disable", "enable"]: ...
    @property
    def check_fgt_disk(self) -> Literal["disable", "enable"]: ...
    @property
    def fds_failover_fmg(self) -> Literal["disable", "enable"]: ...
    @property
    def fds_image_timeout(self) -> int: ...
    @property
    def health_check(self) -> Literal["disable", "enable"]: ...
    @property
    def immx_source(self) -> Literal["fmg", "fgt", "cloud"]: ...
    @property
    def log(self) -> Literal["fwm", "fwm_dm", "fwm_dm_json"]: ...
    @property
    def max_device_history(self) -> int: ...
    @property
    def max_profile_history(self) -> int: ...
    @property
    def multiple_steps_interval(self) -> int: ...
    @property
    def retrieve(self) -> Literal["disable", "enable"]: ...
    @property
    def retry_interval(self) -> int: ...
    @property
    def retry_max(self) -> int: ...
    @property
    def revision_diff(self) -> Literal["disable", "enable"]: ...
    @property
    def send_image_retry(self) -> int: ...
    @property
    def upgrade_timeout(self) -> dict[str, Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateFwmSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFwmSettingGet endpoint with autocomplete support."""

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
    def auto_scan_fgt_disk(self) -> Literal["disable", "enable"] | None:
        """Field: auto-scan-fgt-disk"""
        ...

    @property
    def check_fgt_disk(self) -> Literal["disable", "enable"] | None:
        """Field: check-fgt-disk"""
        ...

    @property
    def fds_failover_fmg(self) -> Literal["disable", "enable"] | None:
        """Field: fds-failover-fmg"""
        ...

    @property
    def fds_image_timeout(self) -> int | None:
        """Field: fds-image-timeout"""
        ...

    @property
    def health_check(self) -> Literal["disable", "enable"] | None:
        """Field: health-check"""
        ...

    @property
    def immx_source(self) -> Literal["fmg", "fgt", "cloud"] | None:
        """Field: immx-source"""
        ...

    @property
    def log(self) -> Literal["fwm", "fwm_dm", "fwm_dm_json"] | None:
        """Field: log"""
        ...

    @property
    def max_device_history(self) -> int | None:
        """Field: max-device-history"""
        ...

    @property
    def max_profile_history(self) -> int | None:
        """Field: max-profile-history"""
        ...

    @property
    def multiple_steps_interval(self) -> int | None:
        """Field: multiple-steps-interval"""
        ...

    @property
    def retrieve(self) -> Literal["disable", "enable"] | None:
        """Field: retrieve"""
        ...

    @property
    def retry_interval(self) -> int | None:
        """Field: retry-interval"""
        ...

    @property
    def retry_max(self) -> int | None:
        """Field: retry-max"""
        ...

    @property
    def revision_diff(self) -> Literal["disable", "enable"] | None:
        """Field: revision-diff"""
        ...

    @property
    def send_image_retry(self) -> int | None:
        """Field: send-image-retry"""
        ...

    @property
    def upgrade_timeout(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.fmupdate.fwm-setting.upgrade-timeout)."""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFwmSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFwmSetting:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fwm-setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFwmSettingGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        auto_scan_fgt_disk: Literal["disable", "enable"] | None = None,
        check_fgt_disk: Literal["disable", "enable"] | None = None,
        fds_failover_fmg: Literal["disable", "enable"] | None = None,
        fds_image_timeout: int | None = None,
        health_check: Literal["disable", "enable"] | None = None,
        immx_source: Literal["fmg", "fgt", "cloud"] | None = None,
        log: Literal["fwm", "fwm_dm", "fwm_dm_json"] | None = None,
        max_device_history: int | None = None,
        max_profile_history: int | None = None,
        multiple_steps_interval: int | None = None,
        retrieve: Literal["disable", "enable"] | None = None,
        retry_interval: int | None = None,
        retry_max: int | None = None,
        revision_diff: Literal["disable", "enable"] | None = None,
        send_image_retry: int | None = None,
        upgrade_timeout: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        auto_scan_fgt_disk: Literal["disable", "enable"] | None = None,
        check_fgt_disk: Literal["disable", "enable"] | None = None,
        fds_failover_fmg: Literal["disable", "enable"] | None = None,
        fds_image_timeout: int | None = None,
        health_check: Literal["disable", "enable"] | None = None,
        immx_source: Literal["fmg", "fgt", "cloud"] | None = None,
        log: Literal["fwm", "fwm_dm", "fwm_dm_json"] | None = None,
        max_device_history: int | None = None,
        max_profile_history: int | None = None,
        multiple_steps_interval: int | None = None,
        retrieve: Literal["disable", "enable"] | None = None,
        retry_interval: int | None = None,
        retry_max: int | None = None,
        revision_diff: Literal["disable", "enable"] | None = None,
        send_image_retry: int | None = None,
        upgrade_timeout: dict[str, Any] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFwmSetting", "CliGlobalFmupdateFwmSettingGetResponse"]