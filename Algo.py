import json
import csv
import sys

import Building
import Calls
import Elevators


def __init__(self, calls, building, out):
    self.loadFromCSV = Calls(calls)
    self.out = out
    self.building = Building(building)


def loadFromCSV(self, csv_file):
    with open(csv_file, 'r') as f:
        read = csv.reader(f)
        temp = []
        for line in read:
            # only for time, src and dest
            arr = Calls(line[1], line[2], line[3])
            temp.append(arr)


def loadFromJSON(self, json_file):
    try:
        with open(json_file, 'r') as fp:
            temp = {}
            data = json.load(fp)
            elevators = data["_elevators"]
            for line in elevators.items():
                b = Building(_id=line["_id"], _speed=line["_speed"], _minFloor=line["_minFloor"],
                             _maxFloor=line["_maxFloor"], _closeTime=line["_closeTime"], _openTime=line["_openTime"],
                             _startTime=line["_startTime"], _stopTime=line["_stopTime"])
                temp = b
            self.building = temp
    except IOError as e:
        print(e)


def timeTo(self, call):
    fromTo = abs(call.src - self._currentFloor) + abs(call.dest - call.src)
    result = self._closeTime + self._startTime + (fromTo / self._speed) + self._stopTime + self._openTime
    return result


def allocate(self):
    if self.calls.src < self.building._minFloor or self.calls.src > self.building._maxFloor or self.calls.dest < self.building._minFloor or self.calls.dest > self.building._maxFloor:
        print("The floor does not exist :(")
    t = self.calls.time + timeTo(self, self.calls)  # 4.37 + (dest - src) --> from 0 to -1
    if self.calls.status != 0:
        if t > self.calls.time:  # t > actual time (t > 16.96)
            with open('out', 'w') as f:
                writer = csv.writer(f)
                # writer.writerow()  # need to write to the csv file at column 5


# if __name__ == '__main__':
#     print(sys.argv[1])
