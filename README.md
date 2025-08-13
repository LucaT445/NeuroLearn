# NeuroLearn

Learn brain anatomy interactively with a 3D model and AI-powered Q&A. 

[![CI Status](https://github.com/LucaT445/NeuroLearn/actions/workflows/ci.yml/badge.svg)](https://github.com/LucaT445/NeuroLearn/actions) [![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://github.com/LucaT445/NeuroLearn/blob/main/LICENSE)

---

## Table Of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Demo](#demo)
4. [Requirements & Dependencies](#requirements--dependencies) 
5. [Installation](#installation)
6. [Usage](#usage)
7. [Configuration](#configuration)
8. [Testing](#testing)
9. [License](#license)

---

### Overview

NeuroLearn is an interactive tool for learning brain anatomy. 
It features a color-coded 3D model of the human brain showing each region's functions, location, and associated disorders, and a built-in AI Q&A system to explore related topics beyond the model. It is designed for students, self-learners, and educators.

---

### Features

1. **Interactive 3D Model** — Rotate, zoom, and click regions to see details for hands-on learning.
2. **Region Details** — Functions, locations, and associated disorders on select for quick reference.
3. **Built-in AI Q&A** — Topics beyond the model (educational scope; requires `OPENAI_API_KEY`) for extended learning.
4. **Clean, responsive layout** — Comfortable on laptops and desktops for an easy viewing experience.
5. **Background/theming** — Subtle neuron video backdrop for added visual context.

---

### Demo

---

### Requirements & Dependencies

- **Python 3.10+** is required
- **Git** for cloning the repository
- **Virtual Environment** tool (e.g. `venv`) is recommended
- **Core Dependencies**:
    - `dash` — web application framework
    - `plotly` — interactive 3D visualization
    - `openai` — AI-powered Q&A
    - `trimesh` — 3D geometry handling
    - `python-dotenv` — loads the environment variables from `.env`
- Install all dependencies with:
```bash
pip install -r dependencies.txt
```
- **Configuration**: Set `OPENAI_API_KEY` in an `.env` file before running the app (see [Configuration](#configuration))

---

### Installation
 
- **Clone the repository**:
```bash
git clone https://github.com/LucaT445/NeuroLearn.git
cd NeuroLearn
```
- **Create and activate a virtual environment**:
    - Windows (PowerShell):
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
    - macOS/Linux:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
- Install all required packages with:
```bash
pip install -r dependencies.txt
```
- **Set environment variables**:
Create a `.env` file in the project root with:

```
OPENAI_API_KEY=your_api_key_here
```
- **(Optional) Verify installation**:
Run the test suite to confirm setup:
```bash
python -m pytest
```

---

### Usage

- **Start the application**:
```bash
python NeuroLearn_app.py
```
- **Access in browser**:

    Once the server starts, open [http://localhost:8050](http://localhost:8050) in your web browser.

- **Interacting with the app**:
    - **3D Model**: Rotate, zoom, and click regions to view functions, locations, and associated disorders. 
    - **AI Q&A**: Ask questions about brain topics beyond the 3D model (requires `OPENAI_API_KEY` set in `.env`).


---

### Configuration

NeuroLearn uses environment variables stored in a `.env` file located in the project root.
- `OPENAI_API_KEY` — required for the AI Q&A feature. This should contain your OpenAI API key.
You can create and manage API keys in your [OpenAI account dashboard](https://platform.openai.com/api-keys). 

Example `.env`:
```
OPENAI_API_KEY=your_api_key_here
```

---

### Testing

You can run the test suite to confirm that NeuroLearn is set up correctly:
```bash
python -m pytest
```
If you don't have pytest installed, install it with:
```bash
pip install pytest
```
If all tests pass, the installation and the configuration are complete. 

---

### License

This project is licensed under the [MIT License](LICENSE). 
