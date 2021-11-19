import json
import sys

from Elevators import Elevators

'''
Building class
Creating a python object from the given json file which representing the main Building
in each run
'''


class Building:

    def __init__(self):
        self._minFloor = 0
        self._maxFloor = 0
        self.elevArr = []

    def loadFromJson(self, json_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                self._minFloor = data["_minFloor"]
                self._maxFloor = data["_maxFloor"]
                arr = data["_elevators"]
                for line in arr:
                    el = Elevators(line["_id"], line["_speed"], line["_minFloor"],
                                   line["_maxFloor"], line["_closeTime"], line["_openTime"],
                                   line["_startTime"], line["_stopTime"])
                    self.elevArr.append(el)
                # return self.elevArr
        except IOError as error:
            print(error)

    # returning the specified index in the elevator arr which we created in the constructor
    def getElevIndex(self, index):
        return self.elevArr[index]

    def getFloorRange(self):
        return range(self._minFloor, self._maxFloor +1)

    def __str__(self):
        return f"The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} " \
               f"and the elevator data is : {self.elevArr} "

    def __repr__(self):
        return f"The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} " \
               f"and the elevator data is : {self.elevArr} "


if __name__ == '__main__':
    b = Building()
    b.loadFromJson(sys.argv[1])
    print(b)

