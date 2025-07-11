import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads a JSON file and returns the deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
