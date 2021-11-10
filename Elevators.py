class Elevators:
    def __init__(self, data):
        self.id = int(data["_id"])
        self.speed = int(data["_speed"])
        self.minFloor = int(data["_minFloor"])
        self.maxFloor = int(data["_maxFloor"])
        self.closeTime = int(data["_closeTime"])
        self.openTime = int(data["_openTime"])
        self.startTime = int(data["_startTime"])
        self.stopTime = int(data["_stopTime"])
