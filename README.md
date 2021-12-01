![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MightyArty/Ex_1?style=plastic) ![GitHub contributors](https://img.shields.io/github/contributors/MightyArty/Ex_1?style=plastic)
# This is an off-line Elevator algorithm in python
2'nd project in OOP course at Ariel Univeristy using python.
This project represnt an off-line smart Elevator system.
Given a list of Calls as a csv files, and a json files that represent the Building structer (amount of floors,amount of elevators) we are creating a calculation and allocating the best elevator for each call.
# The problem we are dealing with :
Nowadays, we have a large buildings with a lot of floors and elevators. The main problem is to allocate the best and fastest elevator for each call.
In our alogirthm we are trying to solve this problem, by dividing the main problems into sub - problems. If the elevator are in the source floor so that elevator would pick up the given call from the source floor. If the elevator is in the range of the source floor and the destination floor - we would send this elevator to the source floor to proceed the call (if we don't have already a more close elevator for this particular call).
If the elevator is out of the range and we don't have any elevator that are closer to the source floor, we will calculate the time that takes the elevator arive to the source floor + the time taking to arrive to destination floor.
# Elevator class :
Represent the elevator functions (speed,close and open time of the doors).
# Calls class :
Represent the calls functions (the time, source, destination of each call).
# Building class :
Represent the building functions (amount of floors, amount of elevators).
# Node class :
The node class help us to store the source, destination and time of each call. So we could access the needed data in the Elevator array.
# Ex_1 (algo class) :
This class represent the reading from given csv files, json files and writing into a new csv 'out' file.
Also the actual algorithm of the calculation and aloocation of the best elevator for each call. And by that we providing the best waiting time for each person on every floor at the building.
# GUI class :
This class represent the GUI running simulator for the Elevator system. Enjoy it :)
# The UML diagram of out algorithm :
![WhatsApp Image 2021-11-18 at 16 47 58](https://user-images.githubusercontent.com/77808208/142437901-77f52ac5-9d41-465d-a11b-0053dbe010c8.jpeg)
# Video simulation GUI of our project :
[![CLICK HERE](https://img.youtube.com/vi/HGhyFRUDFwA/mqdefault.jpg)](https://www.youtube.com/watch?v=HGhyFRUDFwA "CLICK HERE")
<br />
<br />In this video we can see case B5.json and Calls_d.csv.
<br />Red full dot means new call invokes (correlated with the source floor) ,the dot becomes empty in the moment the elevator reached his destination.
<br />The green dots works the same but for destinations, when call invokes green full dot appears in the destination floor
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MightyArty/Ex_1?style=plastic) ![GitHub contributors](https://img.shields.io/github/contributors/MightyArty/Ex_1?style=plastic)
# This is an off-line Elevator algorithm in python
2'nd project in OOP course at Ariel Univeristy using python.
This project represnt an off-line smart Elevator system.
Given a list of Calls as a csv files, and a json files that represent the Building structer (amount of floors,amount of elevators) we are creating a calculation and allocating the best elevator for each call.
# The problem we are dealing with :
Nowadays, we have a large buildings with a lot of floors and elevators. The main problem is to allocate the best and fastest elevator for each call.
In our alogirthm we are trying to solve this problem, by dividing the main problems into sub - problems. If the elevator are in the source floor so that elevator would pick up the given call from the source floor. If the elevator is in the range of the source floor and the destination floor - we would send this elevator to the source floor to proceed the call (if we don't have already a more close elevator for this particular call).
If the elevator is out of the range and we don't have any elevator that are closer to the source floor, we will calculate the time that takes the elevator arive to the source floor + the time taking to arrive to destination floor.
# Elevator class :
Represent the elevator functions (speed,close and open time of the doors).
# Calls class :
Represent the calls functions (the time, source, destination of each call).
# Building class :
Represent the building functions (amount of floors, amount of elevators).
# Node class :
The node class help us to store the source, destination and time of each call. So we could access the needed data in the Elevator array.
# Ex_1 (algo class) :
This class represent the reading from given csv files, json files and writing into a new csv 'out' file.
Also the actual algorithm of the calculation and aloocation of the best elevator for each call. And by that we providing the best waiting time for each person on every floor at the building.
# GUI class :
This class represent the GUI running simulator for the Elevator system. Enjoy it :)
# The UML diagram of out algorithm :
![WhatsApp Image 2021-11-18 at 16 47 58](https://user-images.githubusercontent.com/77808208/142437901-77f52ac5-9d41-465d-a11b-0053dbe010c8.jpeg)
# Video simulation GUI of our project :
[![CLICK HERE](https://img.youtube.com/vi/HGhyFRUDFwA/mqdefault.jpg)](https://www.youtube.com/watch?v=HGhyFRUDFwA "CLICK HERE")
<br />
<br />In this video we can see case B5.json and Calls_d.csv.
<br />Red full dot means new call invokes (correlated with the source floor) ,the dot becomes empty in the moment the elevator reached his destination.
<br />The green dots works the same but for destinations, when call invokes green full dot appears in the destination floor


