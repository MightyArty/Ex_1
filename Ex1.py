import json
import csv
import sys
import Building
import Calls
from Elevators import Elevators
import node
import ListCalls


class Algo:

    def __init__(self, calls, building, out):
        self.calls = Calls(calls)
        self.building = Building(building)
        self.out = out
        self.Node = []
        self.arr = []
        i = 0
        for elev in building.elevArr:
            self.Node.append(node(elev[i].id))
            # self.arr.append(elev)
            i = i + 1
        self.list = ListCalls(building.id)

    # uploading the data to csv output file
    def saveToCSV(self, csv_file):
        name = 'out.csv'
        cList = []
        writer = csv.writer(csv_file)
        for line in csv_file:
            cList.append(line._dict_.values())
            with open(name, 'w', space='') as fp:
                writer.writerow(cList)

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
        return tempID

        # for i in self.building._elevators:
        #     if t > self.calls.time and self.isOn(self.Node.src,self.Node.dest,c.src) == True:  # t > actual time (t > 16.96)
        #         with open('out', 'w') as f:
        #             writer = csv.writer(f)
        #             # writer.writerow()  # need to write to the csv file at column 5
        # time = self.timeTo(c)
        # tempTime = 0
        # id = -1
        # for elev in self.building._elevators:
        #     if ()

    def isOn(self, a, b, c) -> bool:
        if (abs(c - a) + abs(b - a)) == abs(b - a):
            return True
        else:
            return False

    if __name__ == '__main__':
        print("j")
