"""FortiAnalyzer sql system API endpoints."""

from __future__ import annotations

from ..sql_base import CliGlobalSystemSql as CliGlobalSystemSqlBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import custom_index
    from . import custom_skipidx
    from . import ts_index_field

__all__ = ["CliGlobalSystemSql"]


class CliGlobalSystemSql(CliGlobalSystemSqlBase):
    """FortiAnalyzer sql system API endpoints."""

    custom_index: "custom_index.CliGlobalSystemSqlCustomIndex"
    custom_skipidx: "custom_skipidx.CliGlobalSystemSqlCustomSkipidx"
    ts_index_field: "ts_index_field.CliGlobalSystemSqlTsIndexField"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemSql with endpoint methods and child modules."""
        super().__init__(client)

        from . import custom_index as custom_index_module
        from . import custom_skipidx as custom_skipidx_module
        from . import ts_index_field as ts_index_field_module

        self.custom_index = custom_index_module.CliGlobalSystemSqlCustomIndex(client)
        self.custom_skipidx = custom_skipidx_module.CliGlobalSystemSqlCustomSkipidx(client)
        self.ts_index_field = ts_index_field_module.CliGlobalSystemSqlTsIndexField(client)
