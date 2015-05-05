__author__ = 'tal'

import copy

NUM_OF_CUBE = 3


cube = {
    'up': [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ], # Up

    'down': [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ], # Down

    'left': [
        [2,2,2],
        [2,2,2],
        [2,2,2]
    ], # Left

    'right': [
        [3,3,3],
        [3,3,3],
        [3,3,3]
    ], # Right

    'front': [
        [4,4,4],
        [4,4,4],
        [4,4,4]
    ], # Front

    'back': [
        [5,5,5],
        [5,5,5],
        [5,5,5]
    ]  # Back
}


def rotateLeft(side):

    oldside = side[:]

    side[0][0] = oldside[0][2]
    side[0][1] = oldside[1][2]
    side[0][2] = oldside[2][2]

    side[1][2] = oldside[2][1]
    side[2][2] = oldside[2][0]

    side[2][1] = oldside[1][0]
    side[2][0] = oldside[0][0]

    side[1][0] = oldside[0][1]


def rotateRight(side):

    oldside = side[:]

    side[0][0] = oldside[2][0]
    side[0][1] = oldside[1][0]
    side[0][2] = oldside[0][0]

    side[1][2] = oldside[0][1]
    side[2][2] = oldside[0][2]

    side[2][1] = oldside[1][2]
    side[2][0] = oldside[2][2]

    side[1][0] = oldside[2][1]

def convertRow(side1, side2, level):
    side1[level] = side2[level]

def convertColumn(side1, side2, level):
    for i in range(NUM_OF_CUBE):
        side1[i][level] = side2[i][level]

def F2R(cube, level):

    tempCube = copy.deepcopy(cube)
    convertRow(cube['front'], cube['left'], level)
    convertRow(cube['left'], cube['back'], level)
    convertRow(cube['back'], cube['right'], level)
    convertRow(cube['right'], tempCube['front'], level)

    if level == 0:
        rotateLeft(cube['up'])
    if level == 2:
        rotateRight(cube['down'])


def R2F(cube, level):

    tempCube = copy.deepcopy(cube)
    convertRow(cube['front'], cube['right'], level)
    convertRow(cube['right'], cube['back'], level)
    convertRow(cube['back'], cube['left'], level)
    convertRow(cube['left'], tempCube['front'], level)

    if level == 0:
        rotateRight(cube['up'])
    if level == 2:
        rotateLeft(cube['down'])

def F2U(cube, level):

    tempCube = copy.deepcopy(cube)
    convertColumn(cube['front'], cube['down'], level)
    convertColumn(cube['down'], cube['back'], level)
    convertColumn(cube['back'], cube['up'], level)
    convertColumn(cube['up'], tempCube['front'], level)

    if level == 0:
        rotateRight(cube['right'])
    if level == 2:
        rotateLeft(cube['left'])

def U2F(cube, level):

    tempCube = copy.deepcopy(cube)
    convertColumn(cube['front'], cube['up'], level)
    convertColumn(cube['up'], cube['back'], level)
    convertColumn(cube['back'], cube['down'], level)
    convertColumn(cube['down'], tempCube['front'], level)

    if level == 0:
        rotateLeft(cube['right'])
    if level == 2:
        rotateRight(cube['left'])

def R2U(cube, level):

    tempCube = copy.deepcopy(cube)

    # right to up
    for i in range(NUM_OF_CUBE):
        cube['up'][NUM_OF_CUBE - 1 - level][i] = cube['right'][i][level]

    # down to right
    for i in range(NUM_OF_CUBE):
        cube['right'][i][level] = cube['down'][level][NUM_OF_CUBE - 1 - i]

    # left to down
    for i in range(NUM_OF_CUBE):
        cube['down'][level][NUM_OF_CUBE - 1 - i] = cube['left'][NUM_OF_CUBE - 1 - i][NUM_OF_CUBE - 1 - level]

    # up to left
    for i in range(NUM_OF_CUBE):
        cube['left'][NUM_OF_CUBE - 1 -  i][NUM_OF_CUBE - 1 - level] = tempCube['up'][NUM_OF_CUBE - 1 - level][i]

    if level == 0:
        rotateLeft(cube['front'])
    if level == 2:
        rotateRight(cube['back'])

def U2R(cube, level):

    tempCube = copy.deepcopy(cube)

    # left to up
    for i in range(NUM_OF_CUBE):
        cube['up'][NUM_OF_CUBE - 1 - level][i] = cube['left'][NUM_OF_CUBE - 1 -  i][NUM_OF_CUBE - 1 - level]

    # down to left
    for i in range(NUM_OF_CUBE):
        cube['left'][NUM_OF_CUBE - 1 -  i][NUM_OF_CUBE - 1 - level] = cube['down'][level][NUM_OF_CUBE - 1 - i]

    # right to down
    for i in range(NUM_OF_CUBE):
        cube['down'][level][NUM_OF_CUBE - 1 - i] = cube['right'][i][level]

    # up to right
    for i in range(NUM_OF_CUBE):
        cube['right'][i][level] = tempCube['up'][NUM_OF_CUBE - 1 - level][i]


    if level == 0:
        rotateLeft(cube['back'])
    if level == 2:
        rotateRight(cube['front'])


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

colors = [
    bcolors.OKBLUE,
    bcolors.OKGREEN,
    bcolors.FAIL,
    bcolors.WARNING,
    bcolors.HEADER,
    bcolors.BOLD
]

def printLittleCube(cubeColor):
    sys.stdout.write(colors[cubeColor] + unichr(0x2588) + bcolors.ENDC + ' ')

import sys
def printSide(side):

    for i in range(NUM_OF_CUBE):
        for j in range(NUM_OF_CUBE):
            printLittleCube(side[i][j])
        print


def printCube(cube):
    orderOfPrint = ['front', 'right', 'up', 'left', 'back', 'down']
    for i in orderOfPrint:
        print i
        printSide(cube[i])


def main():
    # R2F(cube, 0)
    # F2R(cube, 1)
    # R2U(cube, 2)
    U2R(cube, 2)
    printCube(cube)


main()