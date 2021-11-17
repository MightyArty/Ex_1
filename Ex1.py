import json
import csv
import sys
import subprocess
from Building import Building
from Calls import Calls
from Elevators import Elevators
import node


def saveToCSV(csv_file):
    callList = []
    for line in csv_file:
        out = Calls(line)
        # out = ["Elevator class", self.calls.time, self.calls.src, self.calls.dest, 0, self.calls.elevIndex]
        # callList.append(out)
    with open(csv_file) as f:
        writer = csv.writer(f)
        writer.writerow(callList)


def loadFromCSV(csv_file):
    callList = []
    with open(csv_file) as f:
        reader = csv.reader(f)
        for line in reader:
            callList.append(Calls(line))
    return callList


class Algo:

    def __init__(self, calls, building, out):
        self.calls = Calls(calls)
        self.building = Building(building)
        self.out = out
        self.Node = []
        self.arr = []
        for elev in Building.Elevators:
            self.Node.append(node(Building.Elevators.id))  # need to add the real id
            self.arr[elev].append(building.elevArr)

    def timeToDest(self, n, elev, c):
        fromTo = abs(n.src - n.dest)  # 1-2
        result = elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime
        result += self.timeToSrc(n, elev, c.src)
        return result

    def timeToSrc(self, n, elev, src):
        fromTo = abs(n.src - src)  # 0-0
        return elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime

    def allocate(self, c):
        if self.calls.src < self.building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
            print("The floor does not exist :(")
        tempTime = float('inf')
        tempID = -1
        i = 0
        index = 0
        for elev in self.building.elevArr:
            # checks whether the calls between the ranges
            if self.isOn(self.Node[i].src, self.Node[i].dest, c.src):
                time = c.time + self.timeToSrc(self.Node[i], elev, c.src)  # 4.37 + (dest - src) --> from 0 to -1
                if time < tempTime:
                    tempTime = time
                    tempID = elev[i].id
                    index = i
            else:
                # checks which elev will come first to the call src floor
                time2 = c.time + self.timeToDest(self.Node[i], elev, c)
                if time2 < tempTime:
                    tempTime = time2
                    tempID = elev[i].id
                    index = i
            i = i + 1
        # modify the nodes
        self.Node[index].src = c.src
        self.Node[index].dest = c.dest
        self.Node[index].time = c.time
        tempID = -1
        tempID = -1
        for elev in range(len(self.building._elevators)):
            time = self.calls.time + self.timeTo(c, elev)  # 4.37 + (dest - src) --> from 0 to -1
            if tempTime > time:
                tempTime = time
                tempID = elev
        return tempID

    def isOn(self, a, b, c) -> bool:
        if (abs(c - a) + abs(b - a)) == abs(b - a):
            return True
        else:
            return False


if __name__ == '__main__':
    load = loadFromCSV('Calls_a.csv')
    print(load)
