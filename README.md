# Story Generator 📝

A simple modular Python project that generates random sentences using word lists stored in text files.

## 🚀 Features

- Reads subjects, verbs, and complements from external `.txt` files
- Cleans and validates file input
- Generates grammatically structured random sentences
- Modular architecture (separation of concerns)
- Error handling for missing or empty files

## 📂 Project Structure

story-generator/
│
├── main.py
├── generator.py
├── utils.py
├── data/
│   ├── subjects.txt
│   ├── verbs.txt
│   └── complements.txt
└── README.md

## ▶️ How to Run

Make sure you are inside the project directory:

```bash
cd story-generator
python main.py
