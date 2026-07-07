"""FortiAnalyzer fmupdate global_ API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import analyzer
    from . import av_ips
    from . import custom_url_list
    from . import disk_quota
    from . import fct_services
    from . import fds_setting
    from . import fgd_setting
    from . import fwm_setting
    from . import multilayer
    from . import publicnetwork
    from . import server_access_priorities
    from . import server_override_status
    from . import service

__all__ = ["Fmupdate"]


class Fmupdate:
    """FortiAnalyzer fmupdate global_ API endpoints."""

    analyzer: "analyzer.Analyzer"
    av_ips: "av_ips.Avips"
    custom_url_list: "custom_url_list.CliGlobalFmupdateCustomUrlList"
    disk_quota: "disk_quota.CliGlobalFmupdateDiskQuota"
    fct_services: "fct_services.CliGlobalFmupdateFctServices"
    fds_setting: "fds_setting.CliGlobalFmupdateFdsSetting"
    fgd_setting: "fgd_setting.CliGlobalFmupdateFgdSetting"
    fwm_setting: "fwm_setting.CliGlobalFmupdateFwmSetting"
    multilayer: "multilayer.CliGlobalFmupdateMultilayer"
    publicnetwork: "publicnetwork.CliGlobalFmupdatePublicnetwork"
    server_access_priorities: "server_access_priorities.CliGlobalFmupdateServerAccessPriorities"
    server_override_status: "server_override_status.CliGlobalFmupdateServerOverrideStatus"
    service: "service.CliGlobalFmupdateService"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Fmupdate namespace with JSON-RPC client."""
        from . import analyzer as analyzer_module
        from . import av_ips as av_ips_module
        from . import custom_url_list as custom_url_list_module
        from . import disk_quota as disk_quota_module
        from . import fct_services as fct_services_module
        from . import fds_setting as fds_setting_module
        from . import fgd_setting as fgd_setting_module
        from . import fwm_setting as fwm_setting_module
        from . import multilayer as multilayer_module
        from . import publicnetwork as publicnetwork_module
        from . import server_access_priorities as server_access_priorities_module
        from . import server_override_status as server_override_status_module
        from . import service as service_module

        self.analyzer = analyzer_module.Analyzer(client)
        self.av_ips = av_ips_module.Avips(client)
        self.custom_url_list = custom_url_list_module.CliGlobalFmupdateCustomUrlList(client)
        self.disk_quota = disk_quota_module.CliGlobalFmupdateDiskQuota(client)
        self.fct_services = fct_services_module.CliGlobalFmupdateFctServices(client)
        self.fds_setting = fds_setting_module.CliGlobalFmupdateFdsSetting(client)
        self.fgd_setting = fgd_setting_module.CliGlobalFmupdateFgdSetting(client)
        self.fwm_setting = fwm_setting_module.CliGlobalFmupdateFwmSetting(client)
        self.multilayer = multilayer_module.CliGlobalFmupdateMultilayer(client)
        self.publicnetwork = publicnetwork_module.CliGlobalFmupdatePublicnetwork(client)
        self.server_access_priorities = server_access_priorities_module.CliGlobalFmupdateServerAccessPriorities(client)
        self.server_override_status = server_override_status_module.CliGlobalFmupdateServerOverrideStatus(client)
        self.service = service_module.CliGlobalFmupdateService(client)
