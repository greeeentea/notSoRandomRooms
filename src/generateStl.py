#!/bin/python3

import rcubes.rcubes as rc


if __name__ == "__main__":
    cube = rc.cube(20)
    
    
    cube.writeToStl('cubetest')
