import json
from typing import Dict


class FileController:
    def __init__(self, filename: str = "exchanger.json"):
        self.filename = filename

    def write_file(self, data: Dict):
        with open(self.filename, "w") as file_obj:
            file_obj.write(json.dumps(data, indent=4))

    def read_file(self) -> Dict:
        with open(self.filename, "r") as file_obj:
            file_data = json.loads(file_obj.read())
        return file_data