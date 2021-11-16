import json
from Elevators import Elevators


def loadFromJSON(json_file):
    try:
        with open(json_file, 'r') as fp:
            data = json.load(fp)
            elevators = data["_elevators"]

            elevList = []
            for line in elevators:
                el = Elevators(line["_id"], line["_speed"], line["_minFloor"],
                               line["_maxFloor"], line["_closeTime"], line["_openTime"],
                               line["_startTime"], line["_stopTime"])
                elevList.append(el)
            listLen = len(elevList)
            return elevList
    except IOError as e:
        print(e)


class Building:
    def __init__(self, _elevators, _minFloor, _maxFloor):
        self._elevators = _elevators
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor

    def __str__(self):
        return f"The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} "

    def __repr__(self):
        return f"The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} "


if __name__ == '__main__':
    b1 = loadFromJSON("B1.json")
    print(b1)
