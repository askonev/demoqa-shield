import json
from typing import Dict


class FileHandler:
    def import_json(self, file_path: str) -> Dict:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                print("Data has been successfully imported:")
                return data
        except FileNotFoundError:
            print(f"Error: file '{file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: file '{file_path}' contains invalid JSON.")
