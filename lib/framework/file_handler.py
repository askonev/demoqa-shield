import json
from typing import Dict


class FileHandler:
    def import_json(self, file_path: str) -> Dict:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print("Data has been successfully imported:")
            return data
