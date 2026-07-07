"""
FortiAnalyzer API endpoint: cli.global.system.certificate.ssh

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemCertificateSsh:
    """
    FortiAnalyzer endpoint: cli.global.system.certificate.ssh
    
    
    Available methods: get, add, set, update, delete
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
        ssh: int | str | None = None,
        fields: list[Literal["certificate", "comment", "name", "password", "private-key"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            ssh: ssh parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ssh is not None:
            url = "/cli/global/system/certificate/ssh/{ssh}"
            url = url.replace("{ssh}", str(ssh))
        else:
            url = "/cli/global/system/certificate/ssh"
        
        # Build request parameters
        # For GET, parameters go at the top level of params (not inside data)
        if fields is not None and fields and not isinstance(fields[0], list):
            fields = [fields]
        
        request_params = {}
        if fields is not None:
            request_params["fields"] = fields
        if filter is not None:
            request_params["filter"] = filter
        if loadsub is not None:
            request_params["loadsub"] = loadsub
        if option is not None:
            request_params["option"] = option
        
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

    def add(
        self,
        ssh: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            ssh: ssh parameter
            certificate: certificate parameter
            comment: comment parameter
            name: name parameter
            password: password parameter
            private_key: private-key parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/certificate/ssh"
        
        # Build data payload
        data = {}
        if certificate is not None:
            data["certificate"] = certificate
        if comment is not None:
            data["comment"] = comment
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if private_key is not None:
            data["private-key"] = private_key
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
            "data": data
        }]
        
        response = self._client.execute(
            method="add",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)

    def set(
        self,
        ssh: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            ssh: ssh parameter
            certificate: certificate parameter
            comment: comment parameter
            name: name parameter
            password: password parameter
            private_key: private-key parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ssh is not None:
            url = "/cli/global/system/certificate/ssh/{ssh}"
            url = url.replace("{ssh}", str(ssh))
        else:
            url = "/cli/global/system/certificate/ssh"
        
        # Build data payload
        data = {}
        if certificate is not None:
            data["certificate"] = certificate
        if comment is not None:
            data["comment"] = comment
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if private_key is not None:
            data["private-key"] = private_key
        
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
        ssh: int | str | None = None,
        certificate: list[Any] | None = None,
        comment: str | None = None,
        name: str | None = None,
        password: list[Any] | None = None,
        private_key: list[Any] | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            ssh: ssh parameter
            certificate: certificate parameter
            comment: comment parameter
            name: name parameter
            password: password parameter
            private_key: private-key parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ssh is not None:
            url = "/cli/global/system/certificate/ssh/{ssh}"
            url = url.replace("{ssh}", str(ssh))
        else:
            url = "/cli/global/system/certificate/ssh"
        
        # Build data payload
        data = {}
        if certificate is not None:
            data["certificate"] = certificate
        if comment is not None:
            data["comment"] = comment
        if name is not None:
            data["name"] = name
        if password is not None:
            data["password"] = password
        if private_key is not None:
            data["private-key"] = private_key
        
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

    def delete(self, ssh: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            ssh: ssh parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if ssh is not None:
            url = "/cli/global/system/certificate/ssh/{ssh}"
            url = url.replace("{ssh}", str(ssh))
        else:
            url = "/cli/global/system/certificate/ssh"
        
        data = {}
        
        # Execute JSON-RPC API call
        params = [{
            "url": url,
        }]
        
        response = self._client.execute(
            method="delete",
            params=params
        )
        
        # Wrap response in FortiAnalyzerResponse for clean attribute access
        return FortiAnalyzerResponse(response)
