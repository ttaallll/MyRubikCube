__author__ = 'tal'



cube = {
    'up': [[0,0,0,],
     [0,0,0],
     [0,0,0]], # Up

    'down': [1,1,1,
     1,1,1,
     1,1,1], # Down

    'left': [2,2,2,
     2,2,2,
     2,2,2], # Left

    'right': [3,3,3,
     3,3,3,
     3,3,3], # Right

    'front': [4,4,4,
     4,4,4,
     4,4,4], # Front

    'back': [5,5,5,
     5,5,5,
     5,5,5]  # Back
}


def rotateLeft(side):
    side[]

def F2R1(cube):

    tempFront = cube['front'][0]
    cube['front'][0] = cube['left'][0]
    cube['left'][0] = cube['back'][0]
    cube['back'][0] = cube['right'][0]
    cube['right'][0] = tempFront

