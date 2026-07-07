"""Type stubs for FortiAnalyzer API module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from .ca import CliGlobalSystemCertificateCa
    from .crl import CliGlobalSystemCertificateCrl
    from .local import CliGlobalSystemCertificateLocal
    from .oftp import CliGlobalSystemCertificateOftp
    from .remote import CliGlobalSystemCertificateRemote
    from .ssh import CliGlobalSystemCertificateSsh

__all__ = ["Certificate"]


class Certificate:
    """Certificate endpoints."""

    ca: CliGlobalSystemCertificateCa
    crl: CliGlobalSystemCertificateCrl
    local: CliGlobalSystemCertificateLocal
    oftp: CliGlobalSystemCertificateOftp
    remote: CliGlobalSystemCertificateRemote
    ssh: CliGlobalSystemCertificateSsh

    def __init__(self, client: HTTPClientJSONRPC) -> None: ...
