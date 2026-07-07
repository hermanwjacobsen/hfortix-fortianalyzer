"""Type stubs for typed response classes."""

from typing import Iterator
from hfortix_fortianalyzer.models import FortiAnalyzerResponse
from hfortix_fortianalyzer.api.models.dvmdb.device import DvmdbDeviceModel


class DvmdbDeviceResponse(FortiAnalyzerResponse):
    """Typed response for /dvmdb/device endpoint."""
    
    def __iter__(self) -> Iterator[DvmdbDeviceModel]: ...  # type: ignore[override]


__all__ = ["DvmdbDeviceResponse"]
