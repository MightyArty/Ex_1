import sys
import csv
import json
from Calls import Calls
from Elevators import Elevators
from Building import Building
from node import node


# converting json to obj (elevator)
def loadFromJson(json_file):
    try:
        with open(json_file, 'r') as f:
            elevArr = []
            data = json.load(f)
            _minFloor = data["_minFloor"]
            _maxFloor = data["_maxFloor"]
            arr = data["_elevators"]
            for line in arr:
                el = Elevators(line["_id"], line["_speed"], line["_minFloor"],
                               line["_maxFloor"], line["_closeTime"], line["_openTime"],
                               line["_startTime"], line["_stopTime"])
                elevArr.append(el)
            # return self.elevArr
    except IOError as error:
        print(error)  ## js   ####c


def loadFromCSV(csv_file):
    """Converting csv file to an object """
    callList = []
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            c = Calls(name=str(line[0]), time=float(line[1]), src=int(line[2]), dest=int(line[3]),
                      status=int(line[4]), elevIndex=int(line[5]))
            callList.append(c)
    return callList


def saveToCSV(c, csv_file):
    """Save our output to the csv file """
    callList = []
    for line in c:
        callList.append(line.__dict__.values())
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(callList)


"""-------------------The actual algo-------------------"""
Node = []
building = Building()
building.loadFromJson(sys.argv[1])
i = 0
for elev in building.elevArr:
    Node.append(node(building.elevArr[i].id))
    i = i + 1


def timeToDest(n, elev, c):
    """The function calculating time from src to dest """
    fromTo = abs(n.src - n.dest)  # 1-2
    result = elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime
    result += timeToSrc(n, elev, c.src)
    return result


def timeToSrc(n, elev, src):
    """The function that calculating timr from src to src """
    fromTo = abs(n.src - src)  # 0-0
    return elev.closeTime + elev.startTime + (fromTo / elev.speed) + elev.stopTime + elev.openTime


def allocate(c):
    tempTime = float('inf')
    tempID = -1
    i = 0
    index = 0
    for elev in building.elevArr:
        if Node[i].dest == c.src:  # Elevator is already in position
            tempTime = max(Node[i].time, c.time) + elev.openTime
            tempID = elev.id
            index = i
            time_departure = tempTime
            time_arrival = time_departure + timeToDest(Node[i], elev, c)
            break

        elif isOn(Node[i].src, Node[i].dest, c.src):
            time = max(Node[i].time, c.time) + timeToSrc(Node[i], elev, c.src)  # 4.37 + (dest - src) --> from 0 to -1
            if time < tempTime:
                tempTime = time
                tempID = elev.id
                index = i
                time_departure = time
                time_arrival = time_departure + timeToDest(Node[i], elev, c)
        else:
            # checks which elev will come first to the call src floor
            time = max(Node[i].time, c.time) + timeToDest(Node[i], elev, c)
            if time < tempTime:
                tempTime = time
                tempID = elev.id
                index = i
                time_departure = time
                time_arrival = time_departure + timeToDest(Node[i], elev, c)
        i = i + 1
    # modify the nodes
    Node[index].src = c.src
    Node[index].dest = c.dest
    Node[index].time = time_arrival
    c.elevIndex = tempID
    c.time_departure = time_departure
    c.time_arrival = time_arrival


def isOn(a, b, c):
    # """Check if the call is in the path of the elevator"""
    if (abs(c - a) + abs(b - c)) == abs(b - a):
        return True
    else:
        return False


def simulationData(time, calls, building):
    """This function is the for running the elevator simulator via GUI"""
    calls_left = []
    calls_right = []
    for _ in building.getFloorRange():
        calls_left.append([0, 0])  # waiting, travelling
        calls_right.append([0, 0])  # arrived, travelling
    elevators = []
    for _ in building.elevArr:
        elevators.append([0, 0])  # src, dst

    max_time = 0
    total_wait_time = 0
    total_calls = 0

    for call in calls:
        if call.dest - building._minFloor >= len(calls_right):
            pass  # invalid call
        elif call.src - building._minFloor >= len(calls_left):
            pass  # invalid call
        elif call.time_arrival < time:  # call already arrived
            calls_right[call.dest - building._minFloor][0] += 1
            total_calls += 1
            total_wait_time += call.time_departure - call.time

        elif call.time_departure < time:  # call is in motion
            calls_right[call.dest - building._minFloor][1] += 1
            calls_left[call.src - building._minFloor][1] += 1
            elevators[call.elevIndex][0] = call.src
            elevators[call.elevIndex][1] = call.dest
            total_calls += 1
            total_wait_time += call.time_departure - call.time

        elif call.time < time:  # call is waiting
            calls_left[call.src - building._minFloor][0] += 1
            total_calls += 1
            total_wait_time += time - call.time

        else:  # elevator has not been called yet
            pass
        max_time = max(call.time_arrival, max_time)

        if total_calls != 0:
            avg_wait_time = total_wait_time / total_calls
        else:
            avg_wait_time = 0

        min_floor = building._minFloor

    return calls_left, calls_right, elevators, max_time, time, total_wait_time, avg_wait_time, min_floor


if __name__ == '__main__':
    calls = loadFromCSV(sys.argv[2])
    for c in calls:
        allocate(c)
        saveToCSV(calls, sys.argv[3])

        """GUI for the simulator"""
        import sys
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtCore import QTimer

        app = QApplication(sys.argv)

        dt = 100
        t = 0.
        multi = 100
        sim_data = simulationData(0, calls, building)


        def start():
            global t
            t = 0
            update_timer.start()


        def x1():
            global multi
            multi = 1


        def x5():
            global multi
            multi = 5


        def x100():
            global multi
            multi = 100


        def x1000():
            global multi
            multi = 1000


        def end():
            global t
            t = sim_data[3]


        w = gui()
        w.show()
        w.b_start.clicked.connect(start)
        w.b_x1.clicked.connect(x1)
        w.b_x5.clicked.connect(x5)
        w.b_x100.clicked.connect(x100)
        w.b_x1000.clicked.connect(x1000)
        w.b_end.clicked.connect(end)

        update_timer = QTimer()
        update_timer.setSingleShot(False)
        update_timer.setInterval(dt)


        def upd():
            global t
            global update_timer
            t += dt / 1000 * multi
            sim_data = simulationData(t, calls, building)
            w.setData(sim_data)
            w.l_status.setText(
                "Current time:    {:10.2f} s\n"
                "Current speed:             x{} \n"
                "Total wait time: {:10.2f} s\n"
                "Avg wait time:   {:10.2f} s\n".format(t, multi, sim_data[5], sim_data[6])
            )
            w.update()

            if sim_data[3] < t:
                update_timer.stop()


        update_timer.timeout.connect(upd)

        cleanup = app.exec()
        sys.exit(cleanup)
