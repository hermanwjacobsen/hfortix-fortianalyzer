"""
FortiAnalyzer API endpoint: cli.global.fmupdate.fwm-setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFwmSetting:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.fwm-setting
    
    
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
        url = "/cli/global/fmupdate/fwm-setting"
        
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
        upgrade_timeout: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            auto_scan_fgt_disk: auto-scan-fgt-disk parameter
            check_fgt_disk: check-fgt-disk parameter
            fds_failover_fmg: fds-failover-fmg parameter
            fds_image_timeout: fds-image-timeout parameter
            health_check: health-check parameter
            immx_source: immx-source parameter
            log: log parameter
            max_device_history: max-device-history parameter
            max_profile_history: max-profile-history parameter
            multiple_steps_interval: multiple-steps-interval parameter
            ... (6 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fwm-setting"
        
        # Build data payload
        data = {}
        if auto_scan_fgt_disk is not None:
            data["auto-scan-fgt-disk"] = auto_scan_fgt_disk
        if check_fgt_disk is not None:
            data["check-fgt-disk"] = check_fgt_disk
        if fds_failover_fmg is not None:
            data["fds-failover-fmg"] = fds_failover_fmg
        if fds_image_timeout is not None:
            data["fds-image-timeout"] = fds_image_timeout
        if health_check is not None:
            data["health-check"] = health_check
        if immx_source is not None:
            data["immx-source"] = immx_source
        if log is not None:
            data["log"] = log
        if max_device_history is not None:
            data["max-device-history"] = max_device_history
        if max_profile_history is not None:
            data["max-profile-history"] = max_profile_history
        if multiple_steps_interval is not None:
            data["multiple-steps-interval"] = multiple_steps_interval
        if retrieve is not None:
            data["retrieve"] = retrieve
        if retry_interval is not None:
            data["retry-interval"] = retry_interval
        if retry_max is not None:
            data["retry-max"] = retry_max
        if revision_diff is not None:
            data["revision-diff"] = revision_diff
        if send_image_retry is not None:
            data["send-image-retry"] = send_image_retry
        if upgrade_timeout is not None:
            data["upgrade-timeout"] = upgrade_timeout
        
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
        upgrade_timeout: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            auto_scan_fgt_disk: auto-scan-fgt-disk parameter
            check_fgt_disk: check-fgt-disk parameter
            fds_failover_fmg: fds-failover-fmg parameter
            fds_image_timeout: fds-image-timeout parameter
            health_check: health-check parameter
            immx_source: immx-source parameter
            log: log parameter
            max_device_history: max-device-history parameter
            max_profile_history: max-profile-history parameter
            multiple_steps_interval: multiple-steps-interval parameter
            ... (6 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fwm-setting"
        
        # Build data payload
        data = {}
        if auto_scan_fgt_disk is not None:
            data["auto-scan-fgt-disk"] = auto_scan_fgt_disk
        if check_fgt_disk is not None:
            data["check-fgt-disk"] = check_fgt_disk
        if fds_failover_fmg is not None:
            data["fds-failover-fmg"] = fds_failover_fmg
        if fds_image_timeout is not None:
            data["fds-image-timeout"] = fds_image_timeout
        if health_check is not None:
            data["health-check"] = health_check
        if immx_source is not None:
            data["immx-source"] = immx_source
        if log is not None:
            data["log"] = log
        if max_device_history is not None:
            data["max-device-history"] = max_device_history
        if max_profile_history is not None:
            data["max-profile-history"] = max_profile_history
        if multiple_steps_interval is not None:
            data["multiple-steps-interval"] = multiple_steps_interval
        if retrieve is not None:
            data["retrieve"] = retrieve
        if retry_interval is not None:
            data["retry-interval"] = retry_interval
        if retry_max is not None:
            data["retry-max"] = retry_max
        if revision_diff is not None:
            data["revision-diff"] = revision_diff
        if send_image_retry is not None:
            data["send-image-retry"] = send_image_retry
        if upgrade_timeout is not None:
            data["upgrade-timeout"] = upgrade_timeout
        
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
