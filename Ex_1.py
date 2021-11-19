import sys
import csv
import json
from Calls import Calls
from Elevators import Elevators
from Building import Building
from node import node


# converting json to obj (elevator)
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


"""-------------------The actual algo-------------------"""
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
    tempTime = float('inf')
    tempID = -1
    i = 0
    index = 0
    for elev in building.elevArr:
        if Node[i].dest == c.src: #Elevator is already in position
            tempTime = max(Node[i].time,c.time) + elev.openTime
            tempID = elev.id
            index = i
            time_departure = tempTime
            time_arrival = time_departure + timeToDest(Node[i], elev, c)
            break

        elif isOn(Node[i].src, Node[i].dest, c.src):
            time = max(Node[i].time,c.time) + timeToSrc(Node[i], elev, c.src)  # 4.37 + (dest - src) --> from 0 to -1
            if time < tempTime:
                tempTime = time
                tempID = elev.id
                index = i
                time_departure = time
                time_arrival = time_departure + timeToDest(Node[i], elev, c)
        else:
            # checks which elev will come first to the call src floor
            time = max(Node[i].time,c.time) + timeToDest(Node[i], elev, c)
            if time < tempTime:
                tempTime = time
                tempID = elev.id
                index = i
                time_departure = time
                time_arrival = time_departure + timeToDest(Node[i], elev, c)
        i = i + 1
    # modify the nodes
    Node[index].src = c.src
    Node[index].dest = c.dest
    Node[index].time = time_arrival
    c.elevIndex = tempID
    c.time_departure = time_departure
    c.time_arrival = time_arrival


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
