"""FortiAnalyzer auto_delete system API endpoints."""

from __future__ import annotations

from ..auto_delete_base import CliGlobalSystemAutoDelete as CliGlobalSystemAutoDeleteBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import dlp_files_auto_deletion
    from . import log_auto_deletion
    from . import quarantine_files_auto_deletion
    from . import report_auto_deletion

__all__ = ["CliGlobalSystemAutoDelete"]


class CliGlobalSystemAutoDelete(CliGlobalSystemAutoDeleteBase):
    """FortiAnalyzer auto_delete system API endpoints."""

    dlp_files_auto_deletion: "dlp_files_auto_deletion.CliGlobalSystemAutoDeleteDlpFilesAutoDeletion"
    log_auto_deletion: "log_auto_deletion.CliGlobalSystemAutoDeleteLogAutoDeletion"
    quarantine_files_auto_deletion: "quarantine_files_auto_deletion.CliGlobalSystemAutoDeleteQuarantineFilesAutoDeletion"
    report_auto_deletion: "report_auto_deletion.CliGlobalSystemAutoDeleteReportAutoDeletion"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemAutoDelete with endpoint methods and child modules."""
        super().__init__(client)

        from . import dlp_files_auto_deletion as dlp_files_auto_deletion_module
        from . import log_auto_deletion as log_auto_deletion_module
        from . import quarantine_files_auto_deletion as quarantine_files_auto_deletion_module
        from . import report_auto_deletion as report_auto_deletion_module

        self.dlp_files_auto_deletion = dlp_files_auto_deletion_module.CliGlobalSystemAutoDeleteDlpFilesAutoDeletion(client)
        self.log_auto_deletion = log_auto_deletion_module.CliGlobalSystemAutoDeleteLogAutoDeletion(client)
        self.quarantine_files_auto_deletion = quarantine_files_auto_deletion_module.CliGlobalSystemAutoDeleteQuarantineFilesAutoDeletion(client)
        self.report_auto_deletion = report_auto_deletion_module.CliGlobalSystemAutoDeleteReportAutoDeletion(client)
