import json

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
    print("File data =", data)
    
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file.")