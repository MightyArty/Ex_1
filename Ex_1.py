import sys
import csv
import json
from Calls import Calls
from Elevators import Elevators
from Building import Building
from node import node


##converting json to obj (elevator)
def loadFromJson(json_file):
    try:
        with open(json_file, 'r') as f:
            elevArr = []
            data = json.load(f)
            _minFloor = data["_minFloor"]
            _maxFloor = data["_maxFloor"]
            arr = data["_elevators"]
            for line in arr:
                el = Elevators(line["_id"], line["_speed"], line["_minFloor"],
                               line["_maxFloor"], line["_closeTime"], line["_openTime"],
                               line["_startTime"], line["_stopTime"])
                elevArr.append(el)
            # return self.elevArr
    except IOError as error:
        print(error)  ## js   ####c


def loadFromCSV(csv_file):
    """Converting csv file to an object """
    callList = []
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            c = Calls(name=str(line[0]), time=float(line[1]), src=int(line[2]), dest=int(line[3]),
                      status=int(line[4]), elevIndex=int(line[5]))
            callList.append(c)
    return callList


def saveToCSV(c, csv_file):
    """Save our output to the csv file """
    callList = []
    for line in c:
        callList.append(line.__dict__.values())
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(callList)


######               ALGO            ###########
Node = []
building = Building()
building.loadFromJson(sys.argv[1])
i = 0
for elev in building.elevArr:
    Node.append(node(building.elevArr[i].id))
    i = i + 1




def timeToDest(n, elev, c):
    """The function calculating time from src to dest """
    fromTo = abs(n.src - n.dest)  # 1-2
    result = elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime
    result += timeToSrc(n, elev, c.src)
    return result


def timeToSrc(n, elev, src):
    """The function that calculating timr from src to src """
    fromTo = abs(n.src - src)  # 0-0
    return elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime


def allocate(c):
    # if calls.src < building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
    #     print("The floor does not exist :(")
    tempTime = float('inf')
    tempID = -1
    i = 0
    index = 0
    for elev in building.elevArr:
        # checks whether the calls between the ranges
        if Node[i].dest == c.src:
            time0 = c.time + timeToSrc(Node[i], elev, c.src)
            Node[i].src = c.src
            Node[i].dest = c.dest
            Node[i].time = time0
            tempID = elev.id
            c.elevIndex = tempID
        #     return tempID
        elif isOn(Node[i].src, Node[i].dest, c.src):
            time = c.time + timeToSrc(Node[i], elev, c.src)  # 4.37 + (dest - src) --> from 0 to -1
            if time < tempTime:
                tempTime = time
                tempID = elev.id
                index = i
        else:
            # checks which elev will come first to the call src floor
            time2 = c.time + timeToDest(Node[i], elev, c)
            if time2 < tempTime:
                tempTime = time2
                tempID = elev.id
                index = i
        i = i + 1
    # modify the nodes
    Node[index].src = c.src
    Node[index].dest = c.dest
    Node[index].time = tempTime
    c.elevIndex = tempID
    # return tempID


def isOn(a, b, c):
    # """Check if the call is in the path of the elevator"""
    if (abs(c - a) + abs(b - c)) == abs(b - a):
        return True
    else:
        return False


if __name__ == '__main__':
    c1 = loadFromCSV(sys.argv[2])
    for c in c1:
        allocate(c)
        saveToCSV(c1, sys.argv[3])
