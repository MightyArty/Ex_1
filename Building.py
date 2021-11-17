import json
from Elevators import Elevators


class Building:

    def __init__(self):
        self._minFloor = -2
        self._maxFloor = 10
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

    def __str__(self):
        return f"The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} " \
               f"and the elevator data is : {self.elevArr} "

    def __repr__(self):
        return f"The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} " \
               f"and the elevator data is : {self.elevArr} "


if __name__ == '__main__':
    b = Building()
    b.loadFromJson("B2.json")
    print(b)
    print(b.elevArr[0].stopTime)
    print(b.elevArr[1].id)
    print(b.elevArr[0].speed)