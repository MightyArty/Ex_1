import json
from Elevators import Elevators


class Building:
    def __init__(self, name):
        with open(name, "r") as f:
            data = json.load(f)
            self._maxFloor = data["_maxFloor"]
            self._minFloor = data["_minFloor"]
            self.elevators = []
            for i in data["_elevators"]:
                self.elevators.append(Elevators(i))
