"""FortiAnalyzer Python API client with type-safe endpoints."""

from . import api
from .client import FortiAnalyzer
from .models import (
    FortiAnalyzerList,
    FortiAnalyzerObject,
    FortiAnalyzerResponse,
)

__version__ = "0.1.0"

__all__ = [
    "FortiAnalyzer",
    "FortiAnalyzerResponse",
    "FortiAnalyzerObject",
    "FortiAnalyzerList",
    "api",
]
