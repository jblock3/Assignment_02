# Assignment_02
CS1026B - Assignment #2

CS1026: Assignment 2
Weight: 8%
Learning Outcome:
By completing this assignment, you will gain skills relating to
 using loops,
 using functions,
 and using lists in Python.
Task:
In this assignment, you will write a complete program in Python that computes the volume for a series
of shapes. Your program is expected to prompt the user for input and validate it before computing the
volume. In addition, your program should keep track of each volume that is calculated and at the end
display the volume for all the shapes. Your program should make use of functions, loops, and lists.

Functional Specifications:
1. Your program should first ask the user for the shape they are interested in, check to make sure
that their input is valid, if the input is not valid, keep on asking them until valid input is given.
Valid input options are: “cube”, “pyramid”, “ellipsoid”, “quit”

2. Based on their selection, prompt them for the necessary dimensions, it is safe to assume that
the user enters positive numeric values.

3. Next your program should calculate the volume for the specified shape given the dimensions
and display the volume to the screen. Your program should also store the volume.
Shape Volume
cube
𝑣𝑜𝑙𝑢𝑚𝑒 = 𝑎^3 where a is the length of a side
pyramid
𝑣𝑜𝑙𝑢𝑚𝑒 = 1/3 * b^2 * h; where b is base length and h is height
ellipsoid
𝑣𝑜𝑙𝑢𝑚𝑒 = 4/3 * pi * r1 * r2 * r3 where pi is π and r is used to represent
each radius

4. Your program should continue to compute volumes as specified by the user until the user
enters “quit”. At this point in time, your program should print the volumes based on their
shape and in ascending order.

If the user enters quit option before actually calculating any volumes show the output below.

5. In order to develop modular code, you MUST encapsulate the prompting for input and
calculation of volume for each shape within a function. That is, you MUST have at least 3
functions, one for cube, another for pyramid, and a third for ellipsoid.

6. The volumes should be formatted to 1 decimal place.

Non-functional Specifications:
1. Include brief comments in your code identifying yourself, describing the program, and describing
key portions of the code.
2. Assignments are to be done individually and must be your own work. Software may be used to
detect cheating.
3. Use Python coding conventions and good programming techniques, for example:
 Meaningful variable and function names
 Conventions for naming variables and constants
 Use of constants where appropriate
 Readability: indentation, white space, consistency
The name of the file you submit should be your UWO userid_Assign2.py. For instance, my assignment
would be oola_Assign2.py. Make sure you attach your python file to your assignment; DO NOT put
the code inline in the textbox.
Make sure that you develop your code with Python 3.5 as the interpreter. TAs will not endeavor to fix
code that uses earlier versions of Python.
What You Will Be Marked On:
 Functional specifications:
 Does the program behave according to specifications?
 Does the program handle invalid input?
