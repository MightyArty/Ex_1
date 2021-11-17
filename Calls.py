import csv


class Calls:
    def __init__(self, csv_file):
        self.string = csv_file[0]  # Elevator call
        self.time = csv_file[1]
        self.src = csv_file[2]
        self.dest = csv_file[3]
        self.status = csv_file[4]
        self.elevIndex = csv_file[5]
        self.state = 0
        if self.dest > self.src:
            self.state = 1
        else:
            self.state = -1

    # checking if the call has been completed
    def finalStatus(self):
        if self.elevIndex != -1:
            return True
        else:
            return False

    def __str__(self):
        return f'income time: {self.time}, src: {self.src}, dest: {self.dest},' \
               f'status: {self.status} and the index {self.index}'

    def __repr__(self):
        return f'income time: {self.time}, src: {self.src}, dest: {self.dest},'\
               f'status {self.status} and the index {self.elevIndex}'


if __name__ == '__main__':
    with open('Calls_a.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)
