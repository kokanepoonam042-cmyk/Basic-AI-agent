# Basic-AI-agent (SLE-2)

A Python-based AI agent environment built for search and optimization scripts. This repository manages agent configurations, execution workflows, and testing metrics.

## 📁 Repository Structure
```text
Basic-AI-agent/
├── CONTRIBUTION_LOG.md    # Tracks version changes and developer updates
├── README.md                # Project overview and execution manual
├── tests/                   # Folder housing target test modules
└── SLE-2/                   # Main executable sandbox environment
    ├── search.py            # Primary core execution script
    ├── result.txt           # Generated operational script outputs
    └── profile.svg          # Visual performance profiling graphic
```

## ⚙️ Prerequisites & Setup

### 1. Requirements
* **Python 3.10+** must be installed on your operating system.

### 2. Quick CLI Setup (Windows)
If running scripts directly via terminal scripts throws a "Python not found" exception, configure your workspace using the Windows package manager (`winget`) within PowerShell:
```powershell
winget install --id Python.Python.3.12 --source winget
```
*Note: Make sure to restart your terminal window or VS Code window after installation complete notifications finish to update structural global pathways.*

## 🚀 Running the Agent

1. Launch your command terminal environment and target your local development subfolder:
   ```bash
   cd C:/Users/Admin/Basic-AI-agent/SLE-2
   ```

2. Execute the primary operational logic framework task:
   ```bash
   python search.py
   ```

## 🛠️ Contribution Guidelines
* Document all pipeline alterations, added dependencies, and debugging modifications clearly within the top-level directory file named `CONTRIBUTION_LOG.md`.
* Ensure profile changes do not unintentionally clear output files (`result.txt`) without passing local criteria validations.
