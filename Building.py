import json
from Elevators import Elevators


class Building:
    def __init__(self, data):
        with open(data, "r") as json_file:
            read = json.load(json_file)
            self._maxFloor = read["_maxFloor"]
            self._minFloor = read["_minFloor"]
            # pushing all the data representing elevator in each building
            # to the elevator array
            self.elevArr = []
            for line in read["_elevators"]:
                self.elevArr.append(Elevators[line])
