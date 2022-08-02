#!/bin/python3
import argparse
import rrooms.rrooms as rms


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generates r stl-files with o random objects in it. ",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-r", "--rooms",  help="the number of rooms", required=True, type=int)
    parser.add_argument(
        "-p", "--path",  help="the path for stl-files", required=True)
    parser.add_argument("-o", "--objects",
                        help="the number of objects", required=True, type=int)
    parser.add_argument("-rs", "--roomsize",
                        help="size of the room", type=int)
    config = vars(parser.parse_args())

    print("~ Creating "+str(config['rooms']) +
          " rooms with " + str(config['objects']) + " objects in " + config['path'] + ". ~")

    for x in range(config['rooms']):
        room = rms.room(config['objects'], config['roomsize'])
        room.writeToStl(config['path'], 'n'+str(config['objects']))

    print("~ done ~")
