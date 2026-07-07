"""
FortiAnalyzer API endpoint: cli.global.system.csf

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCsf:
    """
    FortiAnalyzer endpoint: cli.global.system.csf
    
    
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
        url = "/cli/global/system/csf"
        
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
        accept_auth_by_cert: Literal["disable", "enable"] | None = None,
        authorization_request_type: Literal["certificate", "serial"] | None = None,
        certificate: str | None = None,
        downstream_access: Literal["disable", "enable"] | None = None,
        fabric_workers: int | None = None,
        forticloud_account_enforcement: Literal["disable", "enable"] | None = None,
        log_unification: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        upstream_confirm: Literal["discover", "confirm"] | None = None,
        upstream_port: int | None = None,
        downstream_accprofile: str | None = None,
        fabric_connector: list[Any] | None = None,
        fixed_key: list[Any] | None = None,
        group_name: str | None = None,
        group_password: list[Any] | None = None,
        trusted_list: list[Any] | None = None,
        upstream: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            accept_auth_by_cert: accept-auth-by-cert parameter
            authorization_request_type: authorization-request-type parameter
            certificate: certificate parameter
            downstream_access: downstream-access parameter
            downstream_accprofile: downstream-accprofile parameter
            fabric_connector: fabric-connector parameter
            fabric_workers: fabric-workers parameter
            fixed_key: fixed-key parameter
            forticloud_account_enforcement: forticloud-account-enforcement parameter
            group_name: group-name parameter
            ... (8 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/csf"
        
        # Build data payload
        data = {}
        if accept_auth_by_cert is not None:
            data["accept-auth-by-cert"] = accept_auth_by_cert
        if authorization_request_type is not None:
            data["authorization-request-type"] = authorization_request_type
        if certificate is not None:
            data["certificate"] = certificate
        if downstream_access is not None:
            data["downstream-access"] = downstream_access
        if downstream_accprofile is not None:
            data["downstream-accprofile"] = downstream_accprofile
        if fabric_connector is not None:
            data["fabric-connector"] = fabric_connector
        if fabric_workers is not None:
            data["fabric-workers"] = fabric_workers
        if fixed_key is not None:
            data["fixed-key"] = fixed_key
        if forticloud_account_enforcement is not None:
            data["forticloud-account-enforcement"] = forticloud_account_enforcement
        if group_name is not None:
            data["group-name"] = group_name
        if group_password is not None:
            data["group-password"] = group_password
        if log_unification is not None:
            data["log-unification"] = log_unification
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if status is not None:
            data["status"] = status
        if trusted_list is not None:
            data["trusted-list"] = trusted_list
        if upstream is not None:
            data["upstream"] = upstream
        if upstream_confirm is not None:
            data["upstream-confirm"] = upstream_confirm
        if upstream_port is not None:
            data["upstream-port"] = upstream_port
        
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
        accept_auth_by_cert: Literal["disable", "enable"] | None = None,
        authorization_request_type: Literal["certificate", "serial"] | None = None,
        certificate: str | None = None,
        downstream_access: Literal["disable", "enable"] | None = None,
        fabric_workers: int | None = None,
        forticloud_account_enforcement: Literal["disable", "enable"] | None = None,
        log_unification: Literal["disable", "enable"] | None = None,
        ssl_protocol: Literal["follow-global-ssl-protocol", "sslv3", "tlsv1.0", "tlsv1.1", "tlsv1.2", "tlsv1.3"] | None = None,
        status: Literal["disable", "enable"] | None = None,
        upstream_confirm: Literal["discover", "confirm"] | None = None,
        upstream_port: int | None = None,
        downstream_accprofile: str | None = None,
        fabric_connector: list[Any] | None = None,
        fixed_key: list[Any] | None = None,
        group_name: str | None = None,
        group_password: list[Any] | None = None,
        trusted_list: list[Any] | None = None,
        upstream: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            accept_auth_by_cert: accept-auth-by-cert parameter
            authorization_request_type: authorization-request-type parameter
            certificate: certificate parameter
            downstream_access: downstream-access parameter
            downstream_accprofile: downstream-accprofile parameter
            fabric_connector: fabric-connector parameter
            fabric_workers: fabric-workers parameter
            fixed_key: fixed-key parameter
            forticloud_account_enforcement: forticloud-account-enforcement parameter
            group_name: group-name parameter
            ... (8 more parameters)
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/csf"
        
        # Build data payload
        data = {}
        if accept_auth_by_cert is not None:
            data["accept-auth-by-cert"] = accept_auth_by_cert
        if authorization_request_type is not None:
            data["authorization-request-type"] = authorization_request_type
        if certificate is not None:
            data["certificate"] = certificate
        if downstream_access is not None:
            data["downstream-access"] = downstream_access
        if downstream_accprofile is not None:
            data["downstream-accprofile"] = downstream_accprofile
        if fabric_connector is not None:
            data["fabric-connector"] = fabric_connector
        if fabric_workers is not None:
            data["fabric-workers"] = fabric_workers
        if fixed_key is not None:
            data["fixed-key"] = fixed_key
        if forticloud_account_enforcement is not None:
            data["forticloud-account-enforcement"] = forticloud_account_enforcement
        if group_name is not None:
            data["group-name"] = group_name
        if group_password is not None:
            data["group-password"] = group_password
        if log_unification is not None:
            data["log-unification"] = log_unification
        if ssl_protocol is not None:
            data["ssl-protocol"] = ssl_protocol
        if status is not None:
            data["status"] = status
        if trusted_list is not None:
            data["trusted-list"] = trusted_list
        if upstream is not None:
            data["upstream"] = upstream
        if upstream_confirm is not None:
            data["upstream-confirm"] = upstream_confirm
        if upstream_port is not None:
            data["upstream-port"] = upstream_port
        
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
