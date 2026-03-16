from flask import Flask, render_template
from generator import generate_story
from utils import read_json
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
words_path = BASE_DIR / "data" / "words.json"
words_data = read_json(words_path)

@app.route("/")
def home():
    return render_template('index.html',)


@app.route("/story")
def story():
    if words_data is None:
        print("No se pudieron cargar los datos.")
        return
    
    story = generate_story(words_data)

    return render_template("story.html", story=story)

if __name__ == '__main__':
    app.run(debug=True)