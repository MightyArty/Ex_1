import json
import csv

import Building
from Calls import CallsList


def __init__(self, calls, building, out):
    self.callList = CallsList(calls)
    self.out = out
    self.building = Building(building)


def timeTo(self, call):
    fromTo = abs(call.src - self._currentFloor) + abs(call.dest - call.src)
    result = self._closeTime + self._startTime + (fromTo / self._speed) + self._stopTime + self._openTime
    return result

# if __name__ == '__main__':
#     with open("Ex1_Calls/Calls_a.csv") as file:
#         reader = csv.reader(file)
#         for i in reader:
#             print(i)
