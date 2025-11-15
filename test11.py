import json
from collections import namedtuple

# Custom decoder function
def customDecoder(geekDict):
    return namedtuple('X', geekDict.keys())(*geekDict.values())

# Sample JSON data
geekJsonData = '{"name": "GeekCustomDecoder", "id": 2, "location": "Pune"}'

# Use custom decoder to parse the JSON data
x = json.loads(geekJsonData, object_hook=customDecoder)

print(x.name, x.id, x.location)