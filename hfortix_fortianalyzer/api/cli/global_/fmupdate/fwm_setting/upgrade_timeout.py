"""
FortiAnalyzer API endpoint: cli.global.fmupdate.fwm-setting.upgrade-timeout

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFwmSettingUpgradeTimeout:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.fwm-setting.upgrade-timeout
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(self) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fwm-setting/upgrade-timeout"
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

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
        total_timeout: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            check_status_timeout: check-status-timeout parameter
            ctrl_check_status_timeout: ctrl-check-status-timeout parameter
            ctrl_put_image_by_fds_timeout: ctrl-put-image-by-fds-timeout parameter
            ha_sync_timeout: ha-sync-timeout parameter
            health_check_timeout: health-check-timeout parameter
            license_check_timeout: license-check-timeout parameter
            prepare_image_timeout: prepare-image-timeout parameter
            put_image_by_fds_timeout: put-image-by-fds-timeout parameter
            put_image_timeout: put-image-timeout parameter
            reboot_of_fsck_timeout: reboot-of-fsck-timeout parameter
            ... (4 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fwm-setting/upgrade-timeout"
        
        # Build data payload
        data = {}
        if check_status_timeout is not None:
            data["check-status-timeout"] = check_status_timeout
        if ctrl_check_status_timeout is not None:
            data["ctrl-check-status-timeout"] = ctrl_check_status_timeout
        if ctrl_put_image_by_fds_timeout is not None:
            data["ctrl-put-image-by-fds-timeout"] = ctrl_put_image_by_fds_timeout
        if ha_sync_timeout is not None:
            data["ha-sync-timeout"] = ha_sync_timeout
        if health_check_timeout is not None:
            data["health-check-timeout"] = health_check_timeout
        if license_check_timeout is not None:
            data["license-check-timeout"] = license_check_timeout
        if prepare_image_timeout is not None:
            data["prepare-image-timeout"] = prepare_image_timeout
        if put_image_by_fds_timeout is not None:
            data["put-image-by-fds-timeout"] = put_image_by_fds_timeout
        if put_image_timeout is not None:
            data["put-image-timeout"] = put_image_timeout
        if reboot_of_fsck_timeout is not None:
            data["reboot-of-fsck-timeout"] = reboot_of_fsck_timeout
        if reboot_of_upgrade_timeout is not None:
            data["reboot-of-upgrade-timeout"] = reboot_of_upgrade_timeout
        if retrieve_timeout is not None:
            data["retrieve-timeout"] = retrieve_timeout
        if rpc_timeout is not None:
            data["rpc-timeout"] = rpc_timeout
        if total_timeout is not None:
            data["total-timeout"] = total_timeout
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

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
        total_timeout: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            check_status_timeout: check-status-timeout parameter
            ctrl_check_status_timeout: ctrl-check-status-timeout parameter
            ctrl_put_image_by_fds_timeout: ctrl-put-image-by-fds-timeout parameter
            ha_sync_timeout: ha-sync-timeout parameter
            health_check_timeout: health-check-timeout parameter
            license_check_timeout: license-check-timeout parameter
            prepare_image_timeout: prepare-image-timeout parameter
            put_image_by_fds_timeout: put-image-by-fds-timeout parameter
            put_image_timeout: put-image-timeout parameter
            reboot_of_fsck_timeout: reboot-of-fsck-timeout parameter
            ... (4 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fwm-setting/upgrade-timeout"
        
        # Build data payload
        data = {}
        if check_status_timeout is not None:
            data["check-status-timeout"] = check_status_timeout
        if ctrl_check_status_timeout is not None:
            data["ctrl-check-status-timeout"] = ctrl_check_status_timeout
        if ctrl_put_image_by_fds_timeout is not None:
            data["ctrl-put-image-by-fds-timeout"] = ctrl_put_image_by_fds_timeout
        if ha_sync_timeout is not None:
            data["ha-sync-timeout"] = ha_sync_timeout
        if health_check_timeout is not None:
            data["health-check-timeout"] = health_check_timeout
        if license_check_timeout is not None:
            data["license-check-timeout"] = license_check_timeout
        if prepare_image_timeout is not None:
            data["prepare-image-timeout"] = prepare_image_timeout
        if put_image_by_fds_timeout is not None:
            data["put-image-by-fds-timeout"] = put_image_by_fds_timeout
        if put_image_timeout is not None:
            data["put-image-timeout"] = put_image_timeout
        if reboot_of_fsck_timeout is not None:
            data["reboot-of-fsck-timeout"] = reboot_of_fsck_timeout
        if reboot_of_upgrade_timeout is not None:
            data["reboot-of-upgrade-timeout"] = reboot_of_upgrade_timeout
        if retrieve_timeout is not None:
            data["retrieve-timeout"] = retrieve_timeout
        if rpc_timeout is not None:
            data["rpc-timeout"] = rpc_timeout
        if total_timeout is not None:
            data["total-timeout"] = total_timeout
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)
