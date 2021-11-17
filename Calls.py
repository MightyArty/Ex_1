

class Calls:
    def __init__(self, time: float, src: int, dest: int, status: int, elevIndex: int):
        self.time = time
        self.src = src
        self.dest = dest
        self.status = status
        self.elevIndex = elevIndex
        self.state = 0

    # checking if the call has been completed
    def finalStatus(self):
        if self.elevIndex != -1:
            return True
        else:
            return False

    def __str__(self):
        return f'income time {self.time}, src {self.src}, dest {self.dest},' \
               f'status {self.status}  and the index {self.elevIndex}'

    def __repr__(self):
        return f'income time ({self.time}), src ({self.src}), dest ({self.dest}),' \
               f'status ({self.status}) and the index ({self.elevIndex})'
