__author__ = 'tal'

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

    tempFront = cube['front'][level]
    cube['front'][level] = cube['left'][level]
    cube['left'][level] = cube['back'][level]
    cube['back'][level] = cube['right'][level]
    cube['right'][level] = tempFront

    if level == 0:
        rotateLeft(cube['up'])
    if level == 2:
        rotateRight(cube['down'])


def R2F(cube, level):

    tempFront = cube['front'][level]
    cube['front'][level] = cube['right'][level]
    cube['right'][level] = cube['back'][level]
    cube['back'][level] = cube['left'][level]
    cube['left'][level] = tempFront

    if level == 0:
        rotateRight(cube['up'])
    if level == 2:
        rotateLeft(cube['down'])

def U2F(cube, level):

    tempFront = cube['front'][:]
    convertColumn(cube['front'], cube['up'], level)
    convertColumn(cube['up'], cube['back'], level)
    convertColumn(cube['back'], cube['down'], level)
    convertColumn(cube['down'], tempFront, level)

    if level == 0:
        rotateLeft(cube['right'])
    if level == 2:
        rotateRight(cube['left'])

def F2U(cube, level):

    tempFront = cube['front'][:]
    convertColumn(cube['front'], cube['down'], level)
    convertColumn(cube['down'], cube['back'], level)
    convertColumn(cube['back'], cube['up'], level)
    convertColumn(cube['up'], tempFront, level)

    if level == 0:
        rotateRight(cube['right'])
    if level == 2:
        rotateLeft(cube['left'])