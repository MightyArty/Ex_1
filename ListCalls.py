import node


class ListCalls:
    # num- is the num of the elevators in the building
    # arr- representing the id's of the elevators
    def __init__(self, num, arr: list):
        self.array = []
        self.num = num
        for i in range(0, num):
            self.array.append(i)
            self.array[i] = node(arr[i])
