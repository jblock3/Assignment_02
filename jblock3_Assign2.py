##
# This program was coded by Jamie Block (Student number: 250777666)
# The program is designed to calculate the volume of a cube, a pyramid, or an ellipsoid
# as many times as he/she pleases.
# The sentinel value to end the loop and display the final output is "quit".
#


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
            cubeVolume = cubeVolume()
            print(cubeVolume)
            cubeVolumeList.append(cubeVolume)
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
        elif shapeInput == 'P' :
            pyramidVolume = pyramidVolume()
            print(pyramidVolume)
            pyramidVolumeList.append(pyramidVolume)
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
        elif shapeInput == 'E' :
            ellipsoidVolume = ellipsoidVolume()
            print(ellipsoidVolume)
            ellipsoidVolumeList.append(ellipsoidVolume)
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
        elif shapeInput == 'QUIT' :
            valid = True
        else :
            print('\nInvalid input! Please try again.')
            print()
            shapeInput = (input('Please enter "C" to calculate the volume of a cube, "P" for the volume of a pyramid, "E" for the volume of an ellipsoid, or "quit" to quit: ')).upper()
    if len(cubeVolumeList) != 0 or len(pyramidVolumeList) != 0 or len(ellipsoidVolumeList) != 0 :
        cubeVolumeList.sort()
        pyramidVolumeList.sort()
        ellipsoidVolumeList.sort()
        print()
        print('You have come to the end of the session.')
        print('The volumes calculated for each shape are shown below')
        print('Cube:', cubeVolumeList)
        print('Pyramid:', pyramidVolumeList)
        print('Ellipsoid:', ellipsoidVolumeList)
    else :
        print('You have come to the end of the session.')
        print('You did not perform any volume calculations')

main()
