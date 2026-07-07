"""Type stubs for soar.adom.config.playbooks"""

from typing import Any, Iterator

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class SoarAdomConfigPlaybooks:
    """FortiAnalyzer endpoint: soar.adom.config.playbooks"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def add(
        self,
        adom: str,
        data: list[dict[str, Any]],
        playbook_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """ADD operation."""
        ...

    def update(
        self,
        adom: str,
        data: list[dict[str, Any]],
        playbook_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """UPDATE operation."""
        ...

    def delete(
        self,
        adom: str,
        playbook_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """DELETE operation."""
        ...

    def get(
        self,
        adom: str,
        playbook_uuid: int | str | None = None,
        apiver: int = 3,
    ) -> FortiAnalyzerResponse:
        """GET operation."""
        ...


__all__ = ["SoarAdomConfigPlaybooks"]