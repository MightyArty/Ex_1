import json
import csv
import sys
import Building
import Calls
from Elevators import Elevators
import node


class Algo:

    def __init__(self, calls, building, out):
        self.calls = Calls(calls)
        self.building = Building(building)
        self.out = out
        self.Node = []
        self.arr=[]
        for elev in Building.Elevators:
            self.Node.append(node(Building.Elevators.id))  # need to add the real id
            self.arr[elev].append(building._elevators.)
        self.list=ListCalls(buil)

    # uploading the data to csv output file
    def saveToCSV(self, csv_file):
        name = 'out.csv'
        cList = []
        writer = csv.writer(csv_file)
        for line in csv_file:
            cList.append(line._dict_.values())
            with open(name, 'w', space='') as fp:
                writer.writerow(cList)

    def timeTo(self, call):
        fromTo = abs(call.src - self._currentFloor) + abs(call.dest - call.src)
        result = self._closeTime + self._startTime + (fromTo / self._speed) + self._stopTime + self._openTime
        return result

    def timeTo(self, call, elev):
        elev=self.building._elevators[]

    def allocate(self, c):
        if self.calls.src < self.building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
            print("The floor does not exist :(")
        tempTime = float('inf')
        tempID= -1
        for elev in range(len(self.building._elevators)):
            time = self.calls.time + self.timeTo(c, elev)  # 4.37 + (dest - src) --> from 0 to -1
            if tempTime > time:
                tempTime = time
                tempID = elev
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
