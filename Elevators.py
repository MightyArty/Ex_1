class Elevators:
    def __init__(self, data):
        self.id = float(data["_id"])
        self.speed = float(data["_speed"])
        self.minFloor = int(data["_minFloor"])
        self.maxFloor = int(data["_maxFloor"])
        self.closeTime = float(data["_closeTime"])
        self.openTime = float(data["_openTime"])
        self.startTime = float(data["_startTime"])
        self.stopTime = float(data["_stopTime"])
