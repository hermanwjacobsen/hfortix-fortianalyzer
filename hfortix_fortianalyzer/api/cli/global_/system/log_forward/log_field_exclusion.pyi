"""Type stubs for cli.global.system.log-forward.log-field-exclusion"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemLogForwardLogFieldExclusionGetItem:
    """Item yielded when iterating over CliGlobalSystemLogForwardLogFieldExclusionGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def dev_type(self) -> Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"]: ...
    @property
    def field_list(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def log_type(self) -> Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalSystemLogForwardLogFieldExclusionGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemLogForwardLogFieldExclusionGet endpoint with autocomplete support."""

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
    def dev_type(self) -> Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None:
        """Field: dev-type"""
        ...

    @property
    def field_list(self) -> str | None:
        """Field: field-list"""
        ...

    @property
    def id(self) -> int | None:
        """Field: id"""
        ...

    @property
    def log_type(self) -> Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None:
        """Field: log-type"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemLogForwardLogFieldExclusionGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemLogForwardLogFieldExclusion:
    """FortiAnalyzer endpoint: cli.global.system.log-forward.log-field-exclusion"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        fields: list[Literal["dev-type", "field-list", "id", "log-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemLogForwardLogFieldExclusionGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        dev_type: Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None = None,
        field_list: str | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        dev_type: Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None = None,
        field_list: str | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        log_forward: str,
        log_field_exclusion: int | str | None = None,
        dev_type: Literal["FortiGate", "FortiManager", "Syslog", "FortiClient", "FortiMail", "FortiWeb", "FortiCache", "FortiAnalyzer", "FortiSandbox", "FortiDDoS", "FortiAuthenticator", "FortiProxy", "FortiNAC", "FortiDeceptor", "FortiADC", "FortiFirewall", "FortiIsolator", "FortiEDR", "FortiPAM", "FortiCASB", "FortiToken"] | None = None,
        field_list: str | None = None,
        id: int | None = None,
        log_type: Literal["app-ctrl", "appevent", "attack", "content", "dlp", "emailfilter", "event", "generic", "history", "traffic", "virus", "voip", "webfilter", "netscan", "fct-event", "fct-traffic", "fct-netscan", "waf", "gtp", "dns", "ssh", "ssl", "file-filter", "Asset", "protocol", "ztna", "security", "ANY-TYPE"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        log_forward: str,
        log_field_exclusion: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemLogForwardLogFieldExclusion", "CliGlobalSystemLogForwardLogFieldExclusionGetResponse"]