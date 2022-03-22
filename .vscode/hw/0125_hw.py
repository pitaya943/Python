# coding:utf-8
import sys
from queue import Queue


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


step = [[0]*10 for i in range(10)]
# Queue for temp direction8

queueOfTrack = Queue()
# Begin with (1, 1)
queueOfTrack.put((1, 1))
maze[1][1] = 1
# Number of footstep
step[1][1] = 1

destinationX = int(input('choose your destination: \nX -> '))
destinationY = int(input('Y -> '))
destination = (destinationX, destinationY)


def direction(nextX, nextY):
    queueOfTrack.put((nextX, nextY))
    maze[nextX][nextY] = 1


def Go(locationNow):
    locationX = locationNow[0]
    locationY = locationNow[1]

    # Up
    if maze[locationX-1][locationY] == 0:
        direction(locationX - 1, locationY)
        step[locationX -
             1][locationY] = step[locationX][locationY] + 1
    # Down
    if maze[locationX+1][locationY] == 0:
        direction(locationX + 1, locationY)
        step[locationX +
             1][locationY] = step[locationX][locationY] + 1
    # Left
    if maze[locationX][locationY-1] == 0:
        direction(locationX, locationY - 1)
        step[locationX][locationY -
                        1] = step[locationX][locationY] + 1
    # Right
    if maze[locationX][locationY+1] == 0:
        direction(locationX, locationY + 1)
        step[locationX][locationY +
                        1] = step[locationX][locationY] + 1


while not queueOfTrack.empty():
    location = queueOfTrack.get()
    if location == destination:
        print('到達終點:', location)
        break
    Go(location)


print('最短路徑: ', step[destinationX][destinationY], '步')
print('------------------Maze-----------------')
for mazeOfIndex in maze:
    print(mazeOfIndex)
print('---------------Formatted---------------')

for i in maze:
    print("{0}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}".format(
        i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
print('------------------Len------------------')

for i in range(len(step)):
    print(step[i])
print('---------------Formatted---------------')

for i in step:
    print("{0}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}".format(
        i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
