__author__ = 'tal'


import random

NUM_OF_PARALLEL_SOLUTIONS = 30
NUM_OF_RANDOM_SOLUTION_MOVES = 20


allowedMoves = [
    'F2U1', 'F2U2', 'F2U3',
    'U2F1', 'U2F2', 'U2F3',

    'F2R1', 'F2R2', 'F2R3',
    'R2F1', 'R2F2', 'R2F3',

    'R2U1', 'R2U2', 'R2U3',
    'U2R1', 'U2R2', 'U2R3',
    ]

currentSolutions = []

def generateRandomSolutions():
    tempSolutions = []

    for i in range(NUM_OF_PARALLEL_SOLUTIONS):
        randomMoves = random.randint(1, NUM_OF_RANDOM_SOLUTION_MOVES)
        for j in range(randomMoves):
            tempSolutions[i] += [allowedMoves[random.randint(0, len(allowedMoves))]]

    return tempSolutions

def hueristicCheckCube1(cube1):
    numOfMatches = 0

    colorsToCheck = {
        'up': 0,
        'down': 1,
        'left': 2,
        'right': 3,
        'front': 4,
        'back': 5
    }

    for tempColor in colorsToCheck.keys():
        for i in cube1[tempColor]:
            for j in cube1[tempColor][i]:
                if cube1[tempColor][i][j] ==  colorsToCheck[tempColor]:
                    numOfMatches += 1

    return numOfMatches

