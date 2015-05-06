__author__ = 'tal'


import random
from myrubik import *
from problemsToSolve import *

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

def generateRandomSolutions():
    tempSolutions = []


    for i in range(NUM_OF_PARALLEL_SOLUTIONS):
        randomMoves = random.randint(1, NUM_OF_RANDOM_SOLUTION_MOVES)
        tempSolution1 = []
        for j in range(randomMoves):
            tempSolution1 += [allowedMoves[random.randint(0, len(allowedMoves) - 1)]]
        tempSolutions += [tempSolution1]

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
        for i in range(0, len(cube1[tempColor]) - 1):
            for j in range(0, len(cube1[tempColor][i]) - 1):
                if cube1[tempColor][i][j] ==  colorsToCheck[tempColor]:
                    numOfMatches += 1

    return numOfMatches

def getGradeOfSolution(solution, cubeProblem):
    cube1 = copy.deepcopy(cubeProblem)
    for tempStep in solution:
        if tempStep == 'F2U1':
            F2U(cube1, 0)
        if tempStep == 'F2U2':
            F2U(cube1, 1)
        if tempStep == 'F2U3':
            F2U(cube1, 2)

        if tempStep == 'U2F1':
            U2F(cube1, 0)
        if tempStep == 'U2F2':
            U2F(cube1, 1)
        if tempStep == 'U2F3':
            U2F(cube1, 2)

        if tempStep == 'F2R1':
            F2R(cube1, 0)
        if tempStep == 'F2R2':
            F2R(cube1, 1)
        if tempStep == 'F2R3':
            F2R(cube1, 2)

        if tempStep == 'R2F1':
            R2F(cube1, 0)
        if tempStep == 'R2F2':
            R2F(cube1, 1)
        if tempStep == 'R2F3':
            R2F(cube1, 2)

        if tempStep == 'R2U1':
            R2U(cube1, 0)
        if tempStep == 'R2U2':
            R2U(cube1, 1)
        if tempStep == 'R2U3':
            R2U(cube1, 2)

        if tempStep == 'U2R1':
            U2R(cube1, 0)
        if tempStep == 'U2R2':
            U2R(cube1, 1)
        if tempStep == 'U2R3':
            U2R(cube1, 2)

    return hueristicCheckCube1(cube1)

def merge2Solutions(solution1, solution2):

    random1 = random.randint(0, min(len(solution1) - 1, len(solution2) - 1))

    newSoultion1 = solution1[:random1] + solution2[random1:]
    newSoultion2 = solution2[:random1] + solution1[random1:]

    return [newSoultion1, newSoultion2]

def mutation(solution):
    random1 = random.randint(0, 3)

    for tempRand in range(random1):
        random2 = random.randint(-1, len(solution))
        if random2 != len(solution) and random2 != -1:
            solution[random2] = allowedMoves[random.randint(0, len(allowedMoves) - 1)]
        else:
            if random2 == len(solution):
                random3 = random.randint(0, len(solution) - 1)
                solution = solution[random3:] + [allowedMoves[random.randint(0, len(allowedMoves) - 1)]] + solution[:random3]
            else:
                del solution[random.randint(0, len(solution) - 1)]

    return solution


def getNextGeneration(currentSolutions, cubeProblem):

    best15Solutions = []

    solutionsGrades = []

    for tempSolution in currentSolutions:
        solutionsGrades += [{
                                'grade': getGradeOfSolution(tempSolution, cubeProblem),
                                'solution': tempSolution
                            }]


    from operator import itemgetter
    best15Solutions = sorted(solutionsGrades, key=itemgetter('grade'), reverse=True)[:7]

    bestSolution = copy.deepcopy(best15Solutions[0])

    newSolutions = []

    for tempSolution in best15Solutions[3:]:
        merged = merge2Solutions(best15Solutions[0]['solution'], tempSolution['solution'])
        newSolutions += [mutation(merged[0])]
        newSolutions += [mutation(merged[1])]

        merged = merge2Solutions(best15Solutions[1]['solution'], tempSolution['solution'])
        newSolutions += [mutation(merged[0])]
        newSolutions += [mutation(merged[1])]

        merged = merge2Solutions(best15Solutions[2]['solution'], tempSolution['solution'])
        newSolutions += [mutation(merged[0])]
        newSolutions += [mutation(merged[1])]

    merged = merge2Solutions(best15Solutions[0]['solution'], best15Solutions[1]['solution'])
    newSolutions += [mutation(merged[0])]
    newSolutions += [mutation(merged[1])]

    merged = merge2Solutions(best15Solutions[0]['solution'], best15Solutions[2]['solution'])
    newSolutions += [mutation(merged[0])]
    newSolutions += [mutation(merged[1])]

    merged = merge2Solutions(best15Solutions[2]['solution'], best15Solutions[1]['solution'])
    newSolutions += [mutation(merged[0])]
    newSolutions += [mutation(merged[1])]

    return [newSolutions, bestSolution]


def main():

    cubeProblem1 = problem1()

    currentSolutions = generateRandomSolutions()

    bestSolutionGrade = 0
    currentGeneration = -1

    while bestSolutionGrade < 45:

        currentGeneration += 1
        result1 = getNextGeneration(currentSolutions, cubeProblem1)
        bestSolutionGrade = result1[1]['grade']
        currentSolutions = result1[0]

        print 'generation ' + str(currentGeneration) + ' - best solution grade: ' + str(bestSolutionGrade)

    print 'done'

if __name__ == "__main__":
    main()