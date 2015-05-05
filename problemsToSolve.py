__author__ = 'tal'

import copy
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




def main():

    cube1 = problem1()

    printCube(cube1)


if __name__ == "__main__":
    main()