def read_words_from_file(filepath):
    """
    Reads a text file and returns a list of non-empty lines.

    Args:
        filepath (str): Path to the text file.

    Returns:
        list: A list of cleaned strings or None if an erorr occurs.
    """

    try:
       words = []
       with open(filepath, 'r', encoding='utf-8') as document:
        for line in document:
           cleaned_line = line.strip()
           if cleaned_line:
              words.append(cleaned_line)
        return words

    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no fue encontrado.")
        return None
    
    except Exception as e:
      print(f"Ocurrio un error inesperado {e}")
      return None