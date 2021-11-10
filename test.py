# file_name = "./test.txt"
# f = open(file_name, "w")
# f.write("david is gay")
# f.close()

import json
import Building

f = open('B5.json', "r")
data = json.loads(f.read())
# for i in data['_elevators']:
#     print(i)

b = Building(data)
print(b.size)
f.close()


