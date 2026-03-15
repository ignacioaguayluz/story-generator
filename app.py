from flask import Flask, render_template
from generator import generate_sentence
from utils import read_json
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

@app.route("/")
def home():
    return render_template('index.html',)


@app.route("/story")
def story():
    words_path = BASE_DIR / "data" / "words.json"
    words_data = read_json(words_path)

    if words_data is None:
        print("No se pudieron cargar los datos.")
        return
    
    sentence = generate_sentence(words_data)

    return render_template("story.html", sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)