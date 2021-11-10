import json
from Elevators import Elevators


class Building:
    def __init__(self, data):
            self._maxFloor = int(data["_maxFloor"])
            self._minFloor = int(data["_minFloor"])
            self.elevators = []
            self.size = len(data["_elevators"])
            for i in data["_elevators"]:
                self.elevators.append(Elevators(i))


