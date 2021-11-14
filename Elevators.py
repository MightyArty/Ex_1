class Elevators:

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime

    def __str__(self):
        return f'id {self.id}, speed {self.speed}, minFloor {self.minFloor},' \
               f'maxFloor {self.maxFloor}, closeTime {self.closeTime}, openTime {self.openTime},' \
               f'startTime {self.startTime}, stopTime {self.stopTime}'

    def __repr__(self):
        return f'id: {self.id}, speed: {self.speed}, minFloor: {self.minFloor}, ' \
               f'maxFloor: {self.maxFloor}, closeTime: {self.closeTime}, openTime: {self.openTime}, ' \
               f'startTime: {self.startTime}, stopTime: {self.stopTime}'