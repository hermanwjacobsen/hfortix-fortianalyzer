"""Type stubs for cli.global.fmupdate.fds-setting"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalFmupdateFdsSettingGetItem:
    """Item yielded when iterating over CliGlobalFmupdateFdsSettingGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def User_Agent(self) -> str: ...
    @property
    def controller_contract_download(self) -> Literal["disable", "enable"]: ...
    @property
    def fds_clt_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def fds_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"]: ...
    @property
    def fmtr_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"]: ...
    @property
    def fortiguard_anycast(self) -> Literal["disable", "enable"]: ...
    @property
    def fortiguard_anycast_source(self) -> Literal["fortinet", "aws"]: ...
    @property
    def linkd_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"]: ...
    @property
    def max_av_ips_version(self) -> int: ...
    @property
    def max_work(self) -> int: ...
    @property
    def push_override(self) -> dict[str, Any]: ...
    @property
    def push_override_to_client(self) -> dict[str, Any]: ...
    @property
    def send_report(self) -> Literal["disable", "enable"]: ...
    @property
    def send_setup(self) -> Literal["disable", "enable"]: ...
    @property
    def server_override(self) -> dict[str, Any]: ...
    @property
    def system_support_fai(self) -> list[Any]: ...
    @property
    def system_support_faz(self) -> list[Any]: ...
    @property
    def system_support_fct(self) -> list[Any]: ...
    @property
    def system_support_fdc(self) -> list[Any]: ...
    @property
    def system_support_fgt(self) -> list[Any]: ...
    @property
    def system_support_fis(self) -> list[Any]: ...
    @property
    def system_support_fml(self) -> list[Any]: ...
    @property
    def system_support_fsa(self) -> list[Any]: ...
    @property
    def system_support_fts(self) -> list[Any]: ...
    @property
    def umsvc_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"]: ...
    @property
    def unreg_dev_option(self) -> Literal["ignore", "svc-only", "add-service"]: ...
    @property
    def update_schedule(self) -> dict[str, Any]: ...
    @property
    def wanip_query_mode(self) -> Literal["disable", "ipify"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class CliGlobalFmupdateFdsSettingGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalFmupdateFdsSettingGet endpoint with autocomplete support."""

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
    def User_Agent(self) -> str | None:
        """Field: User-Agent"""
        ...

    @property
    def controller_contract_download(self) -> Literal["disable", "enable"] | None:
        """Field: controller-contract-download"""
        ...

    @property
    def fds_clt_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: fds-clt-ssl-protocol"""
        ...

    @property
    def fds_ssl_protocol(self) -> Literal["sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None:
        """Field: fds-ssl-protocol"""
        ...

    @property
    def fmtr_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None:
        """Field: fmtr-log"""
        ...

    @property
    def fortiguard_anycast(self) -> Literal["disable", "enable"] | None:
        """Field: fortiguard-anycast"""
        ...

    @property
    def fortiguard_anycast_source(self) -> Literal["fortinet", "aws"] | None:
        """Field: fortiguard-anycast-source"""
        ...

    @property
    def linkd_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None:
        """Field: linkd-log"""
        ...

    @property
    def max_av_ips_version(self) -> int | None:
        """Field: max-av-ips-version"""
        ...

    @property
    def max_work(self) -> int | None:
        """Field: max-work"""
        ...

    @property
    def push_override(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.fmupdate.fds-setting.push-override)."""
        ...

    @property
    def push_override_to_client(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.fmupdate.fds-setting.push-override-to-client)."""
        ...

    @property
    def send_report(self) -> Literal["disable", "enable"] | None:
        """Field: send_report"""
        ...

    @property
    def send_setup(self) -> Literal["disable", "enable"] | None:
        """Field: send_setup"""
        ...

    @property
    def server_override(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.fmupdate.fds-setting.server-override)."""
        ...

    @property
    def system_support_fai(self) -> list[Any] | None:
        """Field: system-support-fai"""
        ...

    @property
    def system_support_faz(self) -> list[Any] | None:
        """Field: system-support-faz"""
        ...

    @property
    def system_support_fct(self) -> list[Any] | None:
        """Field: system-support-fct"""
        ...

    @property
    def system_support_fdc(self) -> list[Any] | None:
        """Field: system-support-fdc"""
        ...

    @property
    def system_support_fgt(self) -> list[Any] | None:
        """Field: system-support-fgt"""
        ...

    @property
    def system_support_fis(self) -> list[Any] | None:
        """Field: system-support-fis"""
        ...

    @property
    def system_support_fml(self) -> list[Any] | None:
        """Field: system-support-fml"""
        ...

    @property
    def system_support_fsa(self) -> list[Any] | None:
        """Field: system-support-fsa"""
        ...

    @property
    def system_support_fts(self) -> list[Any] | None:
        """Field: system-support-fts"""
        ...

    @property
    def umsvc_log(self) -> Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None:
        """Field: umsvc-log"""
        ...

    @property
    def unreg_dev_option(self) -> Literal["ignore", "svc-only", "add-service"] | None:
        """Field: unreg-dev-option"""
        ...

    @property
    def update_schedule(self) -> dict[str, Any] | None:
        """Nested object (schema: cli.fmupdate.fds-setting.update-schedule)."""
        ...

    @property
    def wanip_query_mode(self) -> Literal["disable", "ipify"] | None:
        """Field: wanip-query-mode"""
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
    def __iter__(self) -> Iterator[CliGlobalFmupdateFdsSettingGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalFmupdateFdsSetting:
    """FortiAnalyzer endpoint: cli.global.fmupdate.fds-setting"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
    ) -> CliGlobalFmupdateFdsSettingGetResponse:
        """GET operation."""
        ...

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
        push_override: dict[str, Any] | None = None,
        push_override_to_client: dict[str, Any] | None = None,
        send_report: Literal["disable", "enable"] | None = None,
        send_setup: Literal["disable", "enable"] | None = None,
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
        umsvc_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        unreg_dev_option: Literal["ignore", "svc-only", "add-service"] | None = None,
        update_schedule: dict[str, Any] | None = None,
        wanip_query_mode: Literal["disable", "ipify"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

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
        push_override: dict[str, Any] | None = None,
        push_override_to_client: dict[str, Any] | None = None,
        send_report: Literal["disable", "enable"] | None = None,
        send_setup: Literal["disable", "enable"] | None = None,
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
        umsvc_log: Literal["emergency", "alert", "critical", "error", "warn", "notice", "info", "debug", "disable"] | None = None,
        unreg_dev_option: Literal["ignore", "svc-only", "add-service"] | None = None,
        update_schedule: dict[str, Any] | None = None,
        wanip_query_mode: Literal["disable", "ipify"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...


__all__ = ["CliGlobalFmupdateFdsSetting", "CliGlobalFmupdateFdsSettingGetResponse"]