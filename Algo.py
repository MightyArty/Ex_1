import Building
import Elevators
import Calls
import json
import math as m


class Algo:

    def __init__(self,building,numOfElev):
        self.building=Building('B5.json',"r")
        self.numOfElev=building.size


    def __timeTodest__(self, call, elevator):
        floorsTime = m.abs(call.dest - call.src) / elevator.speed
        return floorsTime + elevator.minFloor + elevator.maxFloor + elevator.closeTime + elevator.openTime

    def allocate(self,call):
        num=self.numOfElev
        if(num<1):return None
        elif num==1:
            return 0
            if(num>1):



    def range(self,data):
