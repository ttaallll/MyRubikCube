__author__ = 'tal'


import random
from myrubik import *
from problemsToSolve import *

NUM_OF_INITIAL_PARALLEL_SOLUTIONS = 100
NUM_OF_RANDOM_SOLUTION_MOVES = 20

NUM_OF_MUTATIONS = random.randint(0, 1)
# NUM_OF_MUTATIONS = 1
NUM_OF_BEST_SOLUTIONS_FOR_NEXT_GENERATION = 5
NUM_OF_MAJOR_BEST_SOLUTIONS = 2

NUM_OF_GOOD_ENOUGH_GRADE = 45

THRESHLOD_MOVES = 8
THRESHLOD_MOVES_DEGRADE = 5

# hueristicCheckCube = hueristicCheckCube1

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


    for i in range(NUM_OF_INITIAL_PARALLEL_SOLUTIONS):
        randomMoves = random.randint(1, NUM_OF_RANDOM_SOLUTION_MOVES)
        tempSolution1 = []
        for j in range(randomMoves):
            tempSolution1 += [allowedMoves[random.randint(0, len(allowedMoves) - 1)]]
        tempSolutions += [tempSolution1]

    return tempSolutions

def hueristicCheckCube1(cube1, numOfMoves):
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
        for i in range(0, len(cube1[tempColor])):
            for j in range(0, len(cube1[tempColor][i])):
                if cube1[tempColor][i][j] ==  colorsToCheck[tempColor]:
                    numOfMatches += 1

    if numOfMoves < THRESHLOD_MOVES:
        numOfMatches -= THRESHLOD_MOVES_DEGRADE

    return numOfMatches

def hueristicCheckCube2(cube1, numOfMoves):
    numOfMatches = 0

    colorsToCheck = {
        'up': 0,
        'down': 1,
        'left': 2,
        'right': 3,
        'front': 4,
        'back': 5
    }



    colorsFound = {}

    for tempColor in colorsToCheck.keys():
        colorsFound = {}
        for i in range(0, len(cube1[tempColor])):
            for j in range(0, len(cube1[tempColor][i])):
                if cube1[tempColor][i][j] not in colorsFound:
                    colorsFound[cube1[tempColor][i][j]] = 0
                colorsFound[cube1[tempColor][i][j]] += 1

        maxGradeColor = 0
        for temp1 in colorsFound.keys():
            if colorsFound[temp1] > maxGradeColor:
                maxGradeColor = colorsFound[temp1]
        numOfMatches += maxGradeColor


    # for keeping the grades more realistic
    if numOfMoves < THRESHLOD_MOVES:
        numOfMatches -= THRESHLOD_MOVES_DEGRADE

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

    return hueristicCheckCube2(cube1, len(solution))

def merge2Solutions(solution1, solution2):

    random1 = random.randint(0, min(len(solution1) - 1, len(solution2) - 1))

    # newSoultion1 = solution1[:random1] + solution2[random1:]
    # newSoultion2 = solution2[:random1] + solution1[random1:]

    newSoultion1 = solution1
    newSoultion2 = solution2

    return [newSoultion1, newSoultion2]

def mutation(solution):
    random1 = NUM_OF_MUTATIONS

    for tempRand in range(random1):

        addRemoveOrChange = random.randint(1,3)


        if addRemoveOrChange == 3:
            random2 = random.randint(0, len(solution) - 1)
            solution[random2] = allowedMoves[random.randint(0, len(allowedMoves) - 1)]
        if addRemoveOrChange == 1:
            random3 = random.randint(0, len(solution) - 1)
            solution = solution[random3:] + [allowedMoves[random.randint(0, len(allowedMoves) - 1)]] + solution[:random3]
        if addRemoveOrChange == 2: # if delete
            if len(solution) != 1:
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
    best15Solutions = sorted(solutionsGrades, key=itemgetter('grade'), reverse=True)[:NUM_OF_BEST_SOLUTIONS_FOR_NEXT_GENERATION]

    bestSolution = copy.deepcopy(best15Solutions[0])

    newSolutions = []

    for tempSolution in best15Solutions[NUM_OF_MAJOR_BEST_SOLUTIONS:]:
        for tempMajorSolution in range(NUM_OF_MAJOR_BEST_SOLUTIONS):
            merged = merge2Solutions(best15Solutions[tempMajorSolution]['solution'], tempSolution['solution'])
            newSolutions += [mutation(merged[0])]
            newSolutions += [mutation(merged[1])]

    for i in range(NUM_OF_MAJOR_BEST_SOLUTIONS):
        for j in range(i + 1, NUM_OF_MAJOR_BEST_SOLUTIONS):
            merged = merge2Solutions(best15Solutions[i]['solution'], best15Solutions[j]['solution'])
            newSolutions += [mutation(merged[0])]
            newSolutions += [mutation(merged[1])]

    for tempSolution in best15Solutions:
        newSolutions += mutation(tempSolution['solution'])
        # newSolutions += tempSolution['solution']



    return [newSolutions, bestSolution]


def main():

    cubeProblem1 = problem1()

    currentSolutions = generateRandomSolutions()

    bestSolutionGrade = 0
    currentGeneration = -1
    i = -1

    while bestSolutionGrade < NUM_OF_GOOD_ENOUGH_GRADE:

        currentGeneration += 1
        result1 = getNextGeneration(currentSolutions, cubeProblem1)
        bestSolutionGrade = result1[1]['grade']
        currentSolutions = result1[0]

        i += 1
        if i == 10:
            print 'generation ' + str(currentGeneration) + ' - best solution grade: ' + str(bestSolutionGrade) + \
                ' - num of moves: ' + str(len(result1[1]['solution']))
            i = 0

    print 'done'

if __name__ == "__main__":
    main()