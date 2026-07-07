"""Type stubs for cli.global.system.locallog.syslogd2.filter"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLocallogSyslogd2FilterGetItem:
    """Item yielded when iterating over CliGlobalSystemLocallogSyslogd2FilterGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def controller(self) -> Literal["disable", "enable"]: ...
    @property
    def devcfg(self) -> Literal["disable", "enable"]: ...
    @property
    def devops(self) -> Literal["disable", "enable"]: ...
    @property
    def diskquota(self) -> Literal["disable", "enable"]: ...
    @property
    def dm(self) -> Literal["disable", "enable"]: ...
    @property
    def dvm(self) -> Literal["disable", "enable"]: ...
    @property
    def ediscovery(self) -> Literal["disable", "enable"]: ...
    @property
    def epmgr(self) -> Literal["disable", "enable"]: ...
    @property
    def event(self) -> Literal["disable", "enable"]: ...
    @property
    def eventmgmt(self) -> Literal["disable", "enable"]: ...
    @property
    def faz(self) -> Literal["disable", "enable"]: ...
    @property
    def fazfabric(self) -> Literal["disable", "enable"]: ...
    @property
    def fazha(self) -> Literal["disable", "enable"]: ...
    @property
    def fazsys(self) -> Literal["disable", "enable"]: ...
    @property
    def fgd(self) -> Literal["disable", "enable"]: ...
    @property
    def fgfm(self) -> Literal["disable", "enable"]: ...
    @property
    def fips(self) -> Literal["disable", "enable"]: ...
    @property
    def fmgws(self) -> Literal["disable", "enable"]: ...
    @property
    def fmlmgr(self) -> Literal["disable", "enable"]: ...
    @property
    def fmwmgr(self) -> Literal["disable", "enable"]: ...
    @property
    def fortiview(self) -> Literal["disable", "enable"]: ...
    @property
    def glbcfg(self) -> Literal["disable", "enable"]: ...
    @property
    def ha(self) -> Literal["disable", "enable"]: ...
    @property
    def hcache(self) -> Literal["disable", "enable"]: ...
    @property
    def incident(self) -> Literal["disable", "enable"]: ...
    @property
    def iolog(self) -> Literal["disable", "enable"]: ...
    @property
    def logd(self) -> Literal["disable", "enable"]: ...
    @property
    def logdb(self) -> Literal["disable", "enable"]: ...
    @property
    def logdev(self) -> Literal["disable", "enable"]: ...
    @property
    def logfile(self) -> Literal["disable", "enable"]: ...
    @property
    def logging(self) -> Literal["disable", "enable"]: ...
    @property
    def lrmgr(self) -> Literal["disable", "enable"]: ...
    @property
    def objcfg(self) -> Literal["disable", "enable"]: ...
    @property
    def report(self) -> Literal["disable", "enable"]: ...
    @property
    def rev(self) -> Literal["disable", "enable"]: ...
    @property
    def rtmon(self) -> Literal["disable", "enable"]: ...
    @property
    def scfw(self) -> Literal["disable", "enable"]: ...
    @property
    def scply(self) -> Literal["disable", "enable"]: ...
    @property
    def scrmgr(self) -> Literal["disable", "enable"]: ...
    @property
    def scvpn(self) -> Literal["disable", "enable"]: ...
    @property
    def system(self) -> Literal["disable", "enable"]: ...
    @property
    def webport(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLocallogSyslogd2FilterGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLocallogSyslogd2FilterGet endpoint with autocomplete support."""

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
    def controller(self) -> Literal["disable", "enable"] | None:
        """Field: controller"""
        ...

    @property
    def devcfg(self) -> Literal["disable", "enable"] | None:
        """Field: devcfg"""
        ...

    @property
    def devops(self) -> Literal["disable", "enable"] | None:
        """Field: devops"""
        ...

    @property
    def diskquota(self) -> Literal["disable", "enable"] | None:
        """Field: diskquota"""
        ...

    @property
    def dm(self) -> Literal["disable", "enable"] | None:
        """Field: dm"""
        ...

    @property
    def dvm(self) -> Literal["disable", "enable"] | None:
        """Field: dvm"""
        ...

    @property
    def ediscovery(self) -> Literal["disable", "enable"] | None:
        """Field: ediscovery"""
        ...

    @property
    def epmgr(self) -> Literal["disable", "enable"] | None:
        """Field: epmgr"""
        ...

    @property
    def event(self) -> Literal["disable", "enable"] | None:
        """Field: event"""
        ...

    @property
    def eventmgmt(self) -> Literal["disable", "enable"] | None:
        """Field: eventmgmt"""
        ...

    @property
    def faz(self) -> Literal["disable", "enable"] | None:
        """Field: faz"""
        ...

    @property
    def fazfabric(self) -> Literal["disable", "enable"] | None:
        """Field: fazfabric"""
        ...

    @property
    def fazha(self) -> Literal["disable", "enable"] | None:
        """Field: fazha"""
        ...

    @property
    def fazsys(self) -> Literal["disable", "enable"] | None:
        """Field: fazsys"""
        ...

    @property
    def fgd(self) -> Literal["disable", "enable"] | None:
        """Field: fgd"""
        ...

    @property
    def fgfm(self) -> Literal["disable", "enable"] | None:
        """Field: fgfm"""
        ...

    @property
    def fips(self) -> Literal["disable", "enable"] | None:
        """Field: fips"""
        ...

    @property
    def fmgws(self) -> Literal["disable", "enable"] | None:
        """Field: fmgws"""
        ...

    @property
    def fmlmgr(self) -> Literal["disable", "enable"] | None:
        """Field: fmlmgr"""
        ...

    @property
    def fmwmgr(self) -> Literal["disable", "enable"] | None:
        """Field: fmwmgr"""
        ...

    @property
    def fortiview(self) -> Literal["disable", "enable"] | None:
        """Field: fortiview"""
        ...

    @property
    def glbcfg(self) -> Literal["disable", "enable"] | None:
        """Field: glbcfg"""
        ...

    @property
    def ha(self) -> Literal["disable", "enable"] | None:
        """Field: ha"""
        ...

    @property
    def hcache(self) -> Literal["disable", "enable"] | None:
        """Field: hcache"""
        ...

    @property
    def incident(self) -> Literal["disable", "enable"] | None:
        """Field: incident"""
        ...

    @property
    def iolog(self) -> Literal["disable", "enable"] | None:
        """Field: iolog"""
        ...

    @property
    def logd(self) -> Literal["disable", "enable"] | None:
        """Field: logd"""
        ...

    @property
    def logdb(self) -> Literal["disable", "enable"] | None:
        """Field: logdb"""
        ...

    @property
    def logdev(self) -> Literal["disable", "enable"] | None:
        """Field: logdev"""
        ...

    @property
    def logfile(self) -> Literal["disable", "enable"] | None:
        """Field: logfile"""
        ...

    @property
    def logging(self) -> Literal["disable", "enable"] | None:
        """Field: logging"""
        ...

    @property
    def lrmgr(self) -> Literal["disable", "enable"] | None:
        """Field: lrmgr"""
        ...

    @property
    def objcfg(self) -> Literal["disable", "enable"] | None:
        """Field: objcfg"""
        ...

    @property
    def report(self) -> Literal["disable", "enable"] | None:
        """Field: report"""
        ...

    @property
    def rev(self) -> Literal["disable", "enable"] | None:
        """Field: rev"""
        ...

    @property
    def rtmon(self) -> Literal["disable", "enable"] | None:
        """Field: rtmon"""
        ...

    @property
    def scfw(self) -> Literal["disable", "enable"] | None:
        """Field: scfw"""
        ...

    @property
    def scply(self) -> Literal["disable", "enable"] | None:
        """Field: scply"""
        ...

    @property
    def scrmgr(self) -> Literal["disable", "enable"] | None:
        """Field: scrmgr"""
        ...

    @property
    def scvpn(self) -> Literal["disable", "enable"] | None:
        """Field: scvpn"""
        ...

    @property
    def system(self) -> Literal["disable", "enable"] | None:
        """Field: system"""
        ...

    @property
    def webport(self) -> Literal["disable", "enable"] | None:
        """Field: webport"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLocallogSyslogd2FilterGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLocallogSyslogd2Filter:
    """FortiAnalyzer endpoint: cli.global.system.locallog.syslogd2.filter"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalSystemLocallogSyslogd2FilterGetResponse:
        """GET operation."""
        ...

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
        logfile: Literal["disable", "enable"] | None = None,
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
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

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
        logfile: Literal["disable", "enable"] | None = None,
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
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalSystemLocallogSyslogd2Filter", "CliGlobalSystemLocallogSyslogd2FilterGetResponse"]