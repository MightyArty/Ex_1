import csv


class Calls:
    def __init__(self, time: float = 0, src: int = 0, dest: int = 0, status: int = 0, index: int = -1):
        self.time = time
        self.src = src
        self.dest = dest
        self.status = status
        self.index = index

    def callList(self, csv_file):
        with open(csv_file) as f:
            read = csv.reader(f)
            temp = []
            for line in read:
                # only for time, src and dest
                arr = Calls(line[1], line[2], line[3])
                temp.append(arr)
