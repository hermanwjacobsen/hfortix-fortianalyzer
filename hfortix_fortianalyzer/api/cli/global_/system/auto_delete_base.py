"""
FortiAnalyzer API endpoint: cli.global.system.auto-delete

Auto-generated from swagger specification.
"""

from typing import Any

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class CliGlobalSystemAutoDelete:
    """
    FortiAnalyzer endpoint: cli.global.system.auto-delete
    
    
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
        url = "/cli/global/system/auto-delete"
        
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
        dlp_files_auto_deletion: dict[str, Any] | None = None,
        log_auto_deletion: dict[str, Any] | None = None,
        quarantine_files_auto_deletion: dict[str, Any] | None = None,
        report_auto_deletion: dict[str, Any] | None = None,
        status_fake: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        SET operation.
        
        Args:
            dlp_files_auto_deletion: Nested object (schema: cli.system.auto-delete.dlp-files-auto-deletion).
            log_auto_deletion: Nested object (schema: cli.system.auto-delete.log-auto-deletion).
            quarantine_files_auto_deletion: Nested object (schema: cli.system.auto-delete.quarantine-files-auto-deletion).
            report_auto_deletion: Nested object (schema: cli.system.auto-delete.report-auto-deletion).
            status_fake: status-fake parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/auto-delete"
        
        # Build data payload
        data = {}
        if dlp_files_auto_deletion is not None:
            data["dlp-files-auto-deletion"] = dlp_files_auto_deletion
        if log_auto_deletion is not None:
            data["log-auto-deletion"] = log_auto_deletion
        if quarantine_files_auto_deletion is not None:
            data["quarantine-files-auto-deletion"] = quarantine_files_auto_deletion
        if report_auto_deletion is not None:
            data["report-auto-deletion"] = report_auto_deletion
        if status_fake is not None:
            data["status-fake"] = status_fake
        
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
        dlp_files_auto_deletion: dict[str, Any] | None = None,
        log_auto_deletion: dict[str, Any] | None = None,
        quarantine_files_auto_deletion: dict[str, Any] | None = None,
        report_auto_deletion: dict[str, Any] | None = None,
        status_fake: int | None = None
    ) -> FortiAnalyzerResponse:
        """
        UPDATE operation.
        
        Args:
            dlp_files_auto_deletion: Nested object (schema: cli.system.auto-delete.dlp-files-auto-deletion).
            log_auto_deletion: Nested object (schema: cli.system.auto-delete.log-auto-deletion).
            quarantine_files_auto_deletion: Nested object (schema: cli.system.auto-delete.quarantine-files-auto-deletion).
            report_auto_deletion: Nested object (schema: cli.system.auto-delete.report-auto-deletion).
            status_fake: status-fake parameter
        
        Returns:
            Response data from FortiAnalyzer API
        """
        # Build URL
        url = "/cli/global/system/auto-delete"
        
        # Build data payload
        data = {}
        if dlp_files_auto_deletion is not None:
            data["dlp-files-auto-deletion"] = dlp_files_auto_deletion
        if log_auto_deletion is not None:
            data["log-auto-deletion"] = log_auto_deletion
        if quarantine_files_auto_deletion is not None:
            data["quarantine-files-auto-deletion"] = quarantine_files_auto_deletion
        if report_auto_deletion is not None:
            data["report-auto-deletion"] = report_auto_deletion
        if status_fake is not None:
            data["status-fake"] = status_fake
        
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
