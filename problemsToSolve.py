__author__ = 'tal'

from myrubik import *


def problem1():
    cube1 = createCube()


    R2U(cube1, 0)
    F2U(cube1, 1)
    R2U(cube1, 1)
    R2F(cube1, 2)
    R2U(cube1, 0)
    F2U(cube1, 1)
    U2R(cube1, 2)
    R2U(cube1, 0)

    return cube1


def problem2():
    cube1 = createCube()


    R2U(cube1, 0)
    F2U(cube1, 1)
    R2U(cube1, 1)


    U2R(cube1, 1)
    U2F(cube1, 1)
    U2R(cube1, 0)

    return cube1


def main():

    cube1 = problem2()

    printCube(cube1)


if __name__ == "__main__":
    main()