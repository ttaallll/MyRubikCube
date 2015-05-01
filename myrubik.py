__author__ = 'tal'



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
