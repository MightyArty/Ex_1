import json
import csv

# f = open('B1.json', "r")
# data = json.loads(f.read())
# for i in data['_elevators']:
#     print(i)
# f.close()

with open('B1.json') as f:
    d = json.loads(f.read())
    for line in d['_elevators']:
        print(line)

with open('Calls_a.csv') as csv_file:
    data = csv.reader(csv_file.read())
    for i in data:
        print(i)

