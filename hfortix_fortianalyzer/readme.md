# FortiAnalyzer Python SDK

Type-safe Python API client for FortiAnalyzer with generated endpoints.

## Status

🚧 Early development - generated from FortiAnalyzer 7.6.5 swagger specifications.

## Features

- JSON-RPC based API client (reuses HTTPClientFMG from hfortix-core)
- Type-safe generated endpoints
- Session-based and API key authentication
- IDE autocomplete support

## Installation

```bash
pip install hfortix-fortianalyzer
```

## Usage

```python
from hfortix import FortiAnalyzer

# Create client
faz = FortiAnalyzer(
    url="https://fortianalyzer.example.com",
    username="admin",
    password="password"
)

# Login
faz.login()

# Use generated endpoints
from hfortix_fortianalyzer.api.dvmdb.device import DvmdbDevice

devices = DvmdbDevice(faz.client)
result = devices.get(adom="root")

# Logout
faz.logout()
```

## Generated Endpoints

Currently generated from dvmdb module:
- dvmdb.adom
- dvmdb.device
- dvmdb.vdom
- dvmdb.folder
- dvmdb.group
- dvmdb.ha_slave

More modules coming soon!
