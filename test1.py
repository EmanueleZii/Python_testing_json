import json

# Read from file and parse JSON
with open("sample.json", "r") as f:
    data = json.load(f)

#print(data)
#print(type(data))


json_str = '{"name": "Francis", "age": 25, "city": "New York"}'
data = json.loads(json_str)

print(data)
print(type(data))