"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .dlp_files_auto_deletion import CliGlobalSystemAutoDeleteDlpFilesAutoDeletion
    from .log_auto_deletion import CliGlobalSystemAutoDeleteLogAutoDeletion
    from .quarantine_files_auto_deletion import CliGlobalSystemAutoDeleteQuarantineFilesAutoDeletion
    from .report_auto_deletion import CliGlobalSystemAutoDeleteReportAutoDeletion

__all__ = ["CliGlobalSystemAutoDelete"]


from ..auto_delete_base import CliGlobalSystemAutoDelete as CliGlobalSystemAutoDeleteBase

class CliGlobalSystemAutoDelete(CliGlobalSystemAutoDeleteBase):
    """CliGlobalSystemAutoDelete endpoints."""

    dlp_files_auto_deletion: CliGlobalSystemAutoDeleteDlpFilesAutoDeletion
    log_auto_deletion: CliGlobalSystemAutoDeleteLogAutoDeletion
    quarantine_files_auto_deletion: CliGlobalSystemAutoDeleteQuarantineFilesAutoDeletion
    report_auto_deletion: CliGlobalSystemAutoDeleteReportAutoDeletion

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
