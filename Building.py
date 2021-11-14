class Building:
    def __init__(self, _elevators: list, _minFloor: int = 0, _maxFloor: int = 0):
        self._elevators = _elevators
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor

    def __str__(self):
        return f'The minimum floor is {self._minFloor} , the maximum floor is {self._maxFloor} ' \
               f'and the elevators data is {self._elevators}'

    def __repr__(self):
        return f'The minimum floor is ({self._minFloor}) , the maximum floor is ({self._maxFloor}) ' \
               f'and the elevators data is ({self._elevators})'
