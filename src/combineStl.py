import argparse
import numpy
import stl
import os
import random
from stl import mesh


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='combining two random stl-files of folder1 and folder 2 ',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-f1', '--folder1',  help='path to first folder of stl-files', required=True)
    parser.add_argument(
        '-f2', '--folder2',  help='path to second folder of stl-files', required=True)
    parser.add_argument(
        '-n', '--ntimes',  help='n files will be generated', required=True, type=int)
    parser.add_argument(
        '-d', '--destination',  help='destination for saving the combined stl', required=True)

    config = vars(parser.parse_args())

    for n in range(config['ntimes']):
        randomFile1 = random.choice(os.listdir(config['folder1']))
        randomFile2 = random.choice(os.listdir(config['folder2']))

        mesh1 = mesh.Mesh.from_file(config['folder1']+randomFile1)
        mesh2 = mesh.Mesh.from_file(config['folder2']+randomFile2)

        combinedFileName = randomFile1[len(
        randomFile1)-25:len(randomFile1)-4]+randomFile1[len(randomFile2)-25:len(randomFile2)]

        combined = mesh.Mesh(numpy.concatenate([mesh1.data, mesh2.data]))
        combined.save(config['destination']+combinedFileName, mode=stl.Mode.ASCII)
