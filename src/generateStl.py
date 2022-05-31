#!/bin/python3

import rcubes.rcubes as rc


if __name__ == "__main__":
    cube = rc.cube()
    cube.randomScale()
    cube.randomMove()
    cube.randomRotate()
    cube.writeToStl('cube')
