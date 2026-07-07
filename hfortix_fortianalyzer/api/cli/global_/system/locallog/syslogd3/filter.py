"""
FortiAnalyzer API endpoint: cli.global.system.locallog.syslogd3.filter

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogSyslogd3Filter:
    """
    FortiAnalyzer endpoint: cli.global.system.locallog.syslogd3.filter
    
    
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
        url = "/cli/global/system/locallog/syslogd3/filter"
        
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
        controller: Literal["disable", "enable"] | None = None,
        devcfg: Literal["disable", "enable"] | None = None,
        devops: Literal["disable", "enable"] | None = None,
        diskquota: Literal["disable", "enable"] | None = None,
        dm: Literal["disable", "enable"] | None = None,
        dvm: Literal["disable", "enable"] | None = None,
        ediscovery: Literal["disable", "enable"] | None = None,
        epmgr: Literal["disable", "enable"] | None = None,
        event: Literal["disable", "enable"] | None = None,
        eventmgmt: Literal["disable", "enable"] | None = None,
        faz: Literal["disable", "enable"] | None = None,
        fazfabric: Literal["disable", "enable"] | None = None,
        fazha: Literal["disable", "enable"] | None = None,
        fazsys: Literal["disable", "enable"] | None = None,
        fgd: Literal["disable", "enable"] | None = None,
        fgfm: Literal["disable", "enable"] | None = None,
        fips: Literal["disable", "enable"] | None = None,
        fmgws: Literal["disable", "enable"] | None = None,
        fmlmgr: Literal["disable", "enable"] | None = None,
        fmwmgr: Literal["disable", "enable"] | None = None,
        fortiview: Literal["disable", "enable"] | None = None,
        glbcfg: Literal["disable", "enable"] | None = None,
        ha: Literal["disable", "enable"] | None = None,
        hcache: Literal["disable", "enable"] | None = None,
        incident: Literal["disable", "enable"] | None = None,
        iolog: Literal["disable", "enable"] | None = None,
        logd: Literal["disable", "enable"] | None = None,
        logdb: Literal["disable", "enable"] | None = None,
        logdev: Literal["disable", "enable"] | None = None,
        logging: Literal["disable", "enable"] | None = None,
        lrmgr: Literal["disable", "enable"] | None = None,
        objcfg: Literal["disable", "enable"] | None = None,
        report: Literal["disable", "enable"] | None = None,
        rev: Literal["disable", "enable"] | None = None,
        rtmon: Literal["disable", "enable"] | None = None,
        scfw: Literal["disable", "enable"] | None = None,
        scply: Literal["disable", "enable"] | None = None,
        scrmgr: Literal["disable", "enable"] | None = None,
        scvpn: Literal["disable", "enable"] | None = None,
        system: Literal["disable", "enable"] | None = None,
        webport: Literal["disable", "enable"] | None = None,
        logfile: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            controller: controller parameter
            devcfg: devcfg parameter
            devops: devops parameter
            diskquota: diskquota parameter
            dm: dm parameter
            dvm: dvm parameter
            ediscovery: ediscovery parameter
            epmgr: epmgr parameter
            event: event parameter
            eventmgmt: eventmgmt parameter
            ... (32 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/syslogd3/filter"
        
        # Build data payload
        data = {}
        if controller is not None:
            data["controller"] = controller
        if devcfg is not None:
            data["devcfg"] = devcfg
        if devops is not None:
            data["devops"] = devops
        if diskquota is not None:
            data["diskquota"] = diskquota
        if dm is not None:
            data["dm"] = dm
        if dvm is not None:
            data["dvm"] = dvm
        if ediscovery is not None:
            data["ediscovery"] = ediscovery
        if epmgr is not None:
            data["epmgr"] = epmgr
        if event is not None:
            data["event"] = event
        if eventmgmt is not None:
            data["eventmgmt"] = eventmgmt
        if faz is not None:
            data["faz"] = faz
        if fazfabric is not None:
            data["fazfabric"] = fazfabric
        if fazha is not None:
            data["fazha"] = fazha
        if fazsys is not None:
            data["fazsys"] = fazsys
        if fgd is not None:
            data["fgd"] = fgd
        if fgfm is not None:
            data["fgfm"] = fgfm
        if fips is not None:
            data["fips"] = fips
        if fmgws is not None:
            data["fmgws"] = fmgws
        if fmlmgr is not None:
            data["fmlmgr"] = fmlmgr
        if fmwmgr is not None:
            data["fmwmgr"] = fmwmgr
        if fortiview is not None:
            data["fortiview"] = fortiview
        if glbcfg is not None:
            data["glbcfg"] = glbcfg
        if ha is not None:
            data["ha"] = ha
        if hcache is not None:
            data["hcache"] = hcache
        if incident is not None:
            data["incident"] = incident
        if iolog is not None:
            data["iolog"] = iolog
        if logd is not None:
            data["logd"] = logd
        if logdb is not None:
            data["logdb"] = logdb
        if logdev is not None:
            data["logdev"] = logdev
        if logfile is not None:
            data["logfile"] = logfile
        if logging is not None:
            data["logging"] = logging
        if lrmgr is not None:
            data["lrmgr"] = lrmgr
        if objcfg is not None:
            data["objcfg"] = objcfg
        if report is not None:
            data["report"] = report
        if rev is not None:
            data["rev"] = rev
        if rtmon is not None:
            data["rtmon"] = rtmon
        if scfw is not None:
            data["scfw"] = scfw
        if scply is not None:
            data["scply"] = scply
        if scrmgr is not None:
            data["scrmgr"] = scrmgr
        if scvpn is not None:
            data["scvpn"] = scvpn
        if system is not None:
            data["system"] = system
        if webport is not None:
            data["webport"] = webport
        
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
        controller: Literal["disable", "enable"] | None = None,
        devcfg: Literal["disable", "enable"] | None = None,
        devops: Literal["disable", "enable"] | None = None,
        diskquota: Literal["disable", "enable"] | None = None,
        dm: Literal["disable", "enable"] | None = None,
        dvm: Literal["disable", "enable"] | None = None,
        ediscovery: Literal["disable", "enable"] | None = None,
        epmgr: Literal["disable", "enable"] | None = None,
        event: Literal["disable", "enable"] | None = None,
        eventmgmt: Literal["disable", "enable"] | None = None,
        faz: Literal["disable", "enable"] | None = None,
        fazfabric: Literal["disable", "enable"] | None = None,
        fazha: Literal["disable", "enable"] | None = None,
        fazsys: Literal["disable", "enable"] | None = None,
        fgd: Literal["disable", "enable"] | None = None,
        fgfm: Literal["disable", "enable"] | None = None,
        fips: Literal["disable", "enable"] | None = None,
        fmgws: Literal["disable", "enable"] | None = None,
        fmlmgr: Literal["disable", "enable"] | None = None,
        fmwmgr: Literal["disable", "enable"] | None = None,
        fortiview: Literal["disable", "enable"] | None = None,
        glbcfg: Literal["disable", "enable"] | None = None,
        ha: Literal["disable", "enable"] | None = None,
        hcache: Literal["disable", "enable"] | None = None,
        incident: Literal["disable", "enable"] | None = None,
        iolog: Literal["disable", "enable"] | None = None,
        logd: Literal["disable", "enable"] | None = None,
        logdb: Literal["disable", "enable"] | None = None,
        logdev: Literal["disable", "enable"] | None = None,
        logging: Literal["disable", "enable"] | None = None,
        lrmgr: Literal["disable", "enable"] | None = None,
        objcfg: Literal["disable", "enable"] | None = None,
        report: Literal["disable", "enable"] | None = None,
        rev: Literal["disable", "enable"] | None = None,
        rtmon: Literal["disable", "enable"] | None = None,
        scfw: Literal["disable", "enable"] | None = None,
        scply: Literal["disable", "enable"] | None = None,
        scrmgr: Literal["disable", "enable"] | None = None,
        scvpn: Literal["disable", "enable"] | None = None,
        system: Literal["disable", "enable"] | None = None,
        webport: Literal["disable", "enable"] | None = None,
        logfile: Literal["disable", "enable"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            controller: controller parameter
            devcfg: devcfg parameter
            devops: devops parameter
            diskquota: diskquota parameter
            dm: dm parameter
            dvm: dvm parameter
            ediscovery: ediscovery parameter
            epmgr: epmgr parameter
            event: event parameter
            eventmgmt: eventmgmt parameter
            ... (32 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/locallog/syslogd3/filter"
        
        # Build data payload
        data = {}
        if controller is not None:
            data["controller"] = controller
        if devcfg is not None:
            data["devcfg"] = devcfg
        if devops is not None:
            data["devops"] = devops
        if diskquota is not None:
            data["diskquota"] = diskquota
        if dm is not None:
            data["dm"] = dm
        if dvm is not None:
            data["dvm"] = dvm
        if ediscovery is not None:
            data["ediscovery"] = ediscovery
        if epmgr is not None:
            data["epmgr"] = epmgr
        if event is not None:
            data["event"] = event
        if eventmgmt is not None:
            data["eventmgmt"] = eventmgmt
        if faz is not None:
            data["faz"] = faz
        if fazfabric is not None:
            data["fazfabric"] = fazfabric
        if fazha is not None:
            data["fazha"] = fazha
        if fazsys is not None:
            data["fazsys"] = fazsys
        if fgd is not None:
            data["fgd"] = fgd
        if fgfm is not None:
            data["fgfm"] = fgfm
        if fips is not None:
            data["fips"] = fips
        if fmgws is not None:
            data["fmgws"] = fmgws
        if fmlmgr is not None:
            data["fmlmgr"] = fmlmgr
        if fmwmgr is not None:
            data["fmwmgr"] = fmwmgr
        if fortiview is not None:
            data["fortiview"] = fortiview
        if glbcfg is not None:
            data["glbcfg"] = glbcfg
        if ha is not None:
            data["ha"] = ha
        if hcache is not None:
            data["hcache"] = hcache
        if incident is not None:
            data["incident"] = incident
        if iolog is not None:
            data["iolog"] = iolog
        if logd is not None:
            data["logd"] = logd
        if logdb is not None:
            data["logdb"] = logdb
        if logdev is not None:
            data["logdev"] = logdev
        if logfile is not None:
            data["logfile"] = logfile
        if logging is not None:
            data["logging"] = logging
        if lrmgr is not None:
            data["lrmgr"] = lrmgr
        if objcfg is not None:
            data["objcfg"] = objcfg
        if report is not None:
            data["report"] = report
        if rev is not None:
            data["rev"] = rev
        if rtmon is not None:
            data["rtmon"] = rtmon
        if scfw is not None:
            data["scfw"] = scfw
        if scply is not None:
            data["scply"] = scply
        if scrmgr is not None:
            data["scrmgr"] = scrmgr
        if scvpn is not None:
            data["scvpn"] = scvpn
        if system is not None:
            data["system"] = system
        if webport is not None:
            data["webport"] = webport
        
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
