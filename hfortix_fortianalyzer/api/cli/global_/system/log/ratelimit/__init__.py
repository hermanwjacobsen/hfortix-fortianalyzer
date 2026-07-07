"""FortiAnalyzer ratelimit log API endpoints."""

from __future__ import annotations

from ..ratelimit_base import CliGlobalSystemLogRatelimit as CliGlobalSystemLogRatelimitBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ratelimits

__all__ = ["CliGlobalSystemLogRatelimit"]


class CliGlobalSystemLogRatelimit(CliGlobalSystemLogRatelimitBase):
    """FortiAnalyzer ratelimit log API endpoints."""

    ratelimits: "ratelimits.CliGlobalSystemLogRatelimitRatelimits"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize CliGlobalSystemLogRatelimit with endpoint methods and child modules."""
        super().__init__(client)

        from . import ratelimits as ratelimits_module

        self.ratelimits = ratelimits_module.CliGlobalSystemLogRatelimitRatelimits(client)
