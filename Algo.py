import Building
import Elevators
import json
import csv


class CallsList:
    def __init__(self, data):
        with open(data) as file:
            read = csv.reader(file)
            self.Calls = []
            for i in read:
                self.Calls.append(str(i[0]))  # name
                self.Calls.append(float(i[1]))  # time
                self.Calls.append(int(i[2]))  # src
                self.Calls.append(int(i[3]))  # dest
                self.Calls.append(int(i[4]))  # status
                self.Calls.append(int(i[5]))  # elevator index


class Algo:

