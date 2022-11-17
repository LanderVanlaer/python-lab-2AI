# Create a program that reads the JSON file ‘out.json’ from previous assignments and writes the
# sorted keys to a CSV file ‘keys.csv’.
import csv
import json

with open('out.json', 'r') as fin, open('keys.csv', 'w', newline='') as out:
    data = json.load(fin)
    keys = list(data.keys())

    keys.sort()

    csv_writer = csv.writer(out, delimiter=',')
    csv_writer.writerow(keys)
