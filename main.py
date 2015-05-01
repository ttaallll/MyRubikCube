__author__ = 'tal'

import pycuber as pc

def main():

    # Create a Cube object
    mycube = pc.Cube()

    # Do something at the cube.
    mycube("R U R' U'")

    print(mycube)

main()