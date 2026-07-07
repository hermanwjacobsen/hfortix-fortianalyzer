"""
FortiAnalyzer API endpoint: cli.global.system.ha

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemHa:
    """
    FortiAnalyzer endpoint: cli.global.system.ha
    
    
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
        url = "/cli/global/system/ha"
        
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
        cfg_sync_hb_interval: int | None = None,
        group_id: int | None = None,
        hb_interval: int | None = None,
        initial_sync: Literal["disable", "enable"] | None = None,
        initial_sync_threads: int | None = None,
        load_balance: Literal["disable", "round-robin"] | None = None,
        log_sync: Literal["disable", "enable"] | None = None,
        mode: Literal["standalone", "a-p", "a-a"] | None = None,
        preferred_role: Literal["secondary", "primary"] | None = None,
        priority: int | None = None,
        private_clusterid: int | None = None,
        private_file_quota: int | None = None,
        private_hb_interval: int | None = None,
        private_hb_lost_threshold: int | None = None,
        private_mode: Literal["standalone", "primary", "secondary"] | None = None,
        unicast: Literal["disable", "enable"] | None = None,
        group_name: str | None = None,
        hb_interface: str | None = None,
        healthcheck: list[Any] | None = None,
        local_cert: str | None = None,
        password: list[Any] | None = None,
        peer: list[Any] | None = None,
        private_password: list[Any] | None = None,
        private_peer: list[Any] | None = None,
        vip: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            cfg_sync_hb_interval: cfg-sync-hb-interval parameter
            group_id: group-id parameter
            group_name: group-name parameter
            hb_interface: hb-interface parameter
            hb_interval: hb-interval parameter
            healthcheck: healthcheck parameter
            initial_sync: initial-sync parameter
            initial_sync_threads: initial-sync-threads parameter
            load_balance: load-balance parameter
            local_cert: local-cert parameter
            ... (15 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/ha"
        
        # Build data payload
        data = {}
        if cfg_sync_hb_interval is not None:
            data["cfg-sync-hb-interval"] = cfg_sync_hb_interval
        if group_id is not None:
            data["group-id"] = group_id
        if group_name is not None:
            data["group-name"] = group_name
        if hb_interface is not None:
            data["hb-interface"] = hb_interface
        if hb_interval is not None:
            data["hb-interval"] = hb_interval
        if healthcheck is not None:
            data["healthcheck"] = healthcheck
        if initial_sync is not None:
            data["initial-sync"] = initial_sync
        if initial_sync_threads is not None:
            data["initial-sync-threads"] = initial_sync_threads
        if load_balance is not None:
            data["load-balance"] = load_balance
        if local_cert is not None:
            data["local-cert"] = local_cert
        if log_sync is not None:
            data["log-sync"] = log_sync
        if mode is not None:
            data["mode"] = mode
        if password is not None:
            data["password"] = password
        if peer is not None:
            data["peer"] = peer
        if preferred_role is not None:
            data["preferred-role"] = preferred_role
        if priority is not None:
            data["priority"] = priority
        if private_clusterid is not None:
            data["private-clusterid"] = private_clusterid
        if private_file_quota is not None:
            data["private-file-quota"] = private_file_quota
        if private_hb_interval is not None:
            data["private-hb-interval"] = private_hb_interval
        if private_hb_lost_threshold is not None:
            data["private-hb-lost-threshold"] = private_hb_lost_threshold
        if private_mode is not None:
            data["private-mode"] = private_mode
        if private_password is not None:
            data["private-password"] = private_password
        if private_peer is not None:
            data["private-peer"] = private_peer
        if unicast is not None:
            data["unicast"] = unicast
        if vip is not None:
            data["vip"] = vip
        
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
        cfg_sync_hb_interval: int | None = None,
        group_id: int | None = None,
        hb_interval: int | None = None,
        initial_sync: Literal["disable", "enable"] | None = None,
        initial_sync_threads: int | None = None,
        load_balance: Literal["disable", "round-robin"] | None = None,
        log_sync: Literal["disable", "enable"] | None = None,
        mode: Literal["standalone", "a-p", "a-a"] | None = None,
        preferred_role: Literal["secondary", "primary"] | None = None,
        priority: int | None = None,
        private_clusterid: int | None = None,
        private_file_quota: int | None = None,
        private_hb_interval: int | None = None,
        private_hb_lost_threshold: int | None = None,
        private_mode: Literal["standalone", "primary", "secondary"] | None = None,
        unicast: Literal["disable", "enable"] | None = None,
        group_name: str | None = None,
        hb_interface: str | None = None,
        healthcheck: list[Any] | None = None,
        local_cert: str | None = None,
        password: list[Any] | None = None,
        peer: list[Any] | None = None,
        private_password: list[Any] | None = None,
        private_peer: list[Any] | None = None,
        vip: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            cfg_sync_hb_interval: cfg-sync-hb-interval parameter
            group_id: group-id parameter
            group_name: group-name parameter
            hb_interface: hb-interface parameter
            hb_interval: hb-interval parameter
            healthcheck: healthcheck parameter
            initial_sync: initial-sync parameter
            initial_sync_threads: initial-sync-threads parameter
            load_balance: load-balance parameter
            local_cert: local-cert parameter
            ... (15 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/ha"
        
        # Build data payload
        data = {}
        if cfg_sync_hb_interval is not None:
            data["cfg-sync-hb-interval"] = cfg_sync_hb_interval
        if group_id is not None:
            data["group-id"] = group_id
        if group_name is not None:
            data["group-name"] = group_name
        if hb_interface is not None:
            data["hb-interface"] = hb_interface
        if hb_interval is not None:
            data["hb-interval"] = hb_interval
        if healthcheck is not None:
            data["healthcheck"] = healthcheck
        if initial_sync is not None:
            data["initial-sync"] = initial_sync
        if initial_sync_threads is not None:
            data["initial-sync-threads"] = initial_sync_threads
        if load_balance is not None:
            data["load-balance"] = load_balance
        if local_cert is not None:
            data["local-cert"] = local_cert
        if log_sync is not None:
            data["log-sync"] = log_sync
        if mode is not None:
            data["mode"] = mode
        if password is not None:
            data["password"] = password
        if peer is not None:
            data["peer"] = peer
        if preferred_role is not None:
            data["preferred-role"] = preferred_role
        if priority is not None:
            data["priority"] = priority
        if private_clusterid is not None:
            data["private-clusterid"] = private_clusterid
        if private_file_quota is not None:
            data["private-file-quota"] = private_file_quota
        if private_hb_interval is not None:
            data["private-hb-interval"] = private_hb_interval
        if private_hb_lost_threshold is not None:
            data["private-hb-lost-threshold"] = private_hb_lost_threshold
        if private_mode is not None:
            data["private-mode"] = private_mode
        if private_password is not None:
            data["private-password"] = private_password
        if private_peer is not None:
            data["private-peer"] = private_peer
        if unicast is not None:
            data["unicast"] = unicast
        if vip is not None:
            data["vip"] = vip
        
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
