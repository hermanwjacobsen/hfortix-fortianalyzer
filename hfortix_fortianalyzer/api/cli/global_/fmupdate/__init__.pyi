"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .analyzer import Analyzer
    from .av_ips import Avips
    from .custom_url_list import CliGlobalFmupdateCustomUrlList
    from .disk_quota import CliGlobalFmupdateDiskQuota
    from .fct_services import CliGlobalFmupdateFctServices
    from .fds_setting import CliGlobalFmupdateFdsSetting
    from .fgd_setting import CliGlobalFmupdateFgdSetting
    from .fwm_setting import CliGlobalFmupdateFwmSetting
    from .multilayer import CliGlobalFmupdateMultilayer
    from .publicnetwork import CliGlobalFmupdatePublicnetwork
    from .server_access_priorities import CliGlobalFmupdateServerAccessPriorities
    from .server_override_status import CliGlobalFmupdateServerOverrideStatus
    from .service import CliGlobalFmupdateService

__all__ = ["Fmupdate"]


class Fmupdate:
    """Fmupdate endpoints."""

    analyzer: Analyzer
    av_ips: Avips
    custom_url_list: CliGlobalFmupdateCustomUrlList
    disk_quota: CliGlobalFmupdateDiskQuota
    fct_services: CliGlobalFmupdateFctServices
    fds_setting: CliGlobalFmupdateFdsSetting
    fgd_setting: CliGlobalFmupdateFgdSetting
    fwm_setting: CliGlobalFmupdateFwmSetting
    multilayer: CliGlobalFmupdateMultilayer
    publicnetwork: CliGlobalFmupdatePublicnetwork
    server_access_priorities: CliGlobalFmupdateServerAccessPriorities
    server_override_status: CliGlobalFmupdateServerOverrideStatus
    service: CliGlobalFmupdateService

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
