"""Type stubs for FortiAnalyzer client."""

from typing import Any
from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
from hfortix_fortianalyzer.api import API

__all__ = ["FortiAnalyzer"]


class FortiAnalyzer:
    """FortiAnalyzer API client with type-safe endpoint access."""
    
    api: API
    
    def __init__(
        self,
        host: str,
        username: str | None = None,
        password: str | None = None,
        api_key: str | None = None,
        api_user: str | None = None,
        port: int | None = None,
        verify: bool = True,
        adom: str | None = None,
    ) -> None: ...
    
    @property
    def client(self) -> HTTPClientJSONRPC: ...
    
    def login(self) -> None: ...
    def logout(self) -> None: ...
    def __enter__(self) -> "FortiAnalyzer": ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
