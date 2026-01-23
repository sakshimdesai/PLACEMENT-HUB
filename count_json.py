import json

with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total questions:", len(data))
