from pathlib import Path
from utils import read_words_from_file
from generator import generate_sentence

BASE_DIR = Path(__file__).resolve().parent

def main():
    subjects_path = BASE_DIR / "data" / "subjects.txt"
    verbs_path = BASE_DIR / "data" / "verbs.txt"
    complements_path = BASE_DIR / "data" / "complements.txt"


    subjects = read_words_from_file(subjects_path)
    verbs = read_words_from_file(verbs_path)
    complements = read_words_from_file(complements_path)

    files = {
        "subjects.txt": subjects,
        "verbs.txt": verbs,
        "complements.txt": complements
    }

    for filename, data in files.items():
        if data is None:
            print(f"No se pudo leer {filename}.")
            return
        
        if not data:
            print(f"{filename} esta vacío.")
            return
    
    setence = generate_sentence(subjects, verbs, complements)
    print(setence)

if __name__ == "__main__":
    main()
