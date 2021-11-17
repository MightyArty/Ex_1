import json
import csv
import sys
import subprocess
from Building import Building
from Calls import Calls
from Elevators import Elevators
import node


class Algo:

    def __init__(self, calls, building):
        self.calls = Calls(calls)
        self.building = Building(building)
        self.Node = []
        # self.arr = []
        for elev in self.building.elevArr:
            self.Node.append(node(elev.id))  # need to add the real id
        # self.arr[elev].append(building._elevators)

    def loadFromCSV(self, csv_file):
        callList = []
        with open(csv_file) as f:
            reader = csv.reader(f)
            for line in reader:
                callList.append(Calls(line))
        return callList

    def saveToCSV(self, csv_file):
        callList = []
        for line in csv_file:
            out = ["Elevator class", self.calls.time, self.calls.src, self.calls.dest, 0, self.calls.elevIndex]
            callList.append(out)
        with open(csv_file) as f:
            writer = csv.writer(f)
            writer.writerow(callList)

    def timeToDest(self, n, elev, c):
        fromTo = abs(n.src - n.dest)  # 1-2
        result = elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime
        result += self.timeToSrc(n, elev, c.src)
        return result

    def timeToSrc(self, n, elev, src):
        fromTo = abs(n.src - src)  # 0-0
        return elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime

    def writeToOut(self, csv_file):
        with open(csv_file):
            for line in csv_file:
                ans=self.allocate(line)
                line[5]=ans
                writer.writerow(line)


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
                time0 = c.time + self.timeToSrc(self.Node[i], elev, c.src)
                self.Node[i].src = c.src
                self.Node[i].dest = c.dest
                self.Node[i].time = time0
                tempID = elev.id
                return tempID
            elif self.isOn(self.Node[i].src, self.Node[i].dest, c.src):
                time = c.time + self.timeToSrc(self.Node[i], elev, c.src)  # 4.37 + (dest - src) --> from 0 to -1
                if time < tempTime:
                    tempTime = time
                    tempID = elev.id
                    index = i
            else:
                # checks which elev will come first to the call src floor
                time2 = c.time + self.timeToDest(self.Node[i], elev, c)
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

    def isOn(self, a, b, c) -> bool:
        if (abs(c - a) + abs(b - c)) == abs(b - a):
            return True
        else:
            return False

if __name__ == '__main__':
    b=Building()
    b.loadFromJson('B1.json')
    c=Calls('Calls_a.csv')
    algo = Algo(c,b)
