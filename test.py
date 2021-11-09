# file_name = "./test.txt"
# f = open(file_name, "w")
# f.write("david is gay")
# f.close()

import json
with open('B2.json') as f:
    data = json.load(f)
    #min floor
    print(data["_elevators"][0]["_minFloor"])
    #max floor
    print(data["_elevators"][0]["_maxFloor"])

person_dict = {"name": "David", "age": "2"}
person_json = json.dumps(person_dict)
print(person_json)

# saving the text data
data_json = json.dumps(data)
print(data_json)
