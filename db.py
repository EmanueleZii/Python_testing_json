import json

class JsonDB:
    def __init__(self, file_path):
        self.file_path = file_path

        try:
            with open(self.file_path, "r") as f:
                json.load(f)
        except:
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def read_all(self):
        """Legge tutti i dati dal file"""
        with open(self.file_path, "r") as f:
            return json.load(f)

    def write_all(self, data):
        """Scrive i dati nel file"""
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def insert(self, record):
        """Aggiunge un record"""
        data = self.read_all()
        data.append(record)
        self.write_all(data)

    def update(self, key, value, new_data):
        """Aggiorna il record che ha key == value"""
        data = self.read_all()
        for item in data:
            if item.get(key) == value:
                item.update(new_data)
        self.write_all(data)

    def query(self, key, value):
        """Cerca i record con key == value"""
        data = self.read_all()
        return [item for item in data if item.get(key) == value]
