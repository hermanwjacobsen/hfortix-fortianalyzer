# HFortix-FortiAnalyzer

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

**HFortix-FortiAnalyzer** is a modern, fully-typed Python SDK for the
FortiAnalyzer JSON-RPC API — 315 endpoints generated from the official
FAZ 7.6.7 API specification, with full `.pyi` type stubs for IDE
autocomplete on every call. Sibling package of
[hfortix-fortimanager](https://github.com/hermanwjacobsen/hfortix-fortimanager)
(same transport, same conventions).

## 🚀 Quick Start

```bash
pip install hfortix-fortianalyzer
```

```python
from hfortix_fortianalyzer import FortiAnalyzer

# API key auth (FAZ 7.4.7+ / 7.6.2+) — no login/logout needed
faz = FortiAnalyzer(host="faz.example.com", api_key="your-api-key")

# Session auth — context manager handles login/logout
with FortiAnalyzer(host="faz.example.com", username="admin", password="pw") as faz:
    # Device inventory (Device Manager DB)
    devices = faz.api.dvmdb.adom.device.get(adom="root")
    for dev in devices:
        print(dev.name, dev.ip, dev.os_ver)

    # Event management — alerts in an ADOM
    alerts = faz.api.eventmgmt.adom.alerts.get(
        adom="root",
        limit=100,
        time_range={"start": "2026-07-01 00:00:00", "end": "2026-07-07 00:00:00"},
    )

    # Log search: start a search task, poll it, fetch results
    task = faz.api.logview.adom.logsearch.add(
        adom="root",
        device=[{"devid": "FGT60F0000000001"}],
        logtype="traffic",
        time_range={"start": "2026-07-06 00:00:00", "end": "2026-07-07 00:00:00"},
        filter='srcip=10.0.1.100',
    )
    results = faz.api.logview.adom.logsearch.get(adom="root", tid=task.tid)

    # Run a FortiView query
    faz.api.fortiview.adom.run.add(
        view_name="top-threats",
        adom="root",
        time_range={"start": "2026-07-06 00:00:00", "end": "2026-07-07 00:00:00"},
    )

    # Run a report (by schedule name)
    faz.api.report.adom.run.add(adom="root", schedule="Default Report")
```

## 📦 What is covered (generated from FAZ 7.6.7 specs)

| Namespace | Endpoints | Purpose |
| --- | --- | --- |
| `cli` | 169 | Full system/CLI configuration (`cli.global_.system.*`, `cli.global_.fmupdate.*`, `_meta_fields`, exec) |
| `report` | 35 | Report configuration (layouts, charts, datasets, schedules, outputs), run/export/import |
| `eventmgmt` | 23 | Alerts, alert logs, handlers, MITRE ATT&CK matrix |
| `soar` | 16 | Indicators, playbooks, connectors, SOAR task monitor |
| `fazsys` | 15 | FAZ system utilities (license info, fonts/translations, log rate, storage info) |
| `dvmdb` | 14 | Device Manager database (ADOMs, devices, groups, folders) |
| `sys` | 9 | System status, login/logout, proxy, reboot |
| `logview` | 8 | Log fields, log files, log search, log stats, PCAP |
| `incidentmgmt` | 8 | Incidents, attachments, endpoint/user history |
| `dvm` | 5 | Device add/delete commands (`dvm.cmd.*`, exec-style) |
| `ioc` | 4 | Indicators of compromise (rescan, events ack, license) |
| `task` | 3 | Task monitoring (`task.task`, `task.task.line`, `task.task.line.history`) |
| `sql_report` | 3 | SQL report helpers (layout folders, schedule devices/filters) |
| `um` | 2 | Update manager image upgrade (exec-style) |
| `fortiview` | 1 | FortiView query run/fetch/cancel (all views via `view_name=`) |

Total: **315 endpoints** (466 `.py` + 466 `.pyi` files). Every module of the
official FortiAnalyzer 7.6.7 API specification is generated — nothing was
excluded.

## 🧭 Navigation mirrors the API

URL scoping segments are kept, exactly like hfortix-fortimanager:

- `/dvmdb/adom/{adom}/device` → `faz.api.dvmdb.adom.device.get(adom="root")`
- `/eventmgmt/adom/{adom}/alerts` → `faz.api.eventmgmt.adom.alerts.get(adom="root")`
- `/dvmdb/device/{device}` (no ADOM) → `faz.api.dvmdb.device.get(device="fgt1")`
- Python keywords get a trailing underscore: `cli.global_`, `system.global_`
- Hyphenated API names become underscores in Python (`time_range=`,
  `view_name=`), but the **wire payload always uses the original API names**
  (`"time-range"`, `"indicator-uuid"`, …)

## ✨ Key Features

- **💪 Fully typed** — `.pyi` stubs for every endpoint; `Literal[...]` enums
  for every documented value; PEP 561 `py.typed`
- **🔑 Dual auth** — session (username/password with automatic re-login) or
  API key (Bearer, FAZ 7.4.7+/7.6.2+)
- **🤖 `apiver` handled for you** — v3-style endpoints (eventmgmt, logview,
  fortiview, report, soar, …) automatically send the required `apiver: 3`
- **📦 Minimal payloads** — only the parameters you pass are sent; FAZ
  applies its own server-side defaults (no surprise field writes)
- **🛡️ Production plumbing from hfortix-core** — retry with backoff,
  optional rate limiting and circuit breaker, audit logging, sanitized logs

## 🪄 Escape hatch — raw JSON-RPC

Anything not exposed as a typed endpoint can be called directly:

```python
result = faz.client.execute(
    method="get",
    params=[{"url": "/logview/adom/root/logstats", "apiver": 3}],
)
```

## ⚠️ Known limitations (0.1.x)

- **Generated offline from the 7.6.7 specs** — this release has not yet been
  validated call-by-call against a live FortiAnalyzer. Treat exotic endpoints
  with care and report issues.
- **One URL form per endpoint** — where the spec documents alternate URL
  forms (e.g. `/report/config/import` also existing as
  `/report/global/config/import` and un-scoped `/report/graph-file`), only
  the ADOM-scoped form is generated. Use the raw escape hatch for the others.
- **`/report/adom/root/template/language`** is generated as
  `report.adom.template.language.get(adom=...)` — pass `adom="root"` as the
  spec documents.
- **`model_registry` / `as_models()` / typed response models are experimental
  placeholders** — they currently return `None` / fall back to generic
  objects.
- **Sync only** — no async client yet (unlike hfortix-fortios).

## 🔗 Related Packages

This package is part of the HFortix SDK ecosystem:

- **[hfortix-core](https://github.com/hermanwjacobsen/hfortix-core)** — Core HTTP client and utilities
- **[hfortix-fortimanager](https://github.com/hermanwjacobsen/hfortix-fortimanager)** — FortiManager SDK (sibling)
- **[hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios)** — FortiOS/FortiGate SDK
- **[hfortix](https://github.com/hermanwjacobsen/hfortix)** — Meta package

## 📄 License

Proprietary license. All rights reserved.

## 🤝 Support

- **Issues**: https://github.com/hermanwjacobsen/hfortix-fortianalyzer/issues

---

**Version**: 0.1.0 (Alpha)
**FortiAnalyzer Support**: 7.6.7 (specs)
**Python**: 3.10+
