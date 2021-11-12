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
            for line in file:
                temp = Elevators(line["_id"], line["_speed"], line["_minFloor"], line["_maxFloor"], line["_closeTime"],
                                 line["_openTime"], line["_startTime"], line["_stopTime"])
                self.elevArr.append(temp)
