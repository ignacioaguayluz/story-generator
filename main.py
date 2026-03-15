from pathlib import Path
from utils import read_json
from generator import generate_sentence

BASE_DIR = Path(__file__).resolve().parent

def main():
    words_path = BASE_DIR / "data" / "words.json"
    words_data = read_json(words_path)

    if words_data is None:
        print("No se pudieron cargar los datos.")
        return
    
    sentence = generate_sentence(words_data)

    print(sentence)

if __name__ == "__main__":
    main()
