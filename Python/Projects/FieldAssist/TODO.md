# FieldAssist TODO

## Core Project

- [x] Project structure
- [x] Main application entry point
- [x] System information collector
- [x] Disk information collector
- [x] Reusable byte conversion utility

---

## System Information

### Improvements
- [ ] Replace `platform.system()` with Windows CIM
- [ ] Replace `platform.processor()` with friendly CPU name
- [ ] Get manufacturer
- [ ] Get model
- [ ] Get BIOS version

---

## Disk Information

### Improvements
- [x] Collect C: drive usage
- [ ] Support multiple drives
- [ ] Display filesystem type
- [ ] Add SMART health information
- [ ] Add disk serial number

---

## Memory Information

- [x] Collect total RAM
- [x] Collect available RAM
- [x] Collect used RAM
- [x] Display memory usage %

---

## Network Information

- [ ] IP address
- [ ] Default gateway
- [ ] DNS servers
- [ ] MAC address
- [ ] Network adapter(s)
- [ ] Connection status

---

## Reporting

- [x] Terminal report
- [ ] Export to text file
- [ ] Export to JSON
- [ ] Export to HTML

---

## Analysis

- [ ] Low disk space warning
- [ ] High RAM usage warning
- [ ] Offline network warning
- [ ] Health summary

---

## Future Features

- [ ] Battery information
- [ ] BitLocker status
- [ ] Event Log collection
- [ ] Windows Update status
- [ ] dsregcmd analysis
- [ ] Installed software
- [ ] Services

## Learning Goals

- [x] Functions
- [x] Dictionaries
- [x] Modules
- [x] Imports
- [x] Returning dictionaries
- [x] Third-party packages (psutil)
- [x] Reusable utility functions
- [ ] Classes
- [ ] Unit testing
- [ ] Logging
- [ ] Exception handling
- [ ] FastAPI
- [ ] PowerShell integration