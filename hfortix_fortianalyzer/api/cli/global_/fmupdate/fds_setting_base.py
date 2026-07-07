"""
FortiAnalyzer API endpoint: cli.global.fmupdate.fds-setting

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFdsSetting:
    """
    FortiAnalyzer endpoint: cli.global.fmupdate.fds-setting
    
    
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
        url = "/cli/global/fmupdate/fds-setting"
        
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
        User_Agent: str | None = None,
        controller_contract_download: Literal["disable", "enable"] | None = None,
        fds_clt_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        fds_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        fmtr_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        fortiguard_anycast: Literal["disable", "enable"] | None = None,
        fortiguard_anycast_source: Literal["fortinet", "aws"] | None = None,
        linkd_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        max_av_ips_version: int | None = None,
        max_work: int | None = None,
        send_report: Literal["disable", "enable"] | None = None,
        send_setup: Literal["disable", "enable"] | None = None,
        umsvc_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        unreg_dev_option: Literal["ignore", "svc-only", "add-service"] | None = None,
        wanip_query_mode: Literal["disable", "ipify"] | None = None,
        push_override: dict[str, Any] | None = None,
        push_override_to_client: dict[str, Any] | None = None,
        server_override: dict[str, Any] | None = None,
        system_support_fai: list[Any] | None = None,
        system_support_faz: list[Any] | None = None,
        system_support_fct: list[Any] | None = None,
        system_support_fdc: list[Any] | None = None,
        system_support_fgt: list[Any] | None = None,
        system_support_fis: list[Any] | None = None,
        system_support_fml: list[Any] | None = None,
        system_support_fsa: list[Any] | None = None,
        system_support_fts: list[Any] | None = None,
        update_schedule: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            User_Agent: User-Agent parameter
            controller_contract_download: controller-contract-download parameter
            fds_clt_ssl_protocol: fds-clt-ssl-protocol parameter
            fds_ssl_protocol: fds-ssl-protocol parameter
            fmtr_log: fmtr-log parameter
            fortiguard_anycast: fortiguard-anycast parameter
            fortiguard_anycast_source: fortiguard-anycast-source parameter
            linkd_log: linkd-log parameter
            max_av_ips_version: max-av-ips-version parameter
            max_work: max-work parameter
            ... (18 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fds-setting"
        
        # Build data payload
        data = {}
        if User_Agent is not None:
            data["User-Agent"] = User_Agent
        if controller_contract_download is not None:
            data["controller-contract-download"] = controller_contract_download
        if fds_clt_ssl_protocol is not None:
            data["fds-clt-ssl-protocol"] = fds_clt_ssl_protocol
        if fds_ssl_protocol is not None:
            data["fds-ssl-protocol"] = fds_ssl_protocol
        if fmtr_log is not None:
            data["fmtr-log"] = fmtr_log
        if fortiguard_anycast is not None:
            data["fortiguard-anycast"] = fortiguard_anycast
        if fortiguard_anycast_source is not None:
            data["fortiguard-anycast-source"] = fortiguard_anycast_source
        if linkd_log is not None:
            data["linkd-log"] = linkd_log
        if max_av_ips_version is not None:
            data["max-av-ips-version"] = max_av_ips_version
        if max_work is not None:
            data["max-work"] = max_work
        if push_override is not None:
            data["push-override"] = push_override
        if push_override_to_client is not None:
            data["push-override-to-client"] = push_override_to_client
        if send_report is not None:
            data["send_report"] = send_report
        if send_setup is not None:
            data["send_setup"] = send_setup
        if server_override is not None:
            data["server-override"] = server_override
        if system_support_fai is not None:
            data["system-support-fai"] = system_support_fai
        if system_support_faz is not None:
            data["system-support-faz"] = system_support_faz
        if system_support_fct is not None:
            data["system-support-fct"] = system_support_fct
        if system_support_fdc is not None:
            data["system-support-fdc"] = system_support_fdc
        if system_support_fgt is not None:
            data["system-support-fgt"] = system_support_fgt
        if system_support_fis is not None:
            data["system-support-fis"] = system_support_fis
        if system_support_fml is not None:
            data["system-support-fml"] = system_support_fml
        if system_support_fsa is not None:
            data["system-support-fsa"] = system_support_fsa
        if system_support_fts is not None:
            data["system-support-fts"] = system_support_fts
        if umsvc_log is not None:
            data["umsvc-log"] = umsvc_log
        if unreg_dev_option is not None:
            data["unreg-dev-option"] = unreg_dev_option
        if update_schedule is not None:
            data["update-schedule"] = update_schedule
        if wanip_query_mode is not None:
            data["wanip-query-mode"] = wanip_query_mode
        
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
        User_Agent: str | None = None,
        controller_contract_download: Literal["disable", "enable"] | None = None,
        fds_clt_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        fds_ssl_protocol: Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        fmtr_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        fortiguard_anycast: Literal["disable", "enable"] | None = None,
        fortiguard_anycast_source: Literal["fortinet", "aws"] | None = None,
        linkd_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        max_av_ips_version: int | None = None,
        max_work: int | None = None,
        send_report: Literal["disable", "enable"] | None = None,
        send_setup: Literal["disable", "enable"] | None = None,
        umsvc_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        unreg_dev_option: Literal["ignore", "svc-only", "add-service"] | None = None,
        wanip_query_mode: Literal["disable", "ipify"] | None = None,
        push_override: dict[str, Any] | None = None,
        push_override_to_client: dict[str, Any] | None = None,
        server_override: dict[str, Any] | None = None,
        system_support_fai: list[Any] | None = None,
        system_support_faz: list[Any] | None = None,
        system_support_fct: list[Any] | None = None,
        system_support_fdc: list[Any] | None = None,
        system_support_fgt: list[Any] | None = None,
        system_support_fis: list[Any] | None = None,
        system_support_fml: list[Any] | None = None,
        system_support_fsa: list[Any] | None = None,
        system_support_fts: list[Any] | None = None,
        update_schedule: dict[str, Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            User_Agent: User-Agent parameter
            controller_contract_download: controller-contract-download parameter
            fds_clt_ssl_protocol: fds-clt-ssl-protocol parameter
            fds_ssl_protocol: fds-ssl-protocol parameter
            fmtr_log: fmtr-log parameter
            fortiguard_anycast: fortiguard-anycast parameter
            fortiguard_anycast_source: fortiguard-anycast-source parameter
            linkd_log: linkd-log parameter
            max_av_ips_version: max-av-ips-version parameter
            max_work: max-work parameter
            ... (18 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/fmupdate/fds-setting"
        
        # Build data payload
        data = {}
        if User_Agent is not None:
            data["User-Agent"] = User_Agent
        if controller_contract_download is not None:
            data["controller-contract-download"] = controller_contract_download
        if fds_clt_ssl_protocol is not None:
            data["fds-clt-ssl-protocol"] = fds_clt_ssl_protocol
        if fds_ssl_protocol is not None:
            data["fds-ssl-protocol"] = fds_ssl_protocol
        if fmtr_log is not None:
            data["fmtr-log"] = fmtr_log
        if fortiguard_anycast is not None:
            data["fortiguard-anycast"] = fortiguard_anycast
        if fortiguard_anycast_source is not None:
            data["fortiguard-anycast-source"] = fortiguard_anycast_source
        if linkd_log is not None:
            data["linkd-log"] = linkd_log
        if max_av_ips_version is not None:
            data["max-av-ips-version"] = max_av_ips_version
        if max_work is not None:
            data["max-work"] = max_work
        if push_override is not None:
            data["push-override"] = push_override
        if push_override_to_client is not None:
            data["push-override-to-client"] = push_override_to_client
        if send_report is not None:
            data["send_report"] = send_report
        if send_setup is not None:
            data["send_setup"] = send_setup
        if server_override is not None:
            data["server-override"] = server_override
        if system_support_fai is not None:
            data["system-support-fai"] = system_support_fai
        if system_support_faz is not None:
            data["system-support-faz"] = system_support_faz
        if system_support_fct is not None:
            data["system-support-fct"] = system_support_fct
        if system_support_fdc is not None:
            data["system-support-fdc"] = system_support_fdc
        if system_support_fgt is not None:
            data["system-support-fgt"] = system_support_fgt
        if system_support_fis is not None:
            data["system-support-fis"] = system_support_fis
        if system_support_fml is not None:
            data["system-support-fml"] = system_support_fml
        if system_support_fsa is not None:
            data["system-support-fsa"] = system_support_fsa
        if system_support_fts is not None:
            data["system-support-fts"] = system_support_fts
        if umsvc_log is not None:
            data["umsvc-log"] = umsvc_log
        if unreg_dev_option is not None:
            data["unreg-dev-option"] = unreg_dev_option
        if update_schedule is not None:
            data["update-schedule"] = update_schedule
        if wanip_query_mode is not None:
            data["wanip-query-mode"] = wanip_query_mode
        
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
