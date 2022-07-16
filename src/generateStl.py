#!/bin/python3

import rcubes.rcubes as rc


if __name__ == "__main__":
    numberOfObjects = 10
    roomSize = 10
    
    room = rc.room(numberOfObjects, roomSize)
    room.writeToStl('cubetest')
