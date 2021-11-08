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
