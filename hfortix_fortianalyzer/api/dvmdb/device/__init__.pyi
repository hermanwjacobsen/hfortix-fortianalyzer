"""Type stubs for dvmdb.device"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class VdomItem:
    """Nested item type for vdom array."""

    @property
    def comments(self) -> str: ...
    @property
    def meta_fields(self) -> dict[str, Any]: ...
    @property
    def name(self) -> str: ...
    @property
    def opmode(self) -> Literal["nat", "transparent"]: ...
    @property
    def rtm_prof_id(self) -> int: ...
    @property
    def status(self) -> str: ...
    @property
    def vdom_type(self) -> Literal["traffic", "admin"]: ...
    @property
    def vpn_id(self) -> int: ...


class DvmdbDeviceGetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbDevice endpoint with autocomplete support."""

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
    def adm_pass(self) -> list[Any] | None:
        """Field: adm_pass"""
        ...

    @property
    def adm_usr(self) -> str | None:
        """Field: adm_usr"""
        ...

    @property
    def app_ver(self) -> str | None:
        """Field: app_ver"""
        ...

    @property
    def av_ver(self) -> str | None:
        """Field: av_ver"""
        ...

    @property
    def beta(self) -> int | None:
        """Field: beta"""
        ...

    @property
    def branch_pt(self) -> int | None:
        """Field: branch_pt"""
        ...

    @property
    def build(self) -> int | None:
        """Field: build"""
        ...

    @property
    def checksum(self) -> str | None:
        """Field: checksum"""
        ...

    @property
    def cluster_worker(self) -> list[Any] | None:
        """Field: cluster_worker"""
        ...

    @property
    def conf_status(self) -> Literal["unknown", "insync", "outofsync"] | None:
        """Field: conf_status"""
        ...

    @property
    def conn_mode(self) -> Literal["active", "passive"] | None:
        """Field: conn_mode"""
        ...

    @property
    def conn_status(self) -> Literal["UNKNOWN", "up", "down"] | None:
        """Field: conn_status"""
        ...

    @property
    def db_status(self) -> Literal["unknown", "nomod", "mod"] | None:
        """Field: db_status"""
        ...

    @property
    def desc(self) -> str | None:
        """Field: desc"""
        ...

    @property
    def dev_status(self) -> Literal["none", "unknown", "checkedin", "inprogress", "installed", "aborted", "sched", "retry", "canceled", "pending", "retrieved", "changed_conf", "sync_fail", "timeout", "rev_revert", "auto_updated"] | None:
        """Field: dev_status"""
        ...

    @property
    def eip(self) -> str | None:
        """Field: eip"""
        ...

    @property
    def fap_cnt(self) -> int | None:
        """Field: fap_cnt"""
        ...

    @property
    def faz_full_act(self) -> int | None:
        """Field: faz.full_act"""
        ...

    @property
    def faz_perm(self) -> int | None:
        """Field: faz.perm"""
        ...

    @property
    def faz_quota(self) -> int | None:
        """Field: faz.quota"""
        ...

    @property
    def faz_used(self) -> int | None:
        """Field: faz.used"""
        ...

    @property
    def fex_cnt(self) -> int | None:
        """Field: fex_cnt"""
        ...

    @property
    def first_tunnel_up(self) -> int | None:
        """Field: first_tunnel_up"""
        ...

    @property
    def flags(self) -> list[Any] | None:
        """Field: flags"""
        ...

    @property
    def foslic_cpu(self) -> int | None:
        """VM Meter vCPU count."""
        ...

    @property
    def foslic_dr_site(self) -> Literal["disable", "enable"] | None:
        """VM Meter DR Site status."""
        ...

    @property
    def foslic_inst_time(self) -> int | None:
        """VM Meter first deployment time (in UNIX timestamp)."""
        ...

    @property
    def foslic_last_sync(self) -> int | None:
        """VM Meter last synchronized time (in UNIX timestamp)."""
        ...

    @property
    def foslic_ram(self) -> int | None:
        """VM Meter device RAM size (in MB)."""
        ...

    @property
    def foslic_type(self) -> Literal["temporary", "trial", "regular", "trial_expired"] | None:
        """VM Meter license type."""
        ...

    @property
    def foslic_utm(self) -> list[Any] | None:
        """VM Meter services<br/><b>fw</b> - Firewall<br/><b>av</b> - Anti-virus<br/><b>..."""
        ...

    @property
    def fsw_cnt(self) -> int | None:
        """Field: fsw_cnt"""
        ...

    @property
    def ha_vsn(self) -> str | None:
        """Field: ha.vsn"""
        ...

    @property
    def ha_group_id(self) -> int | None:
        """Field: ha_group_id"""
        ...

    @property
    def ha_group_name(self) -> str | None:
        """Field: ha_group_name"""
        ...

    @property
    def ha_mode(self) -> Literal["standalone", "AP", "AA", "ELBC", "DUAL", "fmg-enabled", "autoscale", "unknown"] | None:
        """Field: ha_mode"""
        ...

    @property
    def ha_upgrade_mode(self) -> int | None:
        """Field: ha_upgrade_mode"""
        ...

    @property
    def hdisk_size(self) -> int | None:
        """Field: hdisk_size"""
        ...

    @property
    def hostname(self) -> str | None:
        """Field: hostname"""
        ...

    @property
    def hw_generation(self) -> int | None:
        """Field: hw_generation"""
        ...

    @property
    def hw_rev_major(self) -> int | None:
        """Field: hw_rev_major"""
        ...

    @property
    def hw_rev_minor(self) -> int | None:
        """Field: hw_rev_minor"""
        ...

    @property
    def hyperscale(self) -> int | None:
        """Field: hyperscale"""
        ...

    @property
    def ip(self) -> str | None:
        """Field: ip"""
        ...

    @property
    def ips_ext(self) -> int | None:
        """Field: ips_ext"""
        ...

    @property
    def ips_ver(self) -> str | None:
        """Field: ips_ver"""
        ...

    @property
    def last_checked(self) -> int | None:
        """Field: last_checked"""
        ...

    @property
    def last_resync(self) -> int | None:
        """Field: last_resync"""
        ...

    @property
    def latitude(self) -> str | None:
        """Field: latitude"""
        ...

    @property
    def lic_flags(self) -> int | None:
        """Field: lic_flags"""
        ...

    @property
    def lic_region(self) -> str | None:
        """Field: lic_region"""
        ...

    @property
    def location_from(self) -> str | None:
        """Field: location_from"""
        ...

    @property
    def logdisk_size(self) -> int | None:
        """Field: logdisk_size"""
        ...

    @property
    def longitude(self) -> str | None:
        """Field: longitude"""
        ...

    @property
    def maxvdom(self) -> int | None:
        """Field: maxvdom"""
        ...

    @property
    def meta_fields(self) -> dict[str, Any] | None:
        """Default metafields: "Contact Phone Number", "Contact Email", "Company/Organiz..."""
        ...

    @property
    def mgmt_if(self) -> str | None:
        """Field: mgmt_if"""
        ...

    @property
    def mgmt_mode(self) -> Literal["unreg", "fmg", "faz", "fmgfaz"] | None:
        """Field: mgmt_mode"""
        ...

    @property
    def mgmt_uuid(self) -> str | None:
        """Field: mgmt_uuid"""
        ...

    @property
    def mgt_vdom(self) -> str | None:
        """Field: mgt_vdom"""
        ...

    @property
    def module_sn(self) -> str | None:
        """Field: module_sn"""
        ...

    @property
    def mr(self) -> int | None:
        """Field: mr"""
        ...

    @property
    def name(self) -> str | None:
        """Unique name for the device."""
        ...

    @property
    def nsxt_service_name(self) -> str | None:
        """Field: nsxt_service_name"""
        ...

    @property
    def os_type(self) -> Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None:
        """Field: os_type"""
        ...

    @property
    def os_ver(self) -> Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None:
        """Field: os_ver"""
        ...

    @property
    def patch(self) -> int | None:
        """Field: patch"""
        ...

    @property
    def platform_str(self) -> str | None:
        """Field: platform_str"""
        ...

    @property
    def prefer_img_ver(self) -> str | None:
        """Field: prefer_img_ver"""
        ...

    @property
    def prio(self) -> int | None:
        """Field: prio"""
        ...

    @property
    def private_key(self) -> str | None:
        """Field: private_key"""
        ...

    @property
    def private_key_status(self) -> int | None:
        """Field: private_key_status"""
        ...

    @property
    def psk(self) -> str | None:
        """Field: psk"""
        ...

    @property
    def relver_info(self) -> str | None:
        """Field: relver_info"""
        ...

    @property
    def role(self) -> Literal["master", "ha-slave", "autoscale-slave"] | None:
        """Field: role"""
        ...

    @property
    def sn(self) -> str | None:
        """Unique value for each device."""
        ...

    @property
    def sov_sase_license(self) -> str | None:
        """Field: sov_sase_license"""
        ...

    @property
    def tunnel_sn(self) -> str | None:
        """Field: tunnel_sn"""
        ...

    @property
    def vdom(self) -> list[VdomItem]:
        """Field: vdom"""
        ...

    @property
    def version(self) -> int | None:
        """Field: version"""
        ...

    @property
    def vm_cpu(self) -> int | None:
        """Field: vm_cpu"""
        ...

    @property
    def vm_cpu_limit(self) -> int | None:
        """Field: vm_cpu_limit"""
        ...

    @property
    def vm_lic_expire(self) -> int | None:
        """Field: vm_lic_expire"""
        ...

    @property
    def vm_lic_overdue_since(self) -> int | None:
        """Field: vm_lic_overdue_since"""
        ...

    @property
    def vm_mem(self) -> int | None:
        """Field: vm_mem"""
        ...

    @property
    def vm_mem_limit(self) -> int | None:
        """Field: vm_mem_limit"""
        ...

    @property
    def vm_payg_status(self) -> int | None:
        """Field: vm_payg_status"""
        ...

    @property
    def vm_status(self) -> Literal["N/A", "No License", "Startup", "Valid", "Pending", "Warning", "Invalid", "Invalid Copy", "Evaluation Expired", "Evaluation", "Expires Soon", "Expired", "Grace Period", "Validation Overdue"] | None:
        """Field: vm_status"""
        ...

    class DvmdbDeviceItem:
        """Item yielded when iterating over DvmdbDeviceResponse."""

        @property
        def oid(self) -> int: ...
        @property
        def adm_pass(self) -> list[Any]: ...
        @property
        def adm_usr(self) -> str: ...
        @property
        def app_ver(self) -> str: ...
        @property
        def av_ver(self) -> str: ...
        @property
        def beta(self) -> int: ...
        @property
        def branch_pt(self) -> int: ...
        @property
        def build(self) -> int: ...
        @property
        def checksum(self) -> str: ...
        @property
        def cluster_worker(self) -> list[Any]: ...
        @property
        def conf_status(self) -> Literal["unknown", "insync", "outofsync"]: ...
        @property
        def conn_mode(self) -> Literal["active", "passive"]: ...
        @property
        def conn_status(self) -> Literal["UNKNOWN", "up", "down"]: ...
        @property
        def db_status(self) -> Literal["unknown", "nomod", "mod"]: ...
        @property
        def desc(self) -> str: ...
        @property
        def dev_status(self) -> Literal["none", "unknown", "checkedin", "inprogress", "installed", "aborted", "sched", "retry", "canceled", "pending", "retrieved", "changed_conf", "sync_fail", "timeout", "rev_revert", "auto_updated"]: ...
        @property
        def eip(self) -> str: ...
        @property
        def fap_cnt(self) -> int: ...
        @property
        def faz_full_act(self) -> int: ...
        @property
        def faz_perm(self) -> int: ...
        @property
        def faz_quota(self) -> int: ...
        @property
        def faz_used(self) -> int: ...
        @property
        def fex_cnt(self) -> int: ...
        @property
        def first_tunnel_up(self) -> int: ...
        @property
        def flags(self) -> list[Any]: ...
        @property
        def foslic_cpu(self) -> int: ...
        @property
        def foslic_dr_site(self) -> Literal["disable", "enable"]: ...
        @property
        def foslic_inst_time(self) -> int: ...
        @property
        def foslic_last_sync(self) -> int: ...
        @property
        def foslic_ram(self) -> int: ...
        @property
        def foslic_type(self) -> Literal["temporary", "trial", "regular", "trial_expired"]: ...
        @property
        def foslic_utm(self) -> list[Any]: ...
        @property
        def fsw_cnt(self) -> int: ...
        @property
        def ha_vsn(self) -> str: ...
        @property
        def ha_group_id(self) -> int: ...
        @property
        def ha_group_name(self) -> str: ...
        @property
        def ha_mode(self) -> Literal["standalone", "AP", "AA", "ELBC", "DUAL", "fmg-enabled", "autoscale", "unknown"]: ...
        @property
        def ha_upgrade_mode(self) -> int: ...
        @property
        def hdisk_size(self) -> int: ...
        @property
        def hostname(self) -> str: ...
        @property
        def hw_generation(self) -> int: ...
        @property
        def hw_rev_major(self) -> int: ...
        @property
        def hw_rev_minor(self) -> int: ...
        @property
        def hyperscale(self) -> int: ...
        @property
        def ip(self) -> str: ...
        @property
        def ips_ext(self) -> int: ...
        @property
        def ips_ver(self) -> str: ...
        @property
        def last_checked(self) -> int: ...
        @property
        def last_resync(self) -> int: ...
        @property
        def latitude(self) -> str: ...
        @property
        def lic_flags(self) -> int: ...
        @property
        def lic_region(self) -> str: ...
        @property
        def location_from(self) -> str: ...
        @property
        def logdisk_size(self) -> int: ...
        @property
        def longitude(self) -> str: ...
        @property
        def maxvdom(self) -> int: ...
        @property
        def meta_fields(self) -> dict[str, Any]: ...
        @property
        def mgmt_if(self) -> str: ...
        @property
        def mgmt_mode(self) -> Literal["unreg", "fmg", "faz", "fmgfaz"]: ...
        @property
        def mgmt_uuid(self) -> str: ...
        @property
        def mgt_vdom(self) -> str: ...
        @property
        def module_sn(self) -> str: ...
        @property
        def mr(self) -> int: ...
        @property
        def name(self) -> str: ...
        @property
        def nsxt_service_name(self) -> str: ...
        @property
        def os_type(self) -> Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"]: ...
        @property
        def os_ver(self) -> Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"]: ...
        @property
        def patch(self) -> int: ...
        @property
        def platform_str(self) -> str: ...
        @property
        def prefer_img_ver(self) -> str: ...
        @property
        def prio(self) -> int: ...
        @property
        def private_key(self) -> str: ...
        @property
        def private_key_status(self) -> int: ...
        @property
        def psk(self) -> str: ...
        @property
        def relver_info(self) -> str: ...
        @property
        def role(self) -> Literal["master", "ha-slave", "autoscale-slave"]: ...
        @property
        def sn(self) -> str: ...
        @property
        def sov_sase_license(self) -> str: ...
        @property
        def tunnel_sn(self) -> str: ...
        @property
        def vdom(self) -> list[VdomItem]: ...
        @property
        def version(self) -> int: ...
        @property
        def vm_cpu(self) -> int: ...
        @property
        def vm_cpu_limit(self) -> int: ...
        @property
        def vm_lic_expire(self) -> int: ...
        @property
        def vm_lic_overdue_since(self) -> int: ...
        @property
        def vm_mem(self) -> int: ...
        @property
        def vm_mem_limit(self) -> int: ...
        @property
        def vm_payg_status(self) -> int: ...
        @property
        def vm_status(self) -> Literal["N/A", "No License", "Startup", "Valid", "Pending", "Warning", "Invalid", "Invalid Copy", "Evaluation Expired", "Evaluation", "Expires Soon", "Expired", "Grace Period", "Validation Overdue"]: ...

        # Inherited from FortiAnalyzerObject
        @property
        def raw(self) -> dict[str, Any]: ...
        @property
        def dict(self) -> dict[str, Any]: ...
        @property
        def json(self) -> str: ...
        def __getitem__(self, key: str) -> Any: ...

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
    def __iter__(self) -> Iterator[DvmdbDeviceItem]: ...
    def __len__(self) -> int: ...


