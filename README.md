# Code Mapping & Visualization Tool
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![Inspired By](https://img.shields.io/badge/Inspired%20By-Obsidian-purple)

This project is a **code mapping and visualization tool** inspired by how **Obsidian** visualizes knowledge graphs. Instead of notes, it focuses on **source code**: files, functions, imports, and their relationships.

Think of it as turning a codebase into a living map, where you can *see* how everything connects rather than mentally simulating it line by line.

---

## 🎯 Purpose

Large codebases fail in the same way large cities do: navigation becomes hard.

This tool helps you:

* Understand **file-level and function-level dependencies**
* See **who imports whom** and **who calls what**
* Generate a **graph view** similar to Obsidian’s graph mode
* Make reverse‑engineering and code comprehension faster (especially useful for CTFs and security reviews)

---

## 🧠 How It Works (Conceptual Flow)

1. **Scan source files**

   * Walks through the project directory
   * Identifies supported source files (currently Python-focused)

2. **Parse code**

   * Extracts:

     * Imports
     * Function definitions
     * Function calls

3. **Build an internal dependency map**

   * File → File relationships (imports)
   * Function → Function relationships (calls)

4. **Visualize the graph**

   * Converts the dependency map into a graph structure
   * Renders it in a node-edge format similar to Obsidian’s graph view

---

## 📁 Project Structure

```text
NeuroCode/
│
│
├── parser/
│   └── python_parser.py    # AST-based Python code parser
│
├── scanner/
│   ├── scan.py             # Project-wide file scanning logic
│   ├── cache.py            # Parsed data caching layer
│   ├── hashh.py            # File/content hashing utilities
│   └── export_graph.py     # Graph data export (nodes & edges)
│
├── storage/                # Persistent storage for parsed data / graphs
│
├── web/
│   └── index.html          # Web-based graph visualization UI
│
├── main.py                 # Application entry point
├── reset_storage.py        # Utility to clear stored graph/cache data
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore              # Git ignore rules


```

---

## 🔍 Example Output (Logical)

```json
{
  "main.py": {
    "imports": ["scanner.scan", "parser.python_parser"],
    "functions": ["run"],
    "calls": ["scan_project"]
  }
}
```

This structure is then transformed into a **node graph**:

* Nodes → files / functions
* Edges → imports / calls

---

## 🧪 Current Status

* ✅ Code scanning works
* ✅ Dependency extraction works
* ✅ Graph rendering pipeline works
* ⚠️ UI may initially show a blank page if graph data is empty or malformed (now fixed)

---

## 🛠️ Technologies Used

* Python
* AST (Abstract Syntax Tree)
* Graph-based visualization (Obsidian-style logic)

---

## 🚀 Future Improvements

* Language-agnostic parsing (C/C++, JavaScript)
* Interactive UI (zoom, filter, isolate nodes)
* Security-focused overlays (attack surface mapping)
* Export to GraphML / JSON for external tools

---

## 🧩 Why This Matters

Humans understand **structures**, not raw text.

A graph turns code from something you *read* into something you can *navigate*.
For reverse engineering, auditing, or learning a new codebase — this is leverage.

---

## 📜 License

MIT License (feel free to learn, fork, and extend)
