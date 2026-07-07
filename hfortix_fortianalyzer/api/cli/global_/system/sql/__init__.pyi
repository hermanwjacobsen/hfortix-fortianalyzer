"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .custom_index import CliGlobalSystemSqlCustomIndex
    from .custom_skipidx import CliGlobalSystemSqlCustomSkipidx
    from .ts_index_field import CliGlobalSystemSqlTsIndexField

__all__ = ["CliGlobalSystemSql"]


from ..sql_base import CliGlobalSystemSql as CliGlobalSystemSqlBase

class CliGlobalSystemSql(CliGlobalSystemSqlBase):
    """CliGlobalSystemSql endpoints."""

    custom_index: CliGlobalSystemSqlCustomIndex
    custom_skipidx: CliGlobalSystemSqlCustomSkipidx
    ts_index_field: CliGlobalSystemSqlTsIndexField

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
