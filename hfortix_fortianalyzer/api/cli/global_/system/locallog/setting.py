"""
FortiAnalyzer API endpoint: cli.global.system.locallog.setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogSetting:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.setting
    
    
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
        url = "/cli/global/system/locallog/setting"
        
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
        log_daemon_crash: Literal["disable", "enable"] | None = None,
        log_interval_adom_perf_stats: int | None = None,
        log_interval_dev_no_logging: int | None = None,
        log_interval_disk_full: int | None = None,
        log_interval_gbday_exceeded: int | None = None,
        no_log_detection_threshold: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            log_daemon_crash: log-daemon-crash parameter
            log_interval_adom_perf_stats: log-interval-adom-perf-stats parameter
            log_interval_dev_no_logging: log-interval-dev-no-logging parameter
            log_interval_disk_full: log-interval-disk-full parameter
            log_interval_gbday_exceeded: log-interval-gbday-exceeded parameter
            no_log_detection_threshold: no-log-detection-threshold parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/setting"
        
        # Build data payload
        data = {}
        if log_daemon_crash is not None:
            data["log-daemon-crash"] = log_daemon_crash
        if log_interval_adom_perf_stats is not None:
            data["log-interval-adom-perf-stats"] = log_interval_adom_perf_stats
        if log_interval_dev_no_logging is not None:
            data["log-interval-dev-no-logging"] = log_interval_dev_no_logging
        if log_interval_disk_full is not None:
            data["log-interval-disk-full"] = log_interval_disk_full
        if log_interval_gbday_exceeded is not None:
            data["log-interval-gbday-exceeded"] = log_interval_gbday_exceeded
        if no_log_detection_threshold is not None:
            data["no-log-detection-threshold"] = no_log_detection_threshold
        
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
        log_daemon_crash: Literal["disable", "enable"] | None = None,
        log_interval_adom_perf_stats: int | None = None,
        log_interval_dev_no_logging: int | None = None,
        log_interval_disk_full: int | None = None,
        log_interval_gbday_exceeded: int | None = None,
        no_log_detection_threshold: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            log_daemon_crash: log-daemon-crash parameter
            log_interval_adom_perf_stats: log-interval-adom-perf-stats parameter
            log_interval_dev_no_logging: log-interval-dev-no-logging parameter
            log_interval_disk_full: log-interval-disk-full parameter
            log_interval_gbday_exceeded: log-interval-gbday-exceeded parameter
            no_log_detection_threshold: no-log-detection-threshold parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/setting"
        
        # Build data payload
        data = {}
        if log_daemon_crash is not None:
            data["log-daemon-crash"] = log_daemon_crash
        if log_interval_adom_perf_stats is not None:
            data["log-interval-adom-perf-stats"] = log_interval_adom_perf_stats
        if log_interval_dev_no_logging is not None:
            data["log-interval-dev-no-logging"] = log_interval_dev_no_logging
        if log_interval_disk_full is not None:
            data["log-interval-disk-full"] = log_interval_disk_full
        if log_interval_gbday_exceeded is not None:
            data["log-interval-gbday-exceeded"] = log_interval_gbday_exceeded
        if no_log_detection_threshold is not None:
            data["no-log-detection-threshold"] = no_log_detection_threshold
        
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