class DvmdbDeviceSetResponse(FortiAnalyzerResponse):
    """Typed response for DvmdbDevice endpoint with autocomplete support."""

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
    def name(self) -> str | None:
        """Unique name for the device."""
        ...

    class DvmdbDeviceItem:
        """Item yielded when iterating over DvmdbDeviceResponse."""

        @property
        def name(self) -> str: ...

        # Inherited from FortiAnalyzerObject
        @property
        def raw(self) -> dict[str, Any]: ...
        @property
        def dict(self) -> dict[str, Any]: ...
        @property
        def json(self) -> str: ...
        def __getitem__(self, key: str) -> Any: ...

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
    def __iter__(self) -> Iterator[DvmdbDeviceItem]: ...
    def __len__(self) -> int: ...



class DvmdbDevice:
    """FortiAnalyzer endpoint: dvmdb.device"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def get(
        self,
        adom: str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["adm_pass", "adm_usr", "app_ver", "av_ver", "beta", "branch_pt", "build", "checksum", "cluster_worker", "conf_status", "conn_mode", "conn_status", "db_status", "desc", "dev_status", "eip", "fap_cnt", "faz.full_act", "faz.perm", "faz.quota", "faz.used", "fex_cnt", "first_tunnel_up", "flags", "foslic_cpu", "foslic_dr_site", "foslic_inst_time", "foslic_last_sync", "foslic_ram", "foslic_type", "foslic_utm", "fsw_cnt", "ha.vsn", "ha_group_id", "ha_group_name", "ha_mode", "ha_upgrade_mode", "hdisk_size", "hostname", "hw_generation", "hw_rev_major", "hw_rev_minor", "hyperscale", "ip", "ips_ext", "ips_ver", "last_checked", "last_resync", "latitude", "lic_flags", "lic_region", "location_from", "logdisk_size", "longitude", "maxvdom", "mgmt_if", "mgmt_mode", "mgmt_uuid", "mgt_vdom", "module_sn", "mr", "name", "nsxt_service_name", "os_type", "os_ver", "patch", "platform_str", "prefer_img_ver", "prio", "private_key", "private_key_status", "psk", "relver_info", "role", "sn", "sov_sase_license", "tunnel_sn", "version", "vm_cpu", "vm_cpu_limit", "vm_lic_expire", "vm_lic_overdue_since", "vm_mem", "vm_mem_limit", "vm_payg_status", "vm_status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        meta_fields: list[str] | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None,
    ) -> DvmdbDeviceGetResponse:
        """GET operation."""
        ...

    def set(
        self,
        adom: str | None = None,
        adm_pass: list[Any] | None = None,
        adm_usr: str | None = None,
        app_ver: str | None = None,
        av_ver: str | None = None,
        beta: int | None = None,
        branch_pt: int | None = None,
        build: int | None = None,
        checksum: str | None = None,
        cluster_worker: list[Any] | None = None,
        conf_status: Literal["unknown", "insync", "outofsync"] | None = None,
        conn_mode: Literal["active", "passive"] | None = None,
        conn_status: Literal["UNKNOWN", "up", "down"] | None = None,
        db_status: Literal["unknown", "nomod", "mod"] | None = None,
        desc: str | None = None,
        dev_status: Literal["none", "unknown", "checkedin", "inprogress", "installed", "aborted", "sched", "retry", "canceled", "pending", "retrieved", "changed_conf", "sync_fail", "timeout", "rev_revert", "auto_updated"] | None = None,
        eip: str | None = None,
        fap_cnt: int | None = None,
        faz_full_act: int | None = None,
        faz_perm: int | None = None,
        faz_quota: int | None = None,
        faz_used: int | None = None,
        fex_cnt: int | None = None,
        first_tunnel_up: int | None = None,
        flags: list[Any] | None = None,
        foslic_cpu: int | None = None,
        foslic_dr_site: Literal["disable", "enable"] | None = None,
        foslic_inst_time: int | None = None,
        foslic_last_sync: int | None = None,
        foslic_ram: int | None = None,
        foslic_type: Literal["temporary", "trial", "regular", "trial_expired"] | None = None,
        foslic_utm: list[Any] | None = None,
        fsw_cnt: int | None = None,
        ha_vsn: str | None = None,
        ha_group_id: int | None = None,
        ha_group_name: str | None = None,
        ha_mode: Literal["standalone", "AP", "AA", "ELBC", "DUAL", "fmg-enabled", "autoscale", "unknown"] | None = None,
        ha_upgrade_mode: int | None = None,
        hdisk_size: int | None = None,
        hostname: str | None = None,
        hw_generation: int | None = None,
        hw_rev_major: int | None = None,
        hw_rev_minor: int | None = None,
        hyperscale: int | None = None,
        ip: str | None = None,
        ips_ext: int | None = None,
        ips_ver: str | None = None,
        last_checked: int | None = None,
        last_resync: int | None = None,
        latitude: str | None = None,
        lic_flags: int | None = None,
        lic_region: str | None = None,
        location_from: str | None = None,
        logdisk_size: int | None = None,
        longitude: str | None = None,
        maxvdom: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mgmt_if: str | None = None,
        mgmt_mode: Literal["unreg", "fmg", "faz", "fmgfaz"] | None = None,
        mgmt_uuid: str | None = None,
        mgt_vdom: str | None = None,
        module_sn: str | None = None,
        mr: int | None = None,
        name: str | None = None,
        nsxt_service_name: str | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        patch: int | None = None,
        platform_str: str | None = None,
        prefer_img_ver: str | None = None,
        prio: int | None = None,
        private_key: str | None = None,
        private_key_status: int | None = None,
        psk: str | None = None,
        relver_info: str | None = None,
        role: Literal["master", "ha-slave", "autoscale-slave"] | None = None,
        sn: str | None = None,
        sov_sase_license: str | None = None,
        tunnel_sn: str | None = None,
        vdom: list[VdomItem] | None = None,
        version: int | None = None,
        vm_cpu: int | None = None,
        vm_cpu_limit: int | None = None,
        vm_lic_expire: int | None = None,
        vm_lic_overdue_since: int | None = None,
        vm_mem: int | None = None,
        vm_mem_limit: int | None = None,
        vm_payg_status: int | None = None,
        vm_status: Literal["N/A", "No License", "Startup", "Valid", "Pending", "Warning", "Invalid", "Invalid Copy", "Evaluation Expired", "Evaluation", "Expires Soon", "Expired", "Grace Period", "Validation Overdue"] | None = None,
    ) -> DvmdbDeviceSetResponse:
        """SET operation."""
        ...

    def update(
        self,
        adom: str | None = None,
        adm_pass: list[Any] | None = None,
        adm_usr: str | None = None,
        app_ver: str | None = None,
        av_ver: str | None = None,
        beta: int | None = None,
        branch_pt: int | None = None,
        build: int | None = None,
        checksum: str | None = None,
        cluster_worker: list[Any] | None = None,
        conf_status: Literal["unknown", "insync", "outofsync"] | None = None,
        conn_mode: Literal["active", "passive"] | None = None,
        conn_status: Literal["UNKNOWN", "up", "down"] | None = None,
        db_status: Literal["unknown", "nomod", "mod"] | None = None,
        desc: str | None = None,
        dev_status: Literal["none", "unknown", "checkedin", "inprogress", "installed", "aborted", "sched", "retry", "canceled", "pending", "retrieved", "changed_conf", "sync_fail", "timeout", "rev_revert", "auto_updated"] | None = None,
        eip: str | None = None,
        fap_cnt: int | None = None,
        faz_full_act: int | None = None,
        faz_perm: int | None = None,
        faz_quota: int | None = None,
        faz_used: int | None = None,
        fex_cnt: int | None = None,
        first_tunnel_up: int | None = None,
        flags: list[Any] | None = None,
        foslic_cpu: int | None = None,
        foslic_dr_site: Literal["disable", "enable"] | None = None,
        foslic_inst_time: int | None = None,
        foslic_last_sync: int | None = None,
        foslic_ram: int | None = None,
        foslic_type: Literal["temporary", "trial", "regular", "trial_expired"] | None = None,
        foslic_utm: list[Any] | None = None,
        fsw_cnt: int | None = None,
        ha_vsn: str | None = None,
        ha_group_id: int | None = None,
        ha_group_name: str | None = None,
        ha_mode: Literal["standalone", "AP", "AA", "ELBC", "DUAL", "fmg-enabled", "autoscale", "unknown"] | None = None,
        ha_upgrade_mode: int | None = None,
        hdisk_size: int | None = None,
        hostname: str | None = None,
        hw_generation: int | None = None,
        hw_rev_major: int | None = None,
        hw_rev_minor: int | None = None,
        hyperscale: int | None = None,
        ip: str | None = None,
        ips_ext: int | None = None,
        ips_ver: str | None = None,
        last_checked: int | None = None,
        last_resync: int | None = None,
        latitude: str | None = None,
        lic_flags: int | None = None,
        lic_region: str | None = None,
        location_from: str | None = None,
        logdisk_size: int | None = None,
        longitude: str | None = None,
        maxvdom: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mgmt_if: str | None = None,
        mgmt_mode: Literal["unreg", "fmg", "faz", "fmgfaz"] | None = None,
        mgmt_uuid: str | None = None,
        mgt_vdom: str | None = None,
        module_sn: str | None = None,
        mr: int | None = None,
        name: str | None = None,
        nsxt_service_name: str | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        patch: int | None = None,
        platform_str: str | None = None,
        prefer_img_ver: str | None = None,
        prio: int | None = None,
        private_key: str | None = None,
        private_key_status: int | None = None,
        psk: str | None = None,
        relver_info: str | None = None,
        role: Literal["master", "ha-slave", "autoscale-slave"] | None = None,
        sn: str | None = None,
        sov_sase_license: str | None = None,
        tunnel_sn: str | None = None,
        vdom: list[VdomItem] | None = None,
        version: int | None = None,
        vm_cpu: int | None = None,
        vm_cpu_limit: int | None = None,
        vm_lic_expire: int | None = None,
        vm_lic_overdue_since: int | None = None,
        vm_mem: int | None = None,
        vm_mem_limit: int | None = None,
        vm_payg_status: int | None = None,
        vm_status: Literal["N/A", "No License", "Startup", "Valid", "Pending", "Warning", "Invalid", "Invalid Copy", "Evaluation Expired", "Evaluation", "Expires Soon", "Expired", "Grace Period", "Validation Overdue"] | None = None,
    ) -> DvmdbDeviceSetResponse:
        """UPDATE operation."""
        ...


__all__ = ["DvmdbDevice", "DvmdbDeviceGetResponse", "DvmdbDeviceSetResponse"]