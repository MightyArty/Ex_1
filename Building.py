import json
from Elevators import Elevators


class Building:
    def __init__(self, data):
        self.elevArr = []
        with open(data, "r") as json_file:
            read = json.load(json_file)
            self._maxFloor = read["_maxFloor"]
            self._minFloor = read["_minFloor"]
            file = read["_elevators"]
            for i in file:
                temp = Elevators(i["_id"], i["_speed"], i["_minFloor"], i["_maxFloor"], i["_closeTime"],
                                 i["_openTime"], i["_startTime"], i["_stopTime"])
                self.elevArr.append(temp)
