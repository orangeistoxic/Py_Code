"""
In Lab 4, you will be asked to design a program with input() such that user can input two texts, x and y.
The rule is introduced in page.22 in the slide.
The following block can help you finish the assinment.
"""

# get x value
try:
    s = input('Input x: ')
    x = float(s)
except ValueError:
    x = s

# TODO part1. try to get y value (remember to use "try-except statement")

try:
    s = input('Input y: ')
    y = float(s)
except ValueError:
    y = s



# TODO part2. using "try-except statement" to print correct information
if type(x) is str :
    try:
        print(len(x)+len(y))
    except:
        print(x+str(y))
elif type(x) is float :
    try:
        print(abs(x+y))
    except:
        print(x)

"""
Also, there are some testcases you can use to test if your program can be implemented correctly.
1.  x is 1.5 and y is 2 --->        3.5
2.  x is 'ABC' and y is 'XYZW' ---> 7      
3.  x is 1.5 and y is 'XYZW' --->   1.5
4.  x is 'ABC' and y is 2.5 --->    ABC2.5
"""
