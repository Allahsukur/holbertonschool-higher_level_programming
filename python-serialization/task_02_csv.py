import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
