"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ext import UmImageUpgradeExt

__all__ = ["UmImageUpgrade"]


from ..upgrade_base import UmImageUpgrade as UmImageUpgradeBase

class UmImageUpgrade(UmImageUpgradeBase):
    """UmImageUpgrade endpoints."""

    ext: UmImageUpgradeExt

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
