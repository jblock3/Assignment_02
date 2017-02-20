##
# This program was coded by Jamie Block (Student number: 250777666)
# The program is designed to calculate the volume of a cube, a pyramid, or an ellipsoid
# as many times as he/she pleases.
# The sentinel value to end the loop and display the final output is "quit".
#

# Defining functions for calculating the volumes of the shapes

def cubeVolume() :
    sideLength = float(input('What is the length of one side of the cube?: '))
    volume = sideLength ** 3
    cubeVolumeList.append(volume)
    cubeVolumeList.sort()
    print('The volume of a pyramid with a side length of %f is %.1f' % (sideLength, volume))

def pyramidVolume() :
    base = float(input('What is the base length of the pyramid?: '))
    height = float(input('What is the height of the pyramid?: '))
    volume = (1 / 3) * (base ** 2) * height
    pyramidVolumeList.append(pyramidVolume)
    pyramidVolumeList.sort()
    print('The volume of a pyramid with a base of %f and a height of %f is %.1f' % (base, height, volume))

def ellipsoidVolume() :
    from math import pi
    r1 = float(input('What is the value of radius 1?: '))
    r2 = float(input('What is the value of radius 2?: '))
    r3 = float(input('What is the value of radius 3?: '))
    volume = (4 / 3) * pi * r1 * r2 * r3
    ellipsoidVolumeList.append(ellipsoidVolume)
    ellipsoidVolumeList.sort()
    print('The volume of an ellipsoid with a radius 1 of %f, a radius 2 of %f, and a radius 3 of %f is %.1f')

# Initialization of empty lists

cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList = []

# Creating the main function to be called at the end of the program

def main() :
    shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
    valid = False
    while not valid :
        if shapeInput == 'C' :
            cubeVolume()
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
        elif shapeInput == 'P' :
            pyramidVolume()
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
        elif shapeInput == 'E' :
            ellipsoidVolume()
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
        elif shapeInput == 'QUIT' :
            valid = True
        else :
            print('\nInvalid input! Please try again.')
            print()
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
    if len(cubeVolumeList) != 0 or len(pyramidVolumeList) != 0 or len(ellipsoidVolumeList) != 0 :
        print()
        print('You have come to the end of the session.')
        print('The volumes calculated for each shape are shown below')

        print('Cube: ', cubeVolumeList)
        print('Pyramid:', pyramidVolumeList)
        print('Ellipsoid:', ellipsoidVolumeList)
    else :
        print('\nYou have come to the end of the session.')
        print('You did not perform any volume calculations')

main()
