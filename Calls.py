"""
This is the calls method class
"""


class Calls:
    def __init__(self, src: int, dest: int, time: float):
        self.src = src
        self.dest = dest
        self.time = time

        #need to move from here !!!!
    # def __timeTo__(self):
    #     result = self.stopTime + self.startTime + self.openTime + self.closeTime + \
    #              self.speed * (abs(self.dest - self.src))
    #     return result
