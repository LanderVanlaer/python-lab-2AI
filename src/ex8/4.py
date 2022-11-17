# Write a program that reads the JSON file ‘out.json’ from the previous assignment and prints the
# value that belongs to ‘key2’.
import json

with open('out.json', 'r') as f:
    data = json.load(f)

    print(data.get("key2"))
