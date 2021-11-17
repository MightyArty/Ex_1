import csv
import json
from Building import Building
from Calls import Calls
from Elevators import Elevators
from node import node
import sys


def timeToSrc(n, elev, src):
    fromTo = abs(n.src - src)  # 0-0
    return elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime


def timeToDest(n, elev, c):
    fromTo = abs(n.src - n.dest)  # 1-2
    result = elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime
    result += timeToSrc(n, elev, c.src)
    return result

    def isOn(self, a, b, c) -> bool:
        if (abs(c - a) + abs(b - c)) == abs(b - a):
            return True
        else:
            return False


def allocate(self, c):
    if self.calls.src < self.building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
        print("The floor does not exist :(")
    tempTime = float('inf')
    tempID = -1
    i = 0
    index = 0
    for elev in self.building.elevArr:
        # checks whether the calls between the ranges
        if self.Node[i].dest == c.src:
            time0 = c.time + timeToSrc(self.Node[i], elev, c.src)
            self.Node[i].src = c.src
            self.Node[i].dest = c.dest
            self.Node[i].time = time0
            tempID = elev.id
            return tempID
        elif self.isOn(self.Node[i].src, self.Node[i].dest, c.src):
            time = c.time + timeToSrc(self.Node[i], elev, c.src)  # 4.37 + (dest - src) --> from 0 to -1
            if time < tempTime:
                tempTime = time
                tempID = elev.id
                index = i
        else:
            # checks which elev will come first to the call src floor
            time2 = c.time + timeToDest(self.Node[i], elev, c)
            if time2 < tempTime:
                tempTime = time2
                tempID = elev.id
                index = i
            i = i + 1
        # modify the nodes
        self.Node[index].src = c.src
        self.Node[index].dest = c.dest
        self.Node[index].time = tempTime
        return tempID


arr = sys.argv
b = arr[1]
c = arr[2]
out = arr[3]

elev = []
calls = []

try:
    with open(b) as json_file:
        data = json_file.read()
    temp = json.load(data)
    minFloor = temp["_minFloor"]
    maxFloor = temp["_maxFloor"]
    link = data["_elevators"]
    for line in link:
        el = Elevators(line["_id"], line["_speed"], line["_minFloor"],
                       line["_maxFloor"], line["_closeTime"], line["_openTime"],
                       line["_startTime"], line["_stopTime"])
        elev.append(el)
except IOError as e:
    print(e)

try:
    with open(c) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            tempArr = Calls(line[1], line[2], line[3], line[4])
            calls.append(tempArr)
except IOError as err:
    print(err)

for k in calls:
    allocate(k)

finalResult = []
for line in calls:
    tempo = ["Elevator call", k.time, k.src, k.dest, 0, k.elevIndex]
    finalResult.append(tempo)

# finally writing the right index to the csv output file
with open(out, 'w', newline="") as final:
    writer = csv.writer(final)
    writer.writerows(finalResult)


