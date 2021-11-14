import csv


def loadFromCSV(csv_file):
    with open(csv_file, 'r') as f:
        read = csv.reader(f)
        temp = []
        for line in read:
            temp.append(Calls(line))
        return temp


class Calls:
    def __init__(self, time: float = 0, src: int = 0, dest: int = 0, status: int = 0, index: int = -1):
        self.time = time
        self.src = src
        self.dest = dest
        self.status = status
        self.index = index

    def __str__(self):
        return f'income time {self.time}, src {self.src}, dest {self.dest},' \
               f'status {self.status} and the index {self.index}'

    def __repr__(self):
        return f'income time ({self.time}), src ({self.src}), dest ({self.dest}),' \
               f'status ({self.status}) and the index ({self.index})'
