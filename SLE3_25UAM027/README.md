# SLE-3: C4 Architecture Model Mapping

This directory contains the architectural design documentation for the **Basic AI Agent** system, structured according to the **C4 Model framework** (Context, Container, Component, and Code). 

The objective of this assignment is to map out how the Python-based application initializes system configurations, processes user prompt data, and interfaces with remote Large Language Models (LLMs).

---

## 📂 Project Directory Structure

All files related to this architectural mapping are contained within the `SLE3_25UAM027` directory:

```text
Basic-AI-agent/
└── SLE3_25UAM027/
    ├── CODES/
    │   ├── c1_context.py
    │   ├── c2_container.py
    │   ├── c3_component.py
    │   └── c4_code.py
    └── Diagrams/
        ├── C1_context_diagram.png
        ├── C2_container_diagram.png
        ├── C3_component_diagram.png
        └── C4_code_diagram.png
```

---

## 🏛️ C4 Level Breakdown

### 🎯 Level 1: System Context Diagram
*   **Purpose:** Outlines the high-level scope of the AI Agent application, defining system boundaries and showing interactions with human users and external systems.
*   **Key Elements:** 
    *   **User:** Interacts with the interface, providing prompts and receiving text responses.
    *   **Basic AI Agent System:** The core software application boundary.
    *   **OpenAI API:** External foundational AI model platform managing response generations.
*   **Artifacts:** `CODES/c1_context.py` | `Diagrams/C1_context_diagram.png`

### 📦 Level 2: Container Diagram
*   **Purpose:** Zooms into the system boundary to showcase the technical building blocks (containers) and structural data workflows.
*   **Key Containers:**
    *   **Console UI / Terminal:** Reads inputs and prints the system text responses.
    *   **Python App Execution Core:** The runtime engine handling processing logic.
    *   **Local File System (`.env`):** Secure key-value storage managing operational settings and secrets.
*   **Artifacts:** `CODES/c2_container.py` | `Diagrams/C2_container_diagram.png`

### 🧩 Level 3: Component Diagram
*   **Purpose:** Breaks down the Python App container into its internal logical code blocks and responsibilities.
*   **Key Components:**
    *   **Input Handler:** Sanitizes and routes raw user terminal parameters.
    *   **Config Loader:** Uses `python-dotenv` modules to parse environment values securely.
    *   **LLM Client Layer:** Orchestrates secure network connections to remote cloud services.
    *   **Response Parser:** Extracts relevant message payloads and handles fallbacks.
*   **Artifacts:** `CODES/c3_component.py` | `Diagrams/C3_component_diagram.png`

### 💻 Level 4: Code Diagram
*   **Purpose:** The granular architectural view showing classes, functions, and interface structures powering `src/agent.py`.
*   **Key Elements:**
    *   `load_environment()`: Validates environment initialization states.
    *   `Agent` Class: The primary object-oriented wrapper managing the runtime lifecycle.
    *   `generate_response()`: The execution method wrapping the LLM chat completions.
*   **Artifacts:** `CODES/c4_code.py` | `Diagrams/C4_code_diagram.png`

---

## 🛠️ Technology Stack Used
*   **Python 3:** Target application execution environment.
*   **Diagrams-as-Code Framework:** Programmatic generation of PNG architectural layouts.
*   **Git / GitHub:** Version tracking, control, and remote repository syncing.
