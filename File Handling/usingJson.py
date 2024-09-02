import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
data = {"name": "Alice", "age": 30}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
