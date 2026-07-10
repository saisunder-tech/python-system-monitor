# Python System Monitor

A modular Python-based Linux system monitoring tool that displays real-time system information such as CPU, memory, disk usage, hostname, IP address, uptime, and logged-in users. The application also generates warnings for high CPU utilization and records events in a log file.

## Features

* CPU usage monitoring
* Memory (RAM) usage monitoring
* Disk usage monitoring
* Hostname and IP address display
* System uptime reporting
* Logged-in user listing
* Configurable alerts for high CPU usage
* Logging to `system.log`

## Project Structure

```text
python-system-monitor/
├── monitor.py
├── cpu.py
├── memory.py
├── disk.py
├── logger.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.8 or later
* Linux operating system
* `psutil` Python package

## Getting Started

1. Create and activate a Python virtual environment.
2. Install the dependencies from `requirements.txt`.
3. Run `monitor.py` to view system statistics.

## Future Enhancements

This project will be progressively extended with Git workflows, Azure DevOps CI/CD, Docker containerization, Kubernetes deployment, and execution on Azure Linux virtual machines.
