"""FortiAnalyzer upgrade image API endpoints."""

from __future__ import annotations

from ..upgrade_base import UmImageUpgrade as UmImageUpgradeBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ext

__all__ = ["UmImageUpgrade"]


class UmImageUpgrade(UmImageUpgradeBase):
    """FortiAnalyzer upgrade image API endpoints."""

    ext: "ext.UmImageUpgradeExt"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize UmImageUpgrade with endpoint methods and child modules."""
        super().__init__(client)

        from . import ext as ext_module

        self.ext = ext_module.UmImageUpgradeExt(client)
