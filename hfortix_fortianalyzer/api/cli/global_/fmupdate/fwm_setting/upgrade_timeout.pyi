"""Type stubs for cli.global.fmupdate.fwm-setting.upgrade-timeout"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFwmSettingUpgradeTimeoutGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFwmSettingUpgradeTimeoutGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def check_status_timeout(self) -> int: ...
    @property
    def ctrl_check_status_timeout(self) -> int: ...
    @property
    def ctrl_put_image_by_fds_timeout(self) -> int: ...
    @property
    def ha_sync_timeout(self) -> int: ...
    @property
    def health_check_timeout(self) -> int: ...
    @property
    def license_check_timeout(self) -> int: ...
    @property
    def prepare_image_timeout(self) -> int: ...
    @property
    def put_image_by_fds_timeout(self) -> int: ...
    @property
    def put_image_timeout(self) -> int: ...
    @property
    def reboot_of_fsck_timeout(self) -> int: ...
    @property
    def reboot_of_upgrade_timeout(self) -> int: ...
    @property
    def retrieve_timeout(self) -> int: ...
    @property
    def rpc_timeout(self) -> int: ...
    @property
    def total_timeout(self) -> int: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateFwmSettingUpgradeTimeoutGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFwmSettingUpgradeTimeoutGet endpoint with autocomplete support."""

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
    def check_status_timeout(self) -> int | None:
        """Field: check-status-timeout"""
        ...

    @property
    def ctrl_check_status_timeout(self) -> int | None:
        """Field: ctrl-check-status-timeout"""
        ...

    @property
    def ctrl_put_image_by_fds_timeout(self) -> int | None:
        """Field: ctrl-put-image-by-fds-timeout"""
        ...

    @property
    def ha_sync_timeout(self) -> int | None:
        """Field: ha-sync-timeout"""
        ...

    @property
    def health_check_timeout(self) -> int | None:
        """Field: health-check-timeout"""
        ...

    @property
    def license_check_timeout(self) -> int | None:
        """Field: license-check-timeout"""
        ...

    @property
    def prepare_image_timeout(self) -> int | None:
        """Field: prepare-image-timeout"""
        ...

    @property
    def put_image_by_fds_timeout(self) -> int | None:
        """Field: put-image-by-fds-timeout"""
        ...

    @property
    def put_image_timeout(self) -> int | None:
        """Field: put-image-timeout"""
        ...

    @property
    def reboot_of_fsck_timeout(self) -> int | None:
        """Field: reboot-of-fsck-timeout"""
        ...

    @property
    def reboot_of_upgrade_timeout(self) -> int | None:
        """Field: reboot-of-upgrade-timeout"""
        ...

    @property
    def retrieve_timeout(self) -> int | None:
        """Field: retrieve-timeout"""
        ...

    @property
    def rpc_timeout(self) -> int | None:
        """Field: rpc-timeout"""
        ...

    @property
    def total_timeout(self) -> int | None:
        """Field: total-timeout"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFwmSettingUpgradeTimeoutGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFwmSettingUpgradeTimeout:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fwm-setting.upgrade-timeout"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFwmSettingUpgradeTimeoutGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        check_status_timeout: int | None = None,
        ctrl_check_status_timeout: int | None = None,
        ctrl_put_image_by_fds_timeout: int | None = None,
        ha_sync_timeout: int | None = None,
        health_check_timeout: int | None = None,
        license_check_timeout: int | None = None,
        prepare_image_timeout: int | None = None,
        put_image_by_fds_timeout: int | None = None,
        put_image_timeout: int | None = None,
        reboot_of_fsck_timeout: int | None = None,
        reboot_of_upgrade_timeout: int | None = None,
        retrieve_timeout: int | None = None,
        rpc_timeout: int | None = None,
        total_timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        check_status_timeout: int | None = None,
        ctrl_check_status_timeout: int | None = None,
        ctrl_put_image_by_fds_timeout: int | None = None,
        ha_sync_timeout: int | None = None,
        health_check_timeout: int | None = None,
        license_check_timeout: int | None = None,
        prepare_image_timeout: int | None = None,
        put_image_by_fds_timeout: int | None = None,
        put_image_timeout: int | None = None,
        reboot_of_fsck_timeout: int | None = None,
        reboot_of_upgrade_timeout: int | None = None,
        retrieve_timeout: int | None = None,
        rpc_timeout: int | None = None,
        total_timeout: int | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFwmSettingUpgradeTimeout", "CliGlobalFmupdateFwmSettingUpgradeTimeoutGetResponse"]