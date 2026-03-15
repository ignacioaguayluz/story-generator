import json

def read_json(filepath):
    """
    Reads a JSON file and returns its content.

    Args:
        filepath (Path): Path to JSON file.

    Returns:
        dict | None
    """
    try:
      
      with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no fue encontrado.")
        return None

    except json.JSONDecodeError:
        print(f"Error: El archivo {filepath} no tiene formato JSON válido.")
        return None
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None