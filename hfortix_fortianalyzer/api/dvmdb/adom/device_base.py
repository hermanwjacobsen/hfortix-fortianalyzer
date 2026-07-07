"""
FortiAnalyzer API endpoint: dvmdb.adom.device

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdomDevice:
    """
    FortiAnalyzer endpoint: dvmdb.adom.device
    
    
    Available methods: get, set, update
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def get(
        self,
        adom: str,
        device: int | str | None = None,
        expand_member: str | None = None,
        fields: list[Literal["adm_pass", "adm_usr", "app_ver", "av_ver", "beta", "branch_pt", "build", "checksum", "cluster_worker", "conf_status", "conn_mode", "conn_status", "db_status", "desc", "dev_status", "eip", "fap_cnt", "faz.full_act", "faz.perm", "faz.quota", "faz.used", "fex_cnt", "first_tunnel_up", "flags", "foslic_cpu", "foslic_dr_site", "foslic_inst_time", "foslic_last_sync", "foslic_ram", "foslic_type", "foslic_utm", "fsw_cnt", "ha.vsn", "ha_group_id", "ha_group_name", "ha_mode", "ha_upgrade_mode", "hdisk_size", "hostname", "hw_generation", "hw_rev_major", "hw_rev_minor", "hyperscale", "ip", "ips_ext", "ips_ver", "last_checked", "last_resync", "latitude", "lic_flags", "lic_region", "location_from", "logdisk_size", "longitude", "maxvdom", "mgmt_if", "mgmt_mode", "mgmt_uuid", "mgt_vdom", "module_sn", "mr", "name", "nsxt_service_name", "os_type", "os_ver", "patch", "platform_str", "prefer_img_ver", "prio", "private_key", "private_key_status", "psk", "relver_info", "role", "sn", "sov_sase_license", "tunnel_sn", "version", "vm_cpu", "vm_cpu_limit", "vm_lic_expire", "vm_lic_overdue_since", "vm_mem", "vm_mem_limit", "vm_payg_status", "vm_status"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        meta_fields: list[str] | None = None,
        option: Literal["count", "object member", "syntax"] | None = None,
        range: list[int] | None = None,
        sortings: list[dict[str, Any]] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            adom: ADOM name.
            device: Unique name for the device.
            expand_member: Fetch all or selected attributes of object members.
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            meta_fields: Specify the meta field attributes to be returned in the result. If none specified, no meta field attribute will be returned.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>object member</b> - Return a list of object members along with other attributes.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
            range: Limit the number of output. For a range of [a, n], the output will contain <i>n</i> elements, starting from the <i>a<sup>th</sup></i> matching result.
            sortings: Specify the sorting of the returned result.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and device is not None:
            url = "/dvmdb/adom/{adom}/device/{device}"
            url = url.replace("{adom}", adom)
            url = url.replace("{device}", str(device))
        else:
            url = "/dvmdb/adom/{adom}/device"
            url = url.replace("{adom}", adom)
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if expand_member is not None:
            request_params["expand member"] = expand_member
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if meta_fields is not None:
            request_params["meta fields"] = meta_fields
        if option is not None:
            request_params["option"] = option
        if range is not None:
            request_params["range"] = range
        if sortings is not None:
            request_params["sortings"] = sortings
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            **request_params
        }]
        
        response = self._client.execute(
            method="get",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        adom: str,
        device: int | str | None = None,
        conf_status: Literal["unknown", "insync", "outofsync"] | None = None,
        conn_mode: Literal["active", "passive"] | None = None,
        conn_status: Literal["UNKNOWN", "up", "down"] | None = None,
        db_status: Literal["unknown", "nomod", "mod"] | None = None,
        dev_status: Literal["none", "unknown", "checkedin", "inprogress", "installed", "aborted", "sched", "retry", "canceled", "pending", "retrieved", "changed_conf", "sync_fail", "timeout", "rev_revert", "auto_updated"] | None = None,
        foslic_dr_site: Literal["disable", "enable"] | None = None,
        foslic_type: Literal["temporary", "trial", "regular", "trial_expired"] | None = None,
        ha_mode: Literal["standalone", "AP", "AA", "ELBC", "DUAL", "fmg-enabled", "autoscale", "unknown"] | None = None,
        maxvdom: int | None = None,
        mgmt_mode: Literal["unreg", "fmg", "faz", "fmgfaz"] | None = None,
        mr: int | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        role: Literal["master", "ha-slave", "autoscale-slave"] | None = None,
        vm_status: Literal["N/A", "No License", "Startup", "Valid", "Pending", "Warning", "Invalid", "Invalid Copy", "Evaluation Expired", "Evaluation", "Expires Soon", "Expired", "Grace Period", "Validation Overdue"] | None = None,
        adm_pass: list[Any] | None = None,
        adm_usr: str | None = None,
        app_ver: str | None = None,
        av_ver: str | None = None,
        beta: int | None = None,
        branch_pt: int | None = None,
        build: int | None = None,
        checksum: str | None = None,
        cluster_worker: list[Any] | None = None,
        desc: str | None = None,
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
        foslic_inst_time: int | None = None,
        foslic_last_sync: int | None = None,
        foslic_ram: int | None = None,
        foslic_utm: list[Any] | None = None,
        fsw_cnt: int | None = None,
        ha_vsn: str | None = None,
        ha_group_id: int | None = None,
        ha_group_name: str | None = None,
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
        meta_fields: dict[str, Any] | None = None,
        mgmt_if: str | None = None,
        mgmt_uuid: str | None = None,
        mgt_vdom: str | None = None,
        module_sn: str | None = None,
        name: str | None = None,
        nsxt_service_name: str | None = None,
        patch: int | None = None,
        platform_str: str | None = None,
        prefer_img_ver: str | None = None,
        prio: int | None = None,
        private_key: str | None = None,
        private_key_status: int | None = None,
        psk: str | None = None,
        relver_info: str | None = None,
        sn: str | None = None,
        sov_sase_license: str | None = None,
        tunnel_sn: str | None = None,
        vdom: list[Any] | None = None,
        version: int | None = None,
        vm_cpu: int | None = None,
        vm_cpu_limit: int | None = None,
        vm_lic_expire: int | None = None,
        vm_lic_overdue_since: int | None = None,
        vm_mem: int | None = None,
        vm_mem_limit: int | None = None,
        vm_payg_status: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            adom: ADOM name.
            device: Unique name for the device.
            adm_pass: adm_pass parameter
            adm_usr: adm_usr parameter
            app_ver: app_ver parameter
            av_ver: av_ver parameter
            beta: beta parameter
            branch_pt: branch_pt parameter
            build: build parameter
            checksum: checksum parameter
            cluster_worker: cluster_worker parameter
            conf_status: conf_status parameter
            ... (78 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and device is not None:
            url = "/dvmdb/adom/{adom}/device/{device}"
            url = url.replace("{adom}", adom)
            url = url.replace("{device}", str(device))
        else:
            url = "/dvmdb/adom/{adom}/device"
            url = url.replace("{adom}", adom)
        
        # Build data payload
        data = {}
        if adm_pass is not None:
            data["adm_pass"] = adm_pass
        if adm_usr is not None:
            data["adm_usr"] = adm_usr
        if app_ver is not None:
            data["app_ver"] = app_ver
        if av_ver is not None:
            data["av_ver"] = av_ver
        if beta is not None:
            data["beta"] = beta
        if branch_pt is not None:
            data["branch_pt"] = branch_pt
        if build is not None:
            data["build"] = build
        if checksum is not None:
            data["checksum"] = checksum
        if cluster_worker is not None:
            data["cluster_worker"] = cluster_worker
        if conf_status is not None:
            data["conf_status"] = conf_status
        if conn_mode is not None:
            data["conn_mode"] = conn_mode
        if conn_status is not None:
            data["conn_status"] = conn_status
        if db_status is not None:
            data["db_status"] = db_status
        if desc is not None:
            data["desc"] = desc
        if dev_status is not None:
            data["dev_status"] = dev_status
        if eip is not None:
            data["eip"] = eip
        if fap_cnt is not None:
            data["fap_cnt"] = fap_cnt
        if faz_full_act is not None:
            data["faz.full_act"] = faz_full_act
        if faz_perm is not None:
            data["faz.perm"] = faz_perm
        if faz_quota is not None:
            data["faz.quota"] = faz_quota
        if faz_used is not None:
            data["faz.used"] = faz_used
        if fex_cnt is not None:
            data["fex_cnt"] = fex_cnt
        if first_tunnel_up is not None:
            data["first_tunnel_up"] = first_tunnel_up
        if flags is not None:
            data["flags"] = flags
        if foslic_cpu is not None:
            data["foslic_cpu"] = foslic_cpu
        if foslic_dr_site is not None:
            data["foslic_dr_site"] = foslic_dr_site
        if foslic_inst_time is not None:
            data["foslic_inst_time"] = foslic_inst_time
        if foslic_last_sync is not None:
            data["foslic_last_sync"] = foslic_last_sync
        if foslic_ram is not None:
            data["foslic_ram"] = foslic_ram
        if foslic_type is not None:
            data["foslic_type"] = foslic_type
        if foslic_utm is not None:
            data["foslic_utm"] = foslic_utm
        if fsw_cnt is not None:
            data["fsw_cnt"] = fsw_cnt
        if ha_vsn is not None:
            data["ha.vsn"] = ha_vsn
        if ha_group_id is not None:
            data["ha_group_id"] = ha_group_id
        if ha_group_name is not None:
            data["ha_group_name"] = ha_group_name
        if ha_mode is not None:
            data["ha_mode"] = ha_mode
        if ha_upgrade_mode is not None:
            data["ha_upgrade_mode"] = ha_upgrade_mode
        if hdisk_size is not None:
            data["hdisk_size"] = hdisk_size
        if hostname is not None:
            data["hostname"] = hostname
        if hw_generation is not None:
            data["hw_generation"] = hw_generation
        if hw_rev_major is not None:
            data["hw_rev_major"] = hw_rev_major
        if hw_rev_minor is not None:
            data["hw_rev_minor"] = hw_rev_minor
        if hyperscale is not None:
            data["hyperscale"] = hyperscale
        if ip is not None:
            data["ip"] = ip
        if ips_ext is not None:
            data["ips_ext"] = ips_ext
        if ips_ver is not None:
            data["ips_ver"] = ips_ver
        if last_checked is not None:
            data["last_checked"] = last_checked
        if last_resync is not None:
            data["last_resync"] = last_resync
        if latitude is not None:
            data["latitude"] = latitude
        if lic_flags is not None:
            data["lic_flags"] = lic_flags
        if lic_region is not None:
            data["lic_region"] = lic_region
        if location_from is not None:
            data["location_from"] = location_from
        if logdisk_size is not None:
            data["logdisk_size"] = logdisk_size
        if longitude is not None:
            data["longitude"] = longitude
        if maxvdom is not None:
            data["maxvdom"] = maxvdom
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if mgmt_if is not None:
            data["mgmt_if"] = mgmt_if
        if mgmt_mode is not None:
            data["mgmt_mode"] = mgmt_mode
        if mgmt_uuid is not None:
            data["mgmt_uuid"] = mgmt_uuid
        if mgt_vdom is not None:
            data["mgt_vdom"] = mgt_vdom
        if module_sn is not None:
            data["module_sn"] = module_sn
        if mr is not None:
            data["mr"] = mr
        if name is not None:
            data["name"] = name
        if nsxt_service_name is not None:
            data["nsxt_service_name"] = nsxt_service_name
        if os_type is not None:
            data["os_type"] = os_type
        if os_ver is not None:
            data["os_ver"] = os_ver
        if patch is not None:
            data["patch"] = patch
        if platform_str is not None:
            data["platform_str"] = platform_str
        if prefer_img_ver is not None:
            data["prefer_img_ver"] = prefer_img_ver
        if prio is not None:
            data["prio"] = prio
        if private_key is not None:
            data["private_key"] = private_key
        if private_key_status is not None:
            data["private_key_status"] = private_key_status
        if psk is not None:
            data["psk"] = psk
        if relver_info is not None:
            data["relver_info"] = relver_info
        if role is not None:
            data["role"] = role
        if sn is not None:
            data["sn"] = sn
        if sov_sase_license is not None:
            data["sov_sase_license"] = sov_sase_license
        if tunnel_sn is not None:
            data["tunnel_sn"] = tunnel_sn
        if vdom is not None:
            data["vdom"] = vdom
        if version is not None:
            data["version"] = version
        if vm_cpu is not None:
            data["vm_cpu"] = vm_cpu
        if vm_cpu_limit is not None:
            data["vm_cpu_limit"] = vm_cpu_limit
        if vm_lic_expire is not None:
            data["vm_lic_expire"] = vm_lic_expire
        if vm_lic_overdue_since is not None:
            data["vm_lic_overdue_since"] = vm_lic_overdue_since
        if vm_mem is not None:
            data["vm_mem"] = vm_mem
        if vm_mem_limit is not None:
            data["vm_mem_limit"] = vm_mem_limit
        if vm_payg_status is not None:
            data["vm_payg_status"] = vm_payg_status
        if vm_status is not None:
            data["vm_status"] = vm_status
        
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
        adom: str,
        device: int | str | None = None,
        conf_status: Literal["unknown", "insync", "outofsync"] | None = None,
        conn_mode: Literal["active", "passive"] | None = None,
        conn_status: Literal["UNKNOWN", "up", "down"] | None = None,
        db_status: Literal["unknown", "nomod", "mod"] | None = None,
        dev_status: Literal["none", "unknown", "checkedin", "inprogress", "installed", "aborted", "sched", "retry", "canceled", "pending", "retrieved", "changed_conf", "sync_fail", "timeout", "rev_revert", "auto_updated"] | None = None,
        foslic_dr_site: Literal["disable", "enable"] | None = None,
        foslic_type: Literal["temporary", "trial", "regular", "trial_expired"] | None = None,
        ha_mode: Literal["standalone", "AP", "AA", "ELBC", "DUAL", "fmg-enabled", "autoscale", "unknown"] | None = None,
        maxvdom: int | None = None,
        mgmt_mode: Literal["unreg", "fmg", "faz", "fmgfaz"] | None = None,
        mr: int | None = None,
        os_type: Literal["unknown", "fos", "fsw", "foc", "fml", "faz", "fwb", "fch", "fct", "log", "fmg", "fsa", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "sim"] | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        role: Literal["master", "ha-slave", "autoscale-slave"] | None = None,
        vm_status: Literal["N/A", "No License", "Startup", "Valid", "Pending", "Warning", "Invalid", "Invalid Copy", "Evaluation Expired", "Evaluation", "Expires Soon", "Expired", "Grace Period", "Validation Overdue"] | None = None,
        adm_pass: list[Any] | None = None,
        adm_usr: str | None = None,
        app_ver: str | None = None,
        av_ver: str | None = None,
        beta: int | None = None,
        branch_pt: int | None = None,
        build: int | None = None,
        checksum: str | None = None,
        cluster_worker: list[Any] | None = None,
        desc: str | None = None,
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
        foslic_inst_time: int | None = None,
        foslic_last_sync: int | None = None,
        foslic_ram: int | None = None,
        foslic_utm: list[Any] | None = None,
        fsw_cnt: int | None = None,
        ha_vsn: str | None = None,
        ha_group_id: int | None = None,
        ha_group_name: str | None = None,
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
        meta_fields: dict[str, Any] | None = None,
        mgmt_if: str | None = None,
        mgmt_uuid: str | None = None,
        mgt_vdom: str | None = None,
        module_sn: str | None = None,
        name: str | None = None,
        nsxt_service_name: str | None = None,
        patch: int | None = None,
        platform_str: str | None = None,
        prefer_img_ver: str | None = None,
        prio: int | None = None,
        private_key: str | None = None,
        private_key_status: int | None = None,
        psk: str | None = None,
        relver_info: str | None = None,
        sn: str | None = None,
        sov_sase_license: str | None = None,
        tunnel_sn: str | None = None,
        vdom: list[Any] | None = None,
        version: int | None = None,
        vm_cpu: int | None = None,
        vm_cpu_limit: int | None = None,
        vm_lic_expire: int | None = None,
        vm_lic_overdue_since: int | None = None,
        vm_mem: int | None = None,
        vm_mem_limit: int | None = None,
        vm_payg_status: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            adom: ADOM name.
            device: Unique name for the device.
            adm_pass: adm_pass parameter
            adm_usr: adm_usr parameter
            app_ver: app_ver parameter
            av_ver: av_ver parameter
            beta: beta parameter
            branch_pt: branch_pt parameter
            build: build parameter
            checksum: checksum parameter
            cluster_worker: cluster_worker parameter
            conf_status: conf_status parameter
            ... (78 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if adom is not None and device is not None:
            url = "/dvmdb/adom/{adom}/device/{device}"
            url = url.replace("{adom}", adom)
            url = url.replace("{device}", str(device))
        else:
            url = "/dvmdb/adom/{adom}/device"
            url = url.replace("{adom}", adom)
        
        # Build data payload
        data = {}
        if adm_pass is not None:
            data["adm_pass"] = adm_pass
        if adm_usr is not None:
            data["adm_usr"] = adm_usr
        if app_ver is not None:
            data["app_ver"] = app_ver
        if av_ver is not None:
            data["av_ver"] = av_ver
        if beta is not None:
            data["beta"] = beta
        if branch_pt is not None:
            data["branch_pt"] = branch_pt
        if build is not None:
            data["build"] = build
        if checksum is not None:
            data["checksum"] = checksum
        if cluster_worker is not None:
            data["cluster_worker"] = cluster_worker
        if conf_status is not None:
            data["conf_status"] = conf_status
        if conn_mode is not None:
            data["conn_mode"] = conn_mode
        if conn_status is not None:
            data["conn_status"] = conn_status
        if db_status is not None:
            data["db_status"] = db_status
        if desc is not None:
            data["desc"] = desc
        if dev_status is not None:
            data["dev_status"] = dev_status
        if eip is not None:
            data["eip"] = eip
        if fap_cnt is not None:
            data["fap_cnt"] = fap_cnt
        if faz_full_act is not None:
            data["faz.full_act"] = faz_full_act
        if faz_perm is not None:
            data["faz.perm"] = faz_perm
        if faz_quota is not None:
            data["faz.quota"] = faz_quota
        if faz_used is not None:
            data["faz.used"] = faz_used
        if fex_cnt is not None:
            data["fex_cnt"] = fex_cnt
        if first_tunnel_up is not None:
            data["first_tunnel_up"] = first_tunnel_up
        if flags is not None:
            data["flags"] = flags
        if foslic_cpu is not None:
            data["foslic_cpu"] = foslic_cpu
        if foslic_dr_site is not None:
            data["foslic_dr_site"] = foslic_dr_site
        if foslic_inst_time is not None:
            data["foslic_inst_time"] = foslic_inst_time
        if foslic_last_sync is not None:
            data["foslic_last_sync"] = foslic_last_sync
        if foslic_ram is not None:
            data["foslic_ram"] = foslic_ram
        if foslic_type is not None:
            data["foslic_type"] = foslic_type
        if foslic_utm is not None:
            data["foslic_utm"] = foslic_utm
        if fsw_cnt is not None:
            data["fsw_cnt"] = fsw_cnt
        if ha_vsn is not None:
            data["ha.vsn"] = ha_vsn
        if ha_group_id is not None:
            data["ha_group_id"] = ha_group_id
        if ha_group_name is not None:
            data["ha_group_name"] = ha_group_name
        if ha_mode is not None:
            data["ha_mode"] = ha_mode
        if ha_upgrade_mode is not None:
            data["ha_upgrade_mode"] = ha_upgrade_mode
        if hdisk_size is not None:
            data["hdisk_size"] = hdisk_size
        if hostname is not None:
            data["hostname"] = hostname
        if hw_generation is not None:
            data["hw_generation"] = hw_generation
        if hw_rev_major is not None:
            data["hw_rev_major"] = hw_rev_major
        if hw_rev_minor is not None:
            data["hw_rev_minor"] = hw_rev_minor
        if hyperscale is not None:
            data["hyperscale"] = hyperscale
        if ip is not None:
            data["ip"] = ip
        if ips_ext is not None:
            data["ips_ext"] = ips_ext
        if ips_ver is not None:
            data["ips_ver"] = ips_ver
        if last_checked is not None:
            data["last_checked"] = last_checked
        if last_resync is not None:
            data["last_resync"] = last_resync
        if latitude is not None:
            data["latitude"] = latitude
        if lic_flags is not None:
            data["lic_flags"] = lic_flags
        if lic_region is not None:
            data["lic_region"] = lic_region
        if location_from is not None:
            data["location_from"] = location_from
        if logdisk_size is not None:
            data["logdisk_size"] = logdisk_size
        if longitude is not None:
            data["longitude"] = longitude
        if maxvdom is not None:
            data["maxvdom"] = maxvdom
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if mgmt_if is not None:
            data["mgmt_if"] = mgmt_if
        if mgmt_mode is not None:
            data["mgmt_mode"] = mgmt_mode
        if mgmt_uuid is not None:
            data["mgmt_uuid"] = mgmt_uuid
        if mgt_vdom is not None:
            data["mgt_vdom"] = mgt_vdom
        if module_sn is not None:
            data["module_sn"] = module_sn
        if mr is not None:
            data["mr"] = mr
        if name is not None:
            data["name"] = name
        if nsxt_service_name is not None:
            data["nsxt_service_name"] = nsxt_service_name
        if os_type is not None:
            data["os_type"] = os_type
        if os_ver is not None:
            data["os_ver"] = os_ver
        if patch is not None:
            data["patch"] = patch
        if platform_str is not None:
            data["platform_str"] = platform_str
        if prefer_img_ver is not None:
            data["prefer_img_ver"] = prefer_img_ver
        if prio is not None:
            data["prio"] = prio
        if private_key is not None:
            data["private_key"] = private_key
        if private_key_status is not None:
            data["private_key_status"] = private_key_status
        if psk is not None:
            data["psk"] = psk
        if relver_info is not None:
            data["relver_info"] = relver_info
        if role is not None:
            data["role"] = role
        if sn is not None:
            data["sn"] = sn
        if sov_sase_license is not None:
            data["sov_sase_license"] = sov_sase_license
        if tunnel_sn is not None:
            data["tunnel_sn"] = tunnel_sn
        if vdom is not None:
            data["vdom"] = vdom
        if version is not None:
            data["version"] = version
        if vm_cpu is not None:
            data["vm_cpu"] = vm_cpu
        if vm_cpu_limit is not None:
            data["vm_cpu_limit"] = vm_cpu_limit
        if vm_lic_expire is not None:
            data["vm_lic_expire"] = vm_lic_expire
        if vm_lic_overdue_since is not None:
            data["vm_lic_overdue_since"] = vm_lic_overdue_since
        if vm_mem is not None:
            data["vm_mem"] = vm_mem
        if vm_mem_limit is not None:
            data["vm_mem_limit"] = vm_mem_limit
        if vm_payg_status is not None:
            data["vm_payg_status"] = vm_payg_status
        if vm_status is not None:
            data["vm_status"] = vm_status
        
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
