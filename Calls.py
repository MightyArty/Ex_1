"""
This is the calls method class
"""
import csv


class Calls:
    def __init__(self, data):
        self.name = data[0]
        self.time = data[1]
        self.src = data[2]
        self.dst = data[3]
        self.status = data[4]
        self.elv = data[5]


class CallsList:
    def __init__(self, data):
        with open(data) as file:
            read = csv.reader(file)
            self.Calls = []
            for line in read:
                self.Calls.append(str(line[0]))  # name
                self.Calls.append(float(line[1]))  # time
                self.Calls.append(int(line[2]))  # src
                self.Calls.append(int(line[3]))  # dest
                self.Calls.append(int(line[4]))  # status
                self.Calls.append(int(line[5]))  # elevator index
