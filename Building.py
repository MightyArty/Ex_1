import json
from Elevators import Elevators


class Building:
    def __init__(self, data):
        data=input("Enter the file name")
        open(data,"r")
        self._maxFloor = int(data["_maxFloor"])
        self._minFloor = int(data["_minFloor"])

