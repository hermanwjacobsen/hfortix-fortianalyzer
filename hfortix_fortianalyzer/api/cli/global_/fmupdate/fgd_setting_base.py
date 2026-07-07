"""
FortiAnalyzer API endpoint: cli.global.fmupdate.fgd-setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFgdSetting:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.fgd-setting
    
    
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
        url = "/cli/global/fmupdate/fgd-setting"
        
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
        restrict_as1_dbver: str | None = None,
        restrict_as2_dbver: str | None = None,
        restrict_as4_dbver: str | None = None,
        restrict_av_dbver: str | None = None,
        restrict_av2_dbver: str | None = None,
        restrict_fq_dbver: str | None = None,
        restrict_iots_dbver: str | None = None,
        restrict_wf_dbver: str | None = None,
        server_override: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            as_cache: as-cache parameter
            as_log: as-log parameter
            as_preload: as-preload parameter
            av_cache: av-cache parameter
            av_log: av-log parameter
            av_preload: av-preload parameter
            av2_cache: av2-cache parameter
            av2_log: av2-log parameter
            av2_preload: av2-preload parameter
            delta_ratio: delta-ratio parameter
            ... (32 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fgd-setting"
        
        # Build data payload
        data = {}
        if as_cache is not None:
            data["as-cache"] = as_cache
        if as_log is not None:
            data["as-log"] = as_log
        if as_preload is not None:
            data["as-preload"] = as_preload
        if av_cache is not None:
            data["av-cache"] = av_cache
        if av_log is not None:
            data["av-log"] = av_log
        if av_preload is not None:
            data["av-preload"] = av_preload
        if av2_cache is not None:
            data["av2-cache"] = av2_cache
        if av2_log is not None:
            data["av2-log"] = av2_log
        if av2_preload is not None:
            data["av2-preload"] = av2_preload
        if delta_ratio is not None:
            data["delta-ratio"] = delta_ratio
        if eventlog_query is not None:
            data["eventlog-query"] = eventlog_query
        if fgd_pull_interval is not None:
            data["fgd-pull-interval"] = fgd_pull_interval
        if fq_cache is not None:
            data["fq-cache"] = fq_cache
        if fq_log is not None:
            data["fq-log"] = fq_log
        if fq_preload is not None:
            data["fq-preload"] = fq_preload
        if iot_cache is not None:
            data["iot-cache"] = iot_cache
        if iot_log is not None:
            data["iot-log"] = iot_log
        if iot_preload is not None:
            data["iot-preload"] = iot_preload
        if iotv_preload is not None:
            data["iotv-preload"] = iotv_preload
        if linkd_log is not None:
            data["linkd-log"] = linkd_log
        if max_client_worker is not None:
            data["max-client-worker"] = max_client_worker
        if max_log_quota is not None:
            data["max-log-quota"] = max_log_quota
        if max_unrated_site is not None:
            data["max-unrated-site"] = max_unrated_site
        if restrict_as1_dbver is not None:
            data["restrict-as1-dbver"] = restrict_as1_dbver
        if restrict_as2_dbver is not None:
            data["restrict-as2-dbver"] = restrict_as2_dbver
        if restrict_as4_dbver is not None:
            data["restrict-as4-dbver"] = restrict_as4_dbver
        if restrict_av_dbver is not None:
            data["restrict-av-dbver"] = restrict_av_dbver
        if restrict_av2_dbver is not None:
            data["restrict-av2-dbver"] = restrict_av2_dbver
        if restrict_fq_dbver is not None:
            data["restrict-fq-dbver"] = restrict_fq_dbver
        if restrict_iots_dbver is not None:
            data["restrict-iots-dbver"] = restrict_iots_dbver
        if restrict_wf_dbver is not None:
            data["restrict-wf-dbver"] = restrict_wf_dbver
        if server_override is not None:
            data["server-override"] = server_override
        if stat_log is not None:
            data["stat-log"] = stat_log
        if stat_log_interval is not None:
            data["stat-log-interval"] = stat_log_interval
        if stat_sync_interval is not None:
            data["stat-sync-interval"] = stat_sync_interval
        if update_interval is not None:
            data["update-interval"] = update_interval
        if update_log is not None:
            data["update-log"] = update_log
        if wf_cache is not None:
            data["wf-cache"] = wf_cache
        if wf_dn_cache_expire_time is not None:
            data["wf-dn-cache-expire-time"] = wf_dn_cache_expire_time
        if wf_dn_cache_max_number is not None:
            data["wf-dn-cache-max-number"] = wf_dn_cache_max_number
        if wf_log is not None:
            data["wf-log"] = wf_log
        if wf_preload is not None:
            data["wf-preload"] = wf_preload
        
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
        restrict_as1_dbver: str | None = None,
        restrict_as2_dbver: str | None = None,
        restrict_as4_dbver: str | None = None,
        restrict_av_dbver: str | None = None,
        restrict_av2_dbver: str | None = None,
        restrict_fq_dbver: str | None = None,
        restrict_iots_dbver: str | None = None,
        restrict_wf_dbver: str | None = None,
        server_override: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            as_cache: as-cache parameter
            as_log: as-log parameter
            as_preload: as-preload parameter
            av_cache: av-cache parameter
            av_log: av-log parameter
            av_preload: av-preload parameter
            av2_cache: av2-cache parameter
            av2_log: av2-log parameter
            av2_preload: av2-preload parameter
            delta_ratio: delta-ratio parameter
            ... (32 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fgd-setting"
        
        # Build data payload
        data = {}
        if as_cache is not None:
            data["as-cache"] = as_cache
        if as_log is not None:
            data["as-log"] = as_log
        if as_preload is not None:
            data["as-preload"] = as_preload
        if av_cache is not None:
            data["av-cache"] = av_cache
        if av_log is not None:
            data["av-log"] = av_log
        if av_preload is not None:
            data["av-preload"] = av_preload
        if av2_cache is not None:
            data["av2-cache"] = av2_cache
        if av2_log is not None:
            data["av2-log"] = av2_log
        if av2_preload is not None:
            data["av2-preload"] = av2_preload
        if delta_ratio is not None:
            data["delta-ratio"] = delta_ratio
        if eventlog_query is not None:
            data["eventlog-query"] = eventlog_query
        if fgd_pull_interval is not None:
            data["fgd-pull-interval"] = fgd_pull_interval
        if fq_cache is not None:
            data["fq-cache"] = fq_cache
        if fq_log is not None:
            data["fq-log"] = fq_log
        if fq_preload is not None:
            data["fq-preload"] = fq_preload
        if iot_cache is not None:
            data["iot-cache"] = iot_cache
        if iot_log is not None:
            data["iot-log"] = iot_log
        if iot_preload is not None:
            data["iot-preload"] = iot_preload
        if iotv_preload is not None:
            data["iotv-preload"] = iotv_preload
        if linkd_log is not None:
            data["linkd-log"] = linkd_log
        if max_client_worker is not None:
            data["max-client-worker"] = max_client_worker
        if max_log_quota is not None:
            data["max-log-quota"] = max_log_quota
        if max_unrated_site is not None:
            data["max-unrated-site"] = max_unrated_site
        if restrict_as1_dbver is not None:
            data["restrict-as1-dbver"] = restrict_as1_dbver
        if restrict_as2_dbver is not None:
            data["restrict-as2-dbver"] = restrict_as2_dbver
        if restrict_as4_dbver is not None:
            data["restrict-as4-dbver"] = restrict_as4_dbver
        if restrict_av_dbver is not None:
            data["restrict-av-dbver"] = restrict_av_dbver
        if restrict_av2_dbver is not None:
            data["restrict-av2-dbver"] = restrict_av2_dbver
        if restrict_fq_dbver is not None:
            data["restrict-fq-dbver"] = restrict_fq_dbver
        if restrict_iots_dbver is not None:
            data["restrict-iots-dbver"] = restrict_iots_dbver
        if restrict_wf_dbver is not None:
            data["restrict-wf-dbver"] = restrict_wf_dbver
        if server_override is not None:
            data["server-override"] = server_override
        if stat_log is not None:
            data["stat-log"] = stat_log
        if stat_log_interval is not None:
            data["stat-log-interval"] = stat_log_interval
        if stat_sync_interval is not None:
            data["stat-sync-interval"] = stat_sync_interval
        if update_interval is not None:
            data["update-interval"] = update_interval
        if update_log is not None:
            data["update-log"] = update_log
        if wf_cache is not None:
            data["wf-cache"] = wf_cache
        if wf_dn_cache_expire_time is not None:
            data["wf-dn-cache-expire-time"] = wf_dn_cache_expire_time
        if wf_dn_cache_max_number is not None:
            data["wf-dn-cache-max-number"] = wf_dn_cache_max_number
        if wf_log is not None:
            data["wf-log"] = wf_log
        if wf_preload is not None:
            data["wf-preload"] = wf_preload
        
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
