import json

class PythonObject:
    def __init__(self, data):
        self.data = data

class JsonAdapter:
    def __init__(self, python_object):
        self.python_object = python_object

    def to_json(self):
        return json.dumps(self.python_object.data)

# Usage
python_data = PythonObject({"key": "value"})
adapter = JsonAdapter(python_data)
print(adapter.to_json())  # {"key": "value"}
