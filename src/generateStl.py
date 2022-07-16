#!/bin/python3

import rrooms.rrooms as rms


if __name__ == "__main__":
    
    times = int(input("Number of random rooms:"))
    path = input("path to output-folder")
    numberOfObjects = int(input("Number of random objects:"))

    for x in range(times):
        room = rms.room(numberOfObjects)
        room.writeToStl(path,str(x).zfill(4)+ 'von'+str(times)+'_nO'+str(numberOfObjects))
