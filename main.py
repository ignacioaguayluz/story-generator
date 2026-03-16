from pathlib import Path
from utils import read_json
from generator import generate_story

BASE_DIR = Path(__file__).resolve().parent

def main():
    words_path = BASE_DIR / "data" / "words.json"
    words_data = read_json(words_path)

    if words_data is None:
        print("No se pudieron cargar los datos.")
        return
    
    story = generate_story(words_data)

    for i in story:
        print(i)

if __name__ == "__main__":
    main()