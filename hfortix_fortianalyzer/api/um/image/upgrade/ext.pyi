"""Type stubs for um.image.upgrade.ext"""

from typing import Any, Iterator
from typing import Literal

from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.models import FortiAnalyzerResponse


class UmImageUpgradeExtExecItem:
    """Item yielded when iterating over UmImageUpgradeExtExecResponse."""

    @property
    def taskid(self) -> list[Any]: ...

    # Inherited from FortiAnalyzerObject
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def __getitem__(self, key: str) -> Any: ...


class UmImageUpgradeExtExecResponse(FortiAnalyzerResponse):
    """Typed response for UmImageUpgradeExtExec endpoint with autocomplete support."""

    # ========================================================================
    # HTTP Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def http_status_code(self) -> int | None: ...
    @property
    def http_response_time(self) -> float | None: ...
    @property
    def http_method(self) -> str | None: ...
    @property
    def http_url(self) -> str | None: ...

    # ========================================================================
    # API Layer Properties (inherited from FortiAnalyzerResponse)
    # ========================================================================
    @property
    def api_status_code(self) -> int | None: ...
    @property
    def api_status_message(self) -> str | None: ...
    @property
    def api_id(self) -> int | None: ...
    @property
    def api_url(self) -> str | None: ...
    @property
    def api_raw(self) -> dict[str, Any]: ...

    # ========================================================================
    # Data Fields (specific to this endpoint)
    # ========================================================================
    @property
    def taskid(self) -> list[Any] | None:
        """Field: taskid"""
        ...


    # Inherited methods from FortiAnalyzerResponse
    @property
    def raw(self) -> dict[str, Any]: ...
    @property
    def dict(self) -> dict[str, Any]: ...
    @property
    def json(self) -> str: ...
    def get(self, key: str, default: Any = None) -> Any: ...
    def __getitem__(self, key: str) -> Any: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[UmImageUpgradeExtExecItem]: ...
    def __len__(self) -> int: ...


class UmImageUpgradeExt:
    """FortiAnalyzer endpoint: um.image.upgrade.ext"""

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...

    def exec(
        self,
        create_task: str | None = None,
        device: list[Any] | None = None,
        flags: Literal["f_boot_alt_partition", "f_skip_retrieve", "f_skip_multi_steps", "f_skip_fortiguard_img", "f_preview"] | None = None,
        image: str | None = None,
        schedule_time: str | None = None,
    ) -> UmImageUpgradeExtExecResponse:
        """EXEC operation."""
        ...


__all__ = ["UmImageUpgradeExt", "UmImageUpgradeExtExecResponse"]