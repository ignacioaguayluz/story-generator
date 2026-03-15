# 📖 Story Generator

A small **Python story generator** that evolves from a simple random sentence generator into a more advanced **probabilistic text generator with a web interface**.

This project was created as a **learning exercise in software engineering, Python architecture, and backend development**.

---

# 🚀 Current Version

**v2.5**

Features implemented so far:

* Modular Python architecture
* JSON-based word datasets
* Weighted random word selection
* Multiple sentence templates
* CLI interface
* Web interface built with Flask

---

# 🎯 Project Goals

The objective of this project is to progressively explore concepts such as:

* modular software design
* separation of responsibilities
* data-driven text generation
* probabilistic systems
* backend web development
* foundations for natural language processing

The project is designed to evolve through multiple versions.

---

# 🏗 Project Structure

```
story-generator/

app.py
main.py

generator.py
utils.py

data/
    words.json

templates/
    index.html
    story.html
```

---

# 🧠 Architecture

The project separates the **generation engine** from the **interfaces**.

```
generator.py (story engine)
        ↑
utils.py (data utilities)
        ↑
 ┌─────────────┬─────────────┐
 main.py       app.py
  CLI          Flask Web App
```

### `generator.py`

Core generation engine.

Responsibilities:

* selecting words
* applying probability weights
* choosing templates
* building the final sentence

Example output:

```
One day, the programmer optimized the code.
```

---

### `utils.py`

Utility functions.

Currently responsible for:

* reading JSON files
* basic error handling

---

### `main.py`

Command-line interface.

Run the generator from the terminal:

```
python main.py
```

Useful for:

* testing
* debugging
* quick generation without the web interface

---

### `app.py`

Flask web application.

Allows users to generate stories from the browser.

Flow:

```
User opens page
↓
Flask receives request
↓
JSON is loaded
↓
generate_sentence()
↓
HTML template rendered
```

---

# 🌐 Web Interface

The project includes a simple frontend using **Flask templates**.

### `index.html`

Main page with a button to generate a story.

### `story.html`

Displays the generated story.

Example output:

```
The robot discovered a magical key.
```

---

# 📊 Concepts Practiced

## Python

* functions
* dictionaries
* JSON parsing
* modular programming
* error handling

---

## Software Engineering

* separation of layers
* reusable logic
* modular architecture

---

## Backend Development

Using Flask:

* routing
* templates
* Jinja2 variables
* backend → frontend interaction

---

# 🗺 Roadmap

## ✅ V1 — Basic Generator

* words stored in `.txt`
* random selection
* modular structure
* CLI execution

Example:

```
The robot discovered the city.
```

---

## ✅ V2 — Probabilistic Generator + Flask

Improvements:

* JSON-based dataset
* weighted random selection
* multiple sentence templates
* web interface with Flask

---

# 📦 Versioning

Current version:

```
v2.5
```

Version meaning:

* V1 → basic generator
* V2 → probabilistic generator + Flask
* **V2.5 → project stabilization and documentation**

---

# 📚 Future Improvements

Planned improvements include:

* multi-sentence story generation
* story genres
* Markov chain based generation
* improved UI
* dataset expansion

---

# 👨‍💻 Author

Created as a learning project in:

* Python
* software engineering
* backend development
* text generation systems
