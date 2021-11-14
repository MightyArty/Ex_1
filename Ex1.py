import json
import csv
import sys
import Building
import Calls
import Elevators


class Algo:

    def __init__(self, calls, building, out):
        self.calls = Calls(calls)
        self.building = Building(building)
        self.out = out

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

    def allocate(self):
        if self.calls.src < self.building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
            print("The floor does not exist :(")
        t = self.calls.time + self.timeTo(self, self.calls)  # 4.37 + (dest - src) --> from 0 to -1
        if self.calls.status != 0:
            if t > self.calls.time:  # t > actual time (t > 16.96)
                with open('out', 'w') as f:
                    writer = csv.writer(f)
                    # writer.writerow()  # need to write to the csv file at column 5

    if __name__ == '__main__':
        print("j")
