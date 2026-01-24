class DataManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def load_data(self):
        import csv
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            self.data = list(reader)
        return self.data

    def get_summary(self):
        return f"Loaded {len(self.data)} records from {self.filename}"

    def filter_by(self, key, value):
        return [item for item in self.data if item.get(key) == value]
