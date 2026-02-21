"""
FortiAnalyzer API endpoint: dvmdb.adom

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class DvmdbAdom:
    """
    FortiAnalyzer endpoint: dvmdb.adom
    
    
    Available methods: add, get, set, update, delete
    """

    def __init__(self, client: HTTPClientJSONRPC):
        """
        Initialize endpoint.
        
        Args:
            client: HTTPClientJSONRPC instance
        """
        self._client = client

    def add(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            create_time: create_time parameter
            desc: desc parameter
            flags: flags parameter
            lock_override: lock_override parameter
            log_db_retention_hours: log_db_retention_hours parameter
            log_disk_quota: log_disk_quota parameter
            log_disk_quota_alert_thres: log_disk_quota_alert_thres parameter
            log_disk_quota_split_ratio: log_disk_quota_split_ratio parameter
            log_file_retention_hours: log_file_retention_hours parameter
            meta_fields: Default metafields: none.
            ... (21 more parameters)
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        url = "/dvmdb/adom"
        
        # Build data payload
        data = {}
        if create_time is not None:
            data["create_time"] = create_time
        if desc is not None:
            data["desc"] = desc
        if flags is not None:
            data["flags"] = flags
        if lock_override is not None:
            data["lock_override"] = lock_override
        if log_db_retention_hours is not None:
            data["log_db_retention_hours"] = log_db_retention_hours
        if log_disk_quota is not None:
            data["log_disk_quota"] = log_disk_quota
        if log_disk_quota_alert_thres is not None:
            data["log_disk_quota_alert_thres"] = log_disk_quota_alert_thres
        if log_disk_quota_split_ratio is not None:
            data["log_disk_quota_split_ratio"] = log_disk_quota_split_ratio
        if log_file_retention_hours is not None:
            data["log_file_retention_hours"] = log_file_retention_hours
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if mig_mr is not None:
            data["mig_mr"] = mig_mr
        if mig_os_ver is not None:
            data["mig_os_ver"] = mig_os_ver
        if mode is not None:
            data["mode"] = mode
        if mr is not None:
            data["mr"] = mr
        if name is not None:
            data["name"] = name
        if os_ver is not None:
            data["os_ver"] = os_ver
        if primary_dns_ip4 is not None:
            data["primary_dns_ip4"] = primary_dns_ip4
        if primary_dns_ip6_1 is not None:
            data["primary_dns_ip6_1"] = primary_dns_ip6_1
        if primary_dns_ip6_2 is not None:
            data["primary_dns_ip6_2"] = primary_dns_ip6_2
        if primary_dns_ip6_3 is not None:
            data["primary_dns_ip6_3"] = primary_dns_ip6_3
        if primary_dns_ip6_4 is not None:
            data["primary_dns_ip6_4"] = primary_dns_ip6_4
        if restricted_prds is not None:
            data["restricted_prds"] = restricted_prds
        if secondary_dns_ip4 is not None:
            data["secondary_dns_ip4"] = secondary_dns_ip4
        if secondary_dns_ip6_1 is not None:
            data["secondary_dns_ip6_1"] = secondary_dns_ip6_1
        if secondary_dns_ip6_2 is not None:
            data["secondary_dns_ip6_2"] = secondary_dns_ip6_2
        if secondary_dns_ip6_3 is not None:
            data["secondary_dns_ip6_3"] = secondary_dns_ip6_3
        if secondary_dns_ip6_4 is not None:
            data["secondary_dns_ip6_4"] = secondary_dns_ip6_4
        if state is not None:
            data["state"] = state
        if tz is not None:
            data["tz"] = tz
        if uuid is not None:
            data["uuid"] = uuid
        if workspace_mode is not None:
            data["workspace_mode"] = workspace_mode
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

    def get(
        self,
        expand_member: str | None = None,
        fields: list[Literal["create_time", "desc", "flags", "lock_override", "log_db_retention_hours", "log_disk_quota", "log_disk_quota_alert_thres", "log_disk_quota_split_ratio", "log_file_retention_hours", "mig_mr", "mig_os_ver", "mode", "mr", "name", "os_ver", "primary_dns_ip4", "primary_dns_ip6_1", "primary_dns_ip6_2", "primary_dns_ip6_3", "primary_dns_ip6_4", "restricted_prds", "secondary_dns_ip4", "secondary_dns_ip6_1", "secondary_dns_ip6_2", "secondary_dns_ip6_3", "secondary_dns_ip6_4", "state", "tz", "uuid", "workspace_mode"]] | None = None,
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
            expand_member: Fetch all or selected attributes of object members.
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            meta_fields: Specify the meta field attributes to be returned in the result. If none specified, no meta field attribute will be returned.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>object member</b> - Return a list of object members along with other attributes.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
            range: Limit the number of output. For a range of [a, n], the output will contain <i>n</i> elements, starting from the <i>a<sup>th</sup></i> matching result.
            sortings: Specify the sorting of the returned result.
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        url = "/dvmdb/adom"
        
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
        
        return FortiAnalyzerResponse(response)

    def set(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            create_time: create_time parameter
            desc: desc parameter
            flags: flags parameter
            lock_override: lock_override parameter
            log_db_retention_hours: log_db_retention_hours parameter
            log_disk_quota: log_disk_quota parameter
            log_disk_quota_alert_thres: log_disk_quota_alert_thres parameter
            log_disk_quota_split_ratio: log_disk_quota_split_ratio parameter
            log_file_retention_hours: log_file_retention_hours parameter
            meta_fields: Default metafields: none.
            ... (21 more parameters)
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        url = "/dvmdb/adom"
        
        # Build data payload
        data = {}
        if create_time is not None:
            data["create_time"] = create_time
        if desc is not None:
            data["desc"] = desc
        if flags is not None:
            data["flags"] = flags
        if lock_override is not None:
            data["lock_override"] = lock_override
        if log_db_retention_hours is not None:
            data["log_db_retention_hours"] = log_db_retention_hours
        if log_disk_quota is not None:
            data["log_disk_quota"] = log_disk_quota
        if log_disk_quota_alert_thres is not None:
            data["log_disk_quota_alert_thres"] = log_disk_quota_alert_thres
        if log_disk_quota_split_ratio is not None:
            data["log_disk_quota_split_ratio"] = log_disk_quota_split_ratio
        if log_file_retention_hours is not None:
            data["log_file_retention_hours"] = log_file_retention_hours
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if mig_mr is not None:
            data["mig_mr"] = mig_mr
        if mig_os_ver is not None:
            data["mig_os_ver"] = mig_os_ver
        if mode is not None:
            data["mode"] = mode
        if mr is not None:
            data["mr"] = mr
        if name is not None:
            data["name"] = name
        if os_ver is not None:
            data["os_ver"] = os_ver
        if primary_dns_ip4 is not None:
            data["primary_dns_ip4"] = primary_dns_ip4
        if primary_dns_ip6_1 is not None:
            data["primary_dns_ip6_1"] = primary_dns_ip6_1
        if primary_dns_ip6_2 is not None:
            data["primary_dns_ip6_2"] = primary_dns_ip6_2
        if primary_dns_ip6_3 is not None:
            data["primary_dns_ip6_3"] = primary_dns_ip6_3
        if primary_dns_ip6_4 is not None:
            data["primary_dns_ip6_4"] = primary_dns_ip6_4
        if restricted_prds is not None:
            data["restricted_prds"] = restricted_prds
        if secondary_dns_ip4 is not None:
            data["secondary_dns_ip4"] = secondary_dns_ip4
        if secondary_dns_ip6_1 is not None:
            data["secondary_dns_ip6_1"] = secondary_dns_ip6_1
        if secondary_dns_ip6_2 is not None:
            data["secondary_dns_ip6_2"] = secondary_dns_ip6_2
        if secondary_dns_ip6_3 is not None:
            data["secondary_dns_ip6_3"] = secondary_dns_ip6_3
        if secondary_dns_ip6_4 is not None:
            data["secondary_dns_ip6_4"] = secondary_dns_ip6_4
        if state is not None:
            data["state"] = state
        if tz is not None:
            data["tz"] = tz
        if uuid is not None:
            data["uuid"] = uuid
        if workspace_mode is not None:
            data["workspace_mode"] = workspace_mode
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="set",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

    def update(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            create_time: create_time parameter
            desc: desc parameter
            flags: flags parameter
            lock_override: lock_override parameter
            log_db_retention_hours: log_db_retention_hours parameter
            log_disk_quota: log_disk_quota parameter
            log_disk_quota_alert_thres: log_disk_quota_alert_thres parameter
            log_disk_quota_split_ratio: log_disk_quota_split_ratio parameter
            log_file_retention_hours: log_file_retention_hours parameter
            meta_fields: Default metafields: none.
            ... (21 more parameters)
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        url = "/dvmdb/adom"
        
        # Build data payload
        data = {}
        if create_time is not None:
            data["create_time"] = create_time
        if desc is not None:
            data["desc"] = desc
        if flags is not None:
            data["flags"] = flags
        if lock_override is not None:
            data["lock_override"] = lock_override
        if log_db_retention_hours is not None:
            data["log_db_retention_hours"] = log_db_retention_hours
        if log_disk_quota is not None:
            data["log_disk_quota"] = log_disk_quota
        if log_disk_quota_alert_thres is not None:
            data["log_disk_quota_alert_thres"] = log_disk_quota_alert_thres
        if log_disk_quota_split_ratio is not None:
            data["log_disk_quota_split_ratio"] = log_disk_quota_split_ratio
        if log_file_retention_hours is not None:
            data["log_file_retention_hours"] = log_file_retention_hours
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if mig_mr is not None:
            data["mig_mr"] = mig_mr
        if mig_os_ver is not None:
            data["mig_os_ver"] = mig_os_ver
        if mode is not None:
            data["mode"] = mode
        if mr is not None:
            data["mr"] = mr
        if name is not None:
            data["name"] = name
        if os_ver is not None:
            data["os_ver"] = os_ver
        if primary_dns_ip4 is not None:
            data["primary_dns_ip4"] = primary_dns_ip4
        if primary_dns_ip6_1 is not None:
            data["primary_dns_ip6_1"] = primary_dns_ip6_1
        if primary_dns_ip6_2 is not None:
            data["primary_dns_ip6_2"] = primary_dns_ip6_2
        if primary_dns_ip6_3 is not None:
            data["primary_dns_ip6_3"] = primary_dns_ip6_3
        if primary_dns_ip6_4 is not None:
            data["primary_dns_ip6_4"] = primary_dns_ip6_4
        if restricted_prds is not None:
            data["restricted_prds"] = restricted_prds
        if secondary_dns_ip4 is not None:
            data["secondary_dns_ip4"] = secondary_dns_ip4
        if secondary_dns_ip6_1 is not None:
            data["secondary_dns_ip6_1"] = secondary_dns_ip6_1
        if secondary_dns_ip6_2 is not None:
            data["secondary_dns_ip6_2"] = secondary_dns_ip6_2
        if secondary_dns_ip6_3 is not None:
            data["secondary_dns_ip6_3"] = secondary_dns_ip6_3
        if secondary_dns_ip6_4 is not None:
            data["secondary_dns_ip6_4"] = secondary_dns_ip6_4
        if state is not None:
            data["state"] = state
        if tz is not None:
            data["tz"] = tz
        if uuid is not None:
            data["uuid"] = uuid
        if workspace_mode is not None:
            data["workspace_mode"] = workspace_mode
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="update",
            params=params
        )
        
        return FortiAnalyzerResponse(response)

    def delete(
        self,
        create_time: int | None = None,
        desc: str | None = None,
        flags: list[Any] | None = None,
        lock_override: int | None = None,
        log_db_retention_hours: int | None = None,
        log_disk_quota: int | None = None,
        log_disk_quota_alert_thres: int | None = None,
        log_disk_quota_split_ratio: int | None = None,
        log_file_retention_hours: int | None = None,
        meta_fields: dict[str, Any] | None = None,
        mig_mr: int | None = None,
        mig_os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        mode: Literal["ems", "gms", "provider"] | None = None,
        mr: int | None = None,
        name: str | None = None,
        os_ver: Literal["unknown", "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0"] | None = None,
        primary_dns_ip4: str | None = None,
        primary_dns_ip6_1: int | None = None,
        primary_dns_ip6_2: int | None = None,
        primary_dns_ip6_3: int | None = None,
        primary_dns_ip6_4: int | None = None,
        restricted_prds: Literal["sim", "fos", "foc", "fml", "fch", "fwb", "log", "fct", "faz", "fsa", "fsw", "fmg", "fdd", "fac", "fpx", "fna", "ffw", "fsr", "fad", "fdc", "fap", "fxt", "fts", "fai", "fwc", "fis", "fed", "fpa", "fca", "ftc", "fss", "fra", "fabric"] | None = None,
        secondary_dns_ip4: str | None = None,
        secondary_dns_ip6_1: int | None = None,
        secondary_dns_ip6_2: int | None = None,
        secondary_dns_ip6_3: int | None = None,
        secondary_dns_ip6_4: int | None = None,
        state: int | None = None,
        tz: int | None = None,
        uuid: str | None = None,
        workspace_mode: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            create_time: create_time parameter
            desc: desc parameter
            flags: flags parameter
            lock_override: lock_override parameter
            log_db_retention_hours: log_db_retention_hours parameter
            log_disk_quota: log_disk_quota parameter
            log_disk_quota_alert_thres: log_disk_quota_alert_thres parameter
            log_disk_quota_split_ratio: log_disk_quota_split_ratio parameter
            log_file_retention_hours: log_file_retention_hours parameter
            meta_fields: Default metafields: none.
            ... (21 more parameters)
        
        Returns:
            Response data from FortiManager API
        """
        # Build URL
        url = "/dvmdb/adom"
        
        # Build data payload
        data = {}
        if create_time is not None:
            data["create_time"] = create_time
        if desc is not None:
            data["desc"] = desc
        if flags is not None:
            data["flags"] = flags
        if lock_override is not None:
            data["lock_override"] = lock_override
        if log_db_retention_hours is not None:
            data["log_db_retention_hours"] = log_db_retention_hours
        if log_disk_quota is not None:
            data["log_disk_quota"] = log_disk_quota
        if log_disk_quota_alert_thres is not None:
            data["log_disk_quota_alert_thres"] = log_disk_quota_alert_thres
        if log_disk_quota_split_ratio is not None:
            data["log_disk_quota_split_ratio"] = log_disk_quota_split_ratio
        if log_file_retention_hours is not None:
            data["log_file_retention_hours"] = log_file_retention_hours
        if meta_fields is not None:
            data["meta fields"] = meta_fields
        if mig_mr is not None:
            data["mig_mr"] = mig_mr
        if mig_os_ver is not None:
            data["mig_os_ver"] = mig_os_ver
        if mode is not None:
            data["mode"] = mode
        if mr is not None:
            data["mr"] = mr
        if name is not None:
            data["name"] = name
        if os_ver is not None:
            data["os_ver"] = os_ver
        if primary_dns_ip4 is not None:
            data["primary_dns_ip4"] = primary_dns_ip4
        if primary_dns_ip6_1 is not None:
            data["primary_dns_ip6_1"] = primary_dns_ip6_1
        if primary_dns_ip6_2 is not None:
            data["primary_dns_ip6_2"] = primary_dns_ip6_2
        if primary_dns_ip6_3 is not None:
            data["primary_dns_ip6_3"] = primary_dns_ip6_3
        if primary_dns_ip6_4 is not None:
            data["primary_dns_ip6_4"] = primary_dns_ip6_4
        if restricted_prds is not None:
            data["restricted_prds"] = restricted_prds
        if secondary_dns_ip4 is not None:
            data["secondary_dns_ip4"] = secondary_dns_ip4
        if secondary_dns_ip6_1 is not None:
            data["secondary_dns_ip6_1"] = secondary_dns_ip6_1
        if secondary_dns_ip6_2 is not None:
            data["secondary_dns_ip6_2"] = secondary_dns_ip6_2
        if secondary_dns_ip6_3 is not None:
            data["secondary_dns_ip6_3"] = secondary_dns_ip6_3
        if secondary_dns_ip6_4 is not None:
            data["secondary_dns_ip6_4"] = secondary_dns_ip6_4
        if state is not None:
            data["state"] = state
        if tz is not None:
            data["tz"] = tz
        if uuid is not None:
            data["uuid"] = uuid
        if workspace_mode is not None:
            data["workspace_mode"] = workspace_mode
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        return FortiAnalyzerResponse(response)
