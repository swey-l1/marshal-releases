# Marshal — Releases

[![Downloads](https://img.shields.io/github/downloads/swey-l1/marshal-releases/total?label=downloads&color=7C6CF6)](https://github.com/swey-l1/marshal-releases/releases/latest)


Download builds of **Marshal**, a modern Windows process manager: priority/affinity control, the **AutoTame** background-CPU balancer, persistent rules, **Gaming Mode**, a live monitor, and a system tray.

**🌐 Product page:** https://marshal.aimbetween.games

## Download

Latest build: **https://github.com/swey-l1/marshal-releases/releases/latest/download/marshal.exe** (Windows x64)

Or browse the [Releases page](https://github.com/swey-l1/marshal-releases/releases/latest).

### Verify your download (optional)

```powershell
(Get-FileHash marshal.exe -Algorithm SHA256).Hash
```

Compare the result with `marshal.exe.sha256` attached to the release.

## SmartScreen note

The binary is currently **unsigned**, so Windows SmartScreen may show *"Windows protected your PC."*
Click **More info → Run anyway**. Code signing is planned.

---

This repository hosts only the compiled binaries. The source code is maintained privately.
