"""
FortiAnalyzer API endpoint: cli.global.system.admin.profile.datamask-custom-fields

Auto-generated from swagger specification.
"""

from typing import Any
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAdminProfileDatamaskCustomFields:
    """
    FortiAnalyzer endpoint: cli.global.system.admin.profile.datamask-custom-fields
    
    
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
        profile: str,
        datamask_custom_fields: int | str | None = None,
        fields: list[Literal["field-category", "field-name", "field-status", "field-type"]] | None = None,
        filter: list[str] | None = None,
        loadsub: int | None = None,
        option: Literal["count", "syntax"] | None = None
    ) -> FortiAnalyzerResponse:
        """
        GET operation.
        
        Args:
            profile: profile parameter
            datamask_custom_fields: datamask-custom-fields parameter
            fields: Limit the output by returning only the attributes specified in the string array. If none specified, all attributes will be returned.
            filter: Filter the result according to a set of criteria.
            loadsub: Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.
            option: Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.<br/><b>count</b> - Return the number of matching entries instead of the actual entry data.<br/><b>syntax</b> - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None and datamask_custom_fields is not None:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}"
            url = url.replace("{profile}", profile)
            url = url.replace("{datamask-custom-fields}", str(datamask_custom_fields))
        else:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields"
            url = url.replace("{profile}", profile)
        
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
        profile: str,
        datamask_custom_fields: int | str | None = None,
        field_status: Literal["disable", "enable"] | None = None,
        field_type: Literal["string", "ip", "mac", "email", "unknown"] | None = None,
        field_category: list[Any] | None = None,
        field_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        ADD operation.
        
        Args:
            profile: profile parameter
            datamask_custom_fields: datamask-custom-fields parameter
            field_category: field-category parameter
            field_name: field-name parameter
            field_status: field-status parameter
            field_type: field-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields"
        url = url.replace("{profile}", profile)
        
        # Build data payload
        data = {}
        if field_category is not None:
            data["field-category"] = field_category
        if field_name is not None:
            data["field-name"] = field_name
        if field_status is not None:
            data["field-status"] = field_status
        if field_type is not None:
            data["field-type"] = field_type
        
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
        profile: str,
        datamask_custom_fields: int | str | None = None,
        field_status: Literal["disable", "enable"] | None = None,
        field_type: Literal["string", "ip", "mac", "email", "unknown"] | None = None,
        field_category: list[Any] | None = None,
        field_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            profile: profile parameter
            datamask_custom_fields: datamask-custom-fields parameter
            field_category: field-category parameter
            field_name: field-name parameter
            field_status: field-status parameter
            field_type: field-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None and datamask_custom_fields is not None:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}"
            url = url.replace("{profile}", profile)
            url = url.replace("{datamask-custom-fields}", str(datamask_custom_fields))
        else:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields"
            url = url.replace("{profile}", profile)
        
        # Build data payload
        data = {}
        if field_category is not None:
            data["field-category"] = field_category
        if field_name is not None:
            data["field-name"] = field_name
        if field_status is not None:
            data["field-status"] = field_status
        if field_type is not None:
            data["field-type"] = field_type
        
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
        profile: str,
        datamask_custom_fields: int | str | None = None,
        field_status: Literal["disable", "enable"] | None = None,
        field_type: Literal["string", "ip", "mac", "email", "unknown"] | None = None,
        field_category: list[Any] | None = None,
        field_name: str | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            profile: profile parameter
            datamask_custom_fields: datamask-custom-fields parameter
            field_category: field-category parameter
            field_name: field-name parameter
            field_status: field-status parameter
            field_type: field-type parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None and datamask_custom_fields is not None:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}"
            url = url.replace("{profile}", profile)
            url = url.replace("{datamask-custom-fields}", str(datamask_custom_fields))
        else:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields"
            url = url.replace("{profile}", profile)
        
        # Build data payload
        data = {}
        if field_category is not None:
            data["field-category"] = field_category
        if field_name is not None:
            data["field-name"] = field_name
        if field_status is not None:
            data["field-status"] = field_status
        if field_type is not None:
            data["field-type"] = field_type
        
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

    def delete(self, profile: str, datamask_custom_fields: int | str | None = None) -> FortiAnalyzerResponse:
        """
        DELETE operation.
        
        Args:
            profile: profile parameter
            datamask_custom_fields: datamask-custom-fields parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        # Path parameters are optional - if not provided, returns all objects
        if profile is not None and datamask_custom_fields is not None:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}"
            url = url.replace("{profile}", profile)
            url = url.replace("{datamask-custom-fields}", str(datamask_custom_fields))
        else:
            url = "/cli/global/system/admin/profile/{profile}/datamask-custom-fields"
            url = url.replace("{profile}", profile)
        
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
