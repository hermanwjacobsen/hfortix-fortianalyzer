"""FortiAnalyzer certificate system API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.jsonrpc_client import HTTPClientJSONRPC
    from . import ca
    from . import crl
    from . import local
    from . import oftp
    from . import remote
    from . import ssh

__all__ = ["Certificate"]


class Certificate:
    """FortiAnalyzer certificate system API endpoints."""

    ca: "ca.CliGlobalSystemCertificateCa"
    crl: "crl.CliGlobalSystemCertificateCrl"
    local: "local.CliGlobalSystemCertificateLocal"
    oftp: "oftp.CliGlobalSystemCertificateOftp"
    remote: "remote.CliGlobalSystemCertificateRemote"
    ssh: "ssh.CliGlobalSystemCertificateSsh"

    def __init__(self, client: "HTTPClientJSONRPC") -> None:
        """Initialize Certificate namespace with JSON-RPC client."""
        from . import ca as ca_module
        from . import crl as crl_module
        from . import local as local_module
        from . import oftp as oftp_module
        from . import remote as remote_module
        from . import ssh as ssh_module

        self.ca = ca_module.CliGlobalSystemCertificateCa(client)
        self.crl = crl_module.CliGlobalSystemCertificateCrl(client)
        self.local = local_module.CliGlobalSystemCertificateLocal(client)
        self.oftp = oftp_module.CliGlobalSystemCertificateOftp(client)
        self.remote = remote_module.CliGlobalSystemCertificateRemote(client)
        self.ssh = ssh_module.CliGlobalSystemCertificateSsh(client)
