"""Type stubs for cli.global.system.admin.user"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminUserGetItem:
    """Item yielded when iterating over CliGlobalSystemAdminUserGetResponse."""

    @property
    def oid(self) -> int: ...
    @property
    def adom(self) -> list[AdomItem]: ...
    @property
    def adom_access(self) -> Literal["all", "specify", "exclude", "per-adom-profile"]: ...
    @property
    def autoreg_user(self) -> Literal["disable", "enable"]: ...
    @property
    def avatar(self) -> str: ...
    @property
    def ca(self) -> str: ...
    @property
    def change_password(self) -> Literal["disable", "enable"]: ...
    @property
    def cors_allow_origin(self) -> str: ...
    @property
    def dashboard(self) -> list[DashboardItem]: ...
    @property
    def dashboard_tabs(self) -> list[DashboardTabsItem]: ...
    @property
    def description(self) -> str: ...
    @property
    def dev_group(self) -> str: ...
    @property
    def email_address(self) -> str: ...
    @property
    def ext_auth_accprofile_override(self) -> Literal["disable", "enable"]: ...
    @property
    def ext_auth_adom_override(self) -> Literal["disable", "enable"]: ...
    @property
    def ext_auth_group_match(self) -> str: ...
    @property
    def fingerprint(self) -> str: ...
    @property
    def first_name(self) -> str: ...
    @property
    def force_password_change(self) -> Literal["disable", "enable"]: ...
    @property
    def fortiai(self) -> Literal["disable", "enable"]: ...
    @property
    def group(self) -> str: ...
    @property
    def ipv6_trusthost1(self) -> str: ...
    @property
    def ipv6_trusthost10(self) -> str: ...
    @property
    def ipv6_trusthost2(self) -> str: ...
    @property
    def ipv6_trusthost3(self) -> str: ...
    @property
    def ipv6_trusthost4(self) -> str: ...
    @property
    def ipv6_trusthost5(self) -> str: ...
    @property
    def ipv6_trusthost6(self) -> str: ...
    @property
    def ipv6_trusthost7(self) -> str: ...
    @property
    def ipv6_trusthost8(self) -> str: ...
    @property
    def ipv6_trusthost9(self) -> str: ...
    @property
    def last_name(self) -> str: ...
    @property
    def ldap_server(self) -> str: ...
    @property
    def login_max(self) -> int: ...
    @property
    def meta_data(self) -> list[MetaDataItem]: ...
    @property
    def mobile_number(self) -> str: ...
    @property
    def old_password(self) -> str: ...
    @property
    def pager_number(self) -> str: ...
    @property
    def password(self) -> str: ...
    @property
    def password_expire(self) -> str: ...
    @property
    def phone_number(self) -> str: ...
    @property
    def policy_block(self) -> list[PolicyBlockItem]: ...
    @property
    def policy_package(self) -> list[PolicyPackageItem]: ...
    @property
    def profileid(self) -> str: ...
    @property
    def radius_server(self) -> str: ...
    @property
    def rpc_permit(self) -> Literal["read-write", "none", "read", "from-profile"]: ...
    @property
    def ssh_public_key1(self) -> list[Any]: ...
    @property
    def ssh_public_key2(self) -> list[Any]: ...
    @property
    def ssh_public_key3(self) -> list[Any]: ...
    @property
    def subject(self) -> str: ...
    @property
    def tacacs_plus_server(self) -> str: ...
    @property
    def th_from_profile(self) -> int: ...
    @property
    def th6_from_profile(self) -> int: ...
    @property
    def trusthost1(self) -> list[Any]: ...
    @property
    def trusthost10(self) -> list[Any]: ...
    @property
    def trusthost2(self) -> list[Any]: ...
    @property
    def trusthost3(self) -> list[Any]: ...
    @property
    def trusthost4(self) -> list[Any]: ...
    @property
    def trusthost5(self) -> list[Any]: ...
    @property
    def trusthost6(self) -> list[Any]: ...
    @property
    def trusthost7(self) -> list[Any]: ...
    @property
    def trusthost8(self) -> list[Any]: ...
    @property
    def trusthost9(self) -> list[Any]: ...
    @property
    def two_factor_auth(self) -> Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"]: ...
    @property
    def use_global_theme(self) -> Literal["disable", "enable"]: ...
    @property
    def user_theme(self) -> Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"]: ...
    @property
    def user_type(self) -> Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"]: ...
    @property
    def userid(self) -> str: ...
    @property
    def wildcard(self) -> Literal["disable", "enable"]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class AdomItem:
    """Nested item type for adom array."""

    @property
    def adom_name(self) -> str: ...

class DashboardItem:
    """Nested item type for dashboard array."""

    @property
    def column(self) -> int: ...
    @property
    def diskio_content_type(self) -> Literal["util", "iops", "blks"]: ...
    @property
    def diskio_period(self) -> Literal["1hour", "8hour", "24hour"]: ...
    @property
    def log_rate_period(self) -> Literal["2min ", "1hour", "6hours"]: ...
    @property
    def log_rate_topn(self) -> Literal["1", "2", "3", "4", "5"]: ...
    @property
    def log_rate_type(self) -> Literal["log", "device"]: ...
    @property
    def moduleid(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def num_entries(self) -> int: ...
    @property
    def refresh_interval(self) -> int: ...
    @property
    def res_cpu_display(self) -> Literal["average ", "each"]: ...
    @property
    def res_period(self) -> Literal["10min ", "hour", "day"]: ...
    @property
    def res_view_type(self) -> Literal["real-time ", "history"]: ...
    @property
    def status(self) -> Literal["close", "open"]: ...
    @property
    def tabid(self) -> int: ...
    @property
    def time_period(self) -> Literal["1hour", "8hour", "24hour"]: ...
    @property
    def widget_type(self) -> Literal["top-lograte", "sysres", "sysinfo", "licinfo", "jsconsole", "sysop", "alert", "statistics", "rpteng", "raid", "logrecv", "devsummary", "logdb-perf", "logdb-lag", "disk-io", "log-rcvd-fwd"]: ...

class DashboardTabsItem:
    """Nested item type for dashboard-tabs array."""

    @property
    def name(self) -> str: ...
    @property
    def tabid(self) -> int: ...

class MetaDataItem:
    """Nested item type for meta-data array."""

    @property
    def fieldlength(self) -> int: ...
    @property
    def fieldname(self) -> str: ...
    @property
    def fieldvalue(self) -> str: ...
    @property
    def importance(self) -> Literal["optional", "required"]: ...
    @property
    def status(self) -> Literal["disabled", "enabled"]: ...

class PolicyBlockItem:
    """Nested item type for policy-block array."""

    @property
    def policy_block_name(self) -> str: ...

class PolicyPackageItem:
    """Nested item type for policy-package array."""

    @property
    def policy_package_name(self) -> str: ...


class CliGlobalSystemAdminUserGetResponse(FortiAnalyzerResponse):
    """Typed response for CliGlobalSystemAdminUserGet endpoint with autocomplete support."""

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
    def adom(self) -> list[AdomItem]:
        """Field: adom"""
        ...

    @property
    def adom_access(self) -> Literal["all", "specify", "exclude", "per-adom-profile"] | None:
        """Field: adom-access"""
        ...

    @property
    def autoreg_user(self) -> Literal["disable", "enable"] | None:
        """Field: autoreg-user"""
        ...

    @property
    def avatar(self) -> str | None:
        """Field: avatar"""
        ...

    @property
    def ca(self) -> str | None:
        """Field: ca"""
        ...

    @property
    def change_password(self) -> Literal["disable", "enable"] | None:
        """Field: change-password"""
        ...

    @property
    def cors_allow_origin(self) -> str | None:
        """Field: cors-allow-origin"""
        ...

    @property
    def dashboard(self) -> list[DashboardItem]:
        """Field: dashboard"""
        ...

    @property
    def dashboard_tabs(self) -> list[DashboardTabsItem]:
        """Field: dashboard-tabs"""
        ...

    @property
    def description(self) -> str | None:
        """Field: description"""
        ...

    @property
    def dev_group(self) -> str | None:
        """Field: dev-group"""
        ...

    @property
    def email_address(self) -> str | None:
        """Field: email-address"""
        ...

    @property
    def ext_auth_accprofile_override(self) -> Literal["disable", "enable"] | None:
        """Field: ext-auth-accprofile-override"""
        ...

    @property
    def ext_auth_adom_override(self) -> Literal["disable", "enable"] | None:
        """Field: ext-auth-adom-override"""
        ...

    @property
    def ext_auth_group_match(self) -> str | None:
        """Field: ext-auth-group-match"""
        ...

    @property
    def fingerprint(self) -> str | None:
        """Field: fingerprint"""
        ...

    @property
    def first_name(self) -> str | None:
        """Field: first-name"""
        ...

    @property
    def force_password_change(self) -> Literal["disable", "enable"] | None:
        """Field: force-password-change"""
        ...

    @property
    def fortiai(self) -> Literal["disable", "enable"] | None:
        """Field: fortiai"""
        ...

    @property
    def group(self) -> str | None:
        """Field: group"""
        ...

    @property
    def ipv6_trusthost1(self) -> str | None:
        """Field: ipv6_trusthost1"""
        ...

    @property
    def ipv6_trusthost10(self) -> str | None:
        """Field: ipv6_trusthost10"""
        ...

    @property
    def ipv6_trusthost2(self) -> str | None:
        """Field: ipv6_trusthost2"""
        ...

    @property
    def ipv6_trusthost3(self) -> str | None:
        """Field: ipv6_trusthost3"""
        ...

    @property
    def ipv6_trusthost4(self) -> str | None:
        """Field: ipv6_trusthost4"""
        ...

    @property
    def ipv6_trusthost5(self) -> str | None:
        """Field: ipv6_trusthost5"""
        ...

    @property
    def ipv6_trusthost6(self) -> str | None:
        """Field: ipv6_trusthost6"""
        ...

    @property
    def ipv6_trusthost7(self) -> str | None:
        """Field: ipv6_trusthost7"""
        ...

    @property
    def ipv6_trusthost8(self) -> str | None:
        """Field: ipv6_trusthost8"""
        ...

    @property
    def ipv6_trusthost9(self) -> str | None:
        """Field: ipv6_trusthost9"""
        ...

    @property
    def last_name(self) -> str | None:
        """Field: last-name"""
        ...

    @property
    def ldap_server(self) -> str | None:
        """Field: ldap-server"""
        ...

    @property
    def login_max(self) -> int | None:
        """Field: login-max"""
        ...

    @property
    def meta_data(self) -> list[MetaDataItem]:
        """Field: meta-data"""
        ...

    @property
    def mobile_number(self) -> str | None:
        """Field: mobile-number"""
        ...

    @property
    def old_password(self) -> str | None:
        """Field: old-password"""
        ...

    @property
    def pager_number(self) -> str | None:
        """Field: pager-number"""
        ...

    @property
    def password(self) -> str | None:
        """Field: password"""
        ...

    @property
    def password_expire(self) -> str | None:
        """Field: password-expire"""
        ...

    @property
    def phone_number(self) -> str | None:
        """Field: phone-number"""
        ...

    @property
    def policy_block(self) -> list[PolicyBlockItem]:
        """Field: policy-block"""
        ...

    @property
    def policy_package(self) -> list[PolicyPackageItem]:
        """Field: policy-package"""
        ...

    @property
    def profileid(self) -> str | None:
        """Field: profileid"""
        ...

    @property
    def radius_server(self) -> str | None:
        """Field: radius_server"""
        ...

    @property
    def rpc_permit(self) -> Literal["read-write", "none", "read", "from-profile"] | None:
        """Field: rpc-permit"""
        ...

    @property
    def ssh_public_key1(self) -> list[Any] | None:
        """Field: ssh-public-key1"""
        ...

    @property
    def ssh_public_key2(self) -> list[Any] | None:
        """Field: ssh-public-key2"""
        ...

    @property
    def ssh_public_key3(self) -> list[Any] | None:
        """Field: ssh-public-key3"""
        ...

    @property
    def subject(self) -> str | None:
        """Field: subject"""
        ...

    @property
    def tacacs_plus_server(self) -> str | None:
        """Field: tacacs-plus-server"""
        ...

    @property
    def th_from_profile(self) -> int | None:
        """Field: th-from-profile"""
        ...

    @property
    def th6_from_profile(self) -> int | None:
        """Field: th6-from-profile"""
        ...

    @property
    def trusthost1(self) -> list[Any] | None:
        """Field: trusthost1"""
        ...

    @property
    def trusthost10(self) -> list[Any] | None:
        """Field: trusthost10"""
        ...

    @property
    def trusthost2(self) -> list[Any] | None:
        """Field: trusthost2"""
        ...

    @property
    def trusthost3(self) -> list[Any] | None:
        """Field: trusthost3"""
        ...

    @property
    def trusthost4(self) -> list[Any] | None:
        """Field: trusthost4"""
        ...

    @property
    def trusthost5(self) -> list[Any] | None:
        """Field: trusthost5"""
        ...

    @property
    def trusthost6(self) -> list[Any] | None:
        """Field: trusthost6"""
        ...

    @property
    def trusthost7(self) -> list[Any] | None:
        """Field: trusthost7"""
        ...

    @property
    def trusthost8(self) -> list[Any] | None:
        """Field: trusthost8"""
        ...

    @property
    def trusthost9(self) -> list[Any] | None:
        """Field: trusthost9"""
        ...

    @property
    def two_factor_auth(self) -> Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None:
        """Field: two-factor-auth"""
        ...

    @property
    def use_global_theme(self) -> Literal["disable", "enable"] | None:
        """Field: use-global-theme"""
        ...

    @property
    def user_theme(self) -> Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None:
        """Field: user-theme"""
        ...

    @property
    def user_type(self) -> Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None:
        """Field: user_type"""
        ...

    @property
    def userid(self) -> str | None:
        """Field: userid"""
        ...

    @property
    def wildcard(self) -> Literal["disable", "enable"] | None:
        """Field: wildcard"""
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
    def __iter__(self) -> Iterator[CliGlobalSystemAdminUserGetItem]: ...
    def __len__(self) -> int: ...


class CliGlobalSystemAdminUser:
    """FortiAnalyzer endpoint: cli.global.system.admin.user"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        user: int | str | None = None,
        fields: list[Literal["adom-access", "autoreg-user", "avatar", "ca", "change-password", "cors-allow-origin", "description", "dev-group", "email-address", "ext-auth-accprofile-override", "ext-auth-adom-override", "ext-auth-group-match", "fingerprint", "first-name", "force-password-change", "fortiai", "group", "ipv6_trusthost1", "ipv6_trusthost10", "ipv6_trusthost2", "ipv6_trusthost3", "ipv6_trusthost4", "ipv6_trusthost5", "ipv6_trusthost6", "ipv6_trusthost7", "ipv6_trusthost8", "ipv6_trusthost9", "last-name", "ldap-server", "login-max", "mobile-number", "old-password", "pager-number", "password", "password-expire", "phone-number", "profileid", "radius_server", "rpc-permit", "ssh-public-key1", "ssh-public-key2", "ssh-public-key3", "subject", "tacacs-plus-server", "th-from-profile", "th6-from-profile", "trusthost1", "trusthost10", "trusthost2", "trusthost3", "trusthost4", "trusthost5", "trusthost6", "trusthost7", "trusthost8", "trusthost9", "two-factor-auth", "use-global-theme", "user-theme", "user_type", "userid", "wildcard"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None,
    ) -> CliGlobalSystemAdminUserGetResponse:
        """GET operation."""
        ...

    def add(
        self,
        user: int | str | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify", "exclude", "per-adom-profile"] | None = None,
        autoreg_user: Literal["disable", "enable"] | None = None,
        avatar: str | None = None,
        ca: str | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        cors_allow_origin: str | None = None,
        dashboard: list[dict[str, Any]] | None = None,
        dashboard_tabs: list[dict[str, Any]] | None = None,
        description: str | None = None,
        dev_group: str | None = None,
        email_address: str | None = None,
        ext_auth_accprofile_override: Literal["disable", "enable"] | None = None,
        ext_auth_adom_override: Literal["disable", "enable"] | None = None,
        ext_auth_group_match: str | None = None,
        fingerprint: str | None = None,
        first_name: str | None = None,
        force_password_change: Literal["disable", "enable"] | None = None,
        fortiai: Literal["disable", "enable"] | None = None,
        group: str | None = None,
        ipv6_trusthost1: str | None = None,
        ipv6_trusthost10: str | None = None,
        ipv6_trusthost2: str | None = None,
        ipv6_trusthost3: str | None = None,
        ipv6_trusthost4: str | None = None,
        ipv6_trusthost5: str | None = None,
        ipv6_trusthost6: str | None = None,
        ipv6_trusthost7: str | None = None,
        ipv6_trusthost8: str | None = None,
        ipv6_trusthost9: str | None = None,
        last_name: str | None = None,
        ldap_server: str | None = None,
        login_max: int | None = None,
        meta_data: list[dict[str, Any]] | None = None,
        mobile_number: str | None = None,
        old_password: str | None = None,
        pager_number: str | None = None,
        password: str | None = None,
        password_expire: str | None = None,
        phone_number: str | None = None,
        policy_block: list[dict[str, Any]] | None = None,
        policy_package: list[dict[str, Any]] | None = None,
        profileid: str | None = None,
        radius_server: str | None = None,
        rpc_permit: Literal["read-write", "none", "read", "from-profile"] | None = None,
        ssh_public_key1: list[Any] | None = None,
        ssh_public_key2: list[Any] | None = None,
        ssh_public_key3: list[Any] | None = None,
        subject: str | None = None,
        tacacs_plus_server: str | None = None,
        th_from_profile: int | None = None,
        th6_from_profile: int | None = None,
        trusthost1: list[Any] | None = None,
        trusthost10: list[Any] | None = None,
        trusthost2: list[Any] | None = None,
        trusthost3: list[Any] | None = None,
        trusthost4: list[Any] | None = None,
        trusthost5: list[Any] | None = None,
        trusthost6: list[Any] | None = None,
        trusthost7: list[Any] | None = None,
        trusthost8: list[Any] | None = None,
        trusthost9: list[Any] | None = None,
        two_factor_auth: Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None = None,
        use_global_theme: Literal["disable", "enable"] | None = None,
        user_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        user_type: Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None = None,
        userid: str | None = None,
        wildcard: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def set(
        self,
        user: int | str | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify", "exclude", "per-adom-profile"] | None = None,
        autoreg_user: Literal["disable", "enable"] | None = None,
        avatar: str | None = None,
        ca: str | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        cors_allow_origin: str | None = None,
        dashboard: list[dict[str, Any]] | None = None,
        dashboard_tabs: list[dict[str, Any]] | None = None,
        description: str | None = None,
        dev_group: str | None = None,
        email_address: str | None = None,
        ext_auth_accprofile_override: Literal["disable", "enable"] | None = None,
        ext_auth_adom_override: Literal["disable", "enable"] | None = None,
        ext_auth_group_match: str | None = None,
        fingerprint: str | None = None,
        first_name: str | None = None,
        force_password_change: Literal["disable", "enable"] | None = None,
        fortiai: Literal["disable", "enable"] | None = None,
        group: str | None = None,
        ipv6_trusthost1: str | None = None,
        ipv6_trusthost10: str | None = None,
        ipv6_trusthost2: str | None = None,
        ipv6_trusthost3: str | None = None,
        ipv6_trusthost4: str | None = None,
        ipv6_trusthost5: str | None = None,
        ipv6_trusthost6: str | None = None,
        ipv6_trusthost7: str | None = None,
        ipv6_trusthost8: str | None = None,
        ipv6_trusthost9: str | None = None,
        last_name: str | None = None,
        ldap_server: str | None = None,
        login_max: int | None = None,
        meta_data: list[dict[str, Any]] | None = None,
        mobile_number: str | None = None,
        old_password: str | None = None,
        pager_number: str | None = None,
        password: str | None = None,
        password_expire: str | None = None,
        phone_number: str | None = None,
        policy_block: list[dict[str, Any]] | None = None,
        policy_package: list[dict[str, Any]] | None = None,
        profileid: str | None = None,
        radius_server: str | None = None,
        rpc_permit: Literal["read-write", "none", "read", "from-profile"] | None = None,
        ssh_public_key1: list[Any] | None = None,
        ssh_public_key2: list[Any] | None = None,
        ssh_public_key3: list[Any] | None = None,
        subject: str | None = None,
        tacacs_plus_server: str | None = None,
        th_from_profile: int | None = None,
        th6_from_profile: int | None = None,
        trusthost1: list[Any] | None = None,
        trusthost10: list[Any] | None = None,
        trusthost2: list[Any] | None = None,
        trusthost3: list[Any] | None = None,
        trusthost4: list[Any] | None = None,
        trusthost5: list[Any] | None = None,
        trusthost6: list[Any] | None = None,
        trusthost7: list[Any] | None = None,
        trusthost8: list[Any] | None = None,
        trusthost9: list[Any] | None = None,
        two_factor_auth: Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None = None,
        use_global_theme: Literal["disable", "enable"] | None = None,
        user_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        user_type: Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None = None,
        userid: str | None = None,
        wildcard: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """SET operation."""
        ...

    def update(
        self,
        user: int | str | None = None,
        adom: list[dict[str, Any]] | None = None,
        adom_access: Literal["all", "specify", "exclude", "per-adom-profile"] | None = None,
        autoreg_user: Literal["disable", "enable"] | None = None,
        avatar: str | None = None,
        ca: str | None = None,
        change_password: Literal["disable", "enable"] | None = None,
        cors_allow_origin: str | None = None,
        dashboard: list[dict[str, Any]] | None = None,
        dashboard_tabs: list[dict[str, Any]] | None = None,
        description: str | None = None,
        dev_group: str | None = None,
        email_address: str | None = None,
        ext_auth_accprofile_override: Literal["disable", "enable"] | None = None,
        ext_auth_adom_override: Literal["disable", "enable"] | None = None,
        ext_auth_group_match: str | None = None,
        fingerprint: str | None = None,
        first_name: str | None = None,
        force_password_change: Literal["disable", "enable"] | None = None,
        fortiai: Literal["disable", "enable"] | None = None,
        group: str | None = None,
        ipv6_trusthost1: str | None = None,
        ipv6_trusthost10: str | None = None,
        ipv6_trusthost2: str | None = None,
        ipv6_trusthost3: str | None = None,
        ipv6_trusthost4: str | None = None,
        ipv6_trusthost5: str | None = None,
        ipv6_trusthost6: str | None = None,
        ipv6_trusthost7: str | None = None,
        ipv6_trusthost8: str | None = None,
        ipv6_trusthost9: str | None = None,
        last_name: str | None = None,
        ldap_server: str | None = None,
        login_max: int | None = None,
        meta_data: list[dict[str, Any]] | None = None,
        mobile_number: str | None = None,
        old_password: str | None = None,
        pager_number: str | None = None,
        password: str | None = None,
        password_expire: str | None = None,
        phone_number: str | None = None,
        policy_block: list[dict[str, Any]] | None = None,
        policy_package: list[dict[str, Any]] | None = None,
        profileid: str | None = None,
        radius_server: str | None = None,
        rpc_permit: Literal["read-write", "none", "read", "from-profile"] | None = None,
        ssh_public_key1: list[Any] | None = None,
        ssh_public_key2: list[Any] | None = None,
        ssh_public_key3: list[Any] | None = None,
        subject: str | None = None,
        tacacs_plus_server: str | None = None,
        th_from_profile: int | None = None,
        th6_from_profile: int | None = None,
        trusthost1: list[Any] | None = None,
        trusthost10: list[Any] | None = None,
        trusthost2: list[Any] | None = None,
        trusthost3: list[Any] | None = None,
        trusthost4: list[Any] | None = None,
        trusthost5: list[Any] | None = None,
        trusthost6: list[Any] | None = None,
        trusthost7: list[Any] | None = None,
        trusthost8: list[Any] | None = None,
        trusthost9: list[Any] | None = None,
        two_factor_auth: Literal["disable", "password", "ftc-ftm", "ftc-email", "ftc-sms"] | None = None,
        use_global_theme: Literal["disable", "enable"] | None = None,
        user_theme: Literal["mariner", "jade", "neutrino", "dark-matter", "spring", "summer", "autumn", "winter", "circuit-board", "calla-lily", "binary-tunnel", "mars", "blue-sea", "technology", "forest", "twilight", "canyon", "northern-light", "astronomy", "fish", "penguin", "mountain", "panda", "cat", "cave", "zebra", "contrast-dark", "graphite"] | None = None,
        user_type: Literal["local", "radius", "ldap", "tacacs-plus", "pki-auth", "group", "sso", "api"] | None = None,
        userid: str | None = None,
        wildcard: Literal["disable", "enable"] | None = None,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        user: int | str | None = None,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...


__all__ = ["CliGlobalSystemAdminUser", "CliGlobalSystemAdminUserGetResponse"]