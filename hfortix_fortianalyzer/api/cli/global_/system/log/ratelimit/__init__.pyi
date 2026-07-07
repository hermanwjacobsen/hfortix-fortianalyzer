"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ratelimits import CliGlobalSystemLogRatelimitRatelimits

__all__ = ["CliGlobalSystemLogRatelimit"]


from ..ratelimit_base import CliGlobalSystemLogRatelimit as CliGlobalSystemLogRatelimitBase

class CliGlobalSystemLogRatelimit(CliGlobalSystemLogRatelimitBase):
    """CliGlobalSystemLogRatelimit endpoints."""

    ratelimits: CliGlobalSystemLogRatelimitRatelimits

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
