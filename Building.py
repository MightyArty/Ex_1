import json
from Elevators import Elevators

"""
Building class
Which collect the data from given json file
"""


class Building:
    def __init__(self, data):
        with open(data, "r") as file:
            read = json.load(file)
            self._maxFloor = read["_maxFloor"]
            self._minFloor = read["_minFloor"]
            # pushing all the data representing elevator in each building
            # to the elevator array
            for i in read["_elevators"]:
                self.elevators.append(Elevators(i))
