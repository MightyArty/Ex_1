"""
This is the calls method class
"""


class Calls:
    def __init__(self, data):
        self.time = data[1]
        self.src = data[2]
        self.dst = data[3]
        self.status = data[4]
        self.elv = data[5]

