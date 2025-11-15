import json

d = {"name": "shakshi", "age": 21}

print(json.dumps(d, indent=4))        # Pretty print JSON
print(json.dumps(d, sort_keys=True))  # Sorted keys
print(json.dumps(d, ensure_ascii=False))  # Non-ASCII encoding
print(json.dumps([{k: d[k]} for k in d]))  # Convert to JSON array format