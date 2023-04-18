"""
In Lab 6, you will be asked to finish two tasks.

1. Find out the maximum element, minimum element, and median in the list.
2. Calculating the standard deviation of median by the equation in CH3 p.32
"""
import random

# Don't modify the list
L = [i+1 for i in range(20)]
random.shuffle(L)
print(L)                       # You can print the content of the list


# First task: try to find out the maximum element, minimum element, and median in the list.
# Don't use any loop statement in this task.

# TODO
L.sort()
print(L)
Max=L[len(L)-1]
Min=L[0]
Half=int(len(L)/2)-1
if(len(L)%2==0):
    Med=(L[Half]+L[Half+1])/2
else:
    Med=L[Half+1]


# print the element of maximum, minimum and median element
print(Max)
print(Min)
print(Med)




# Second task: calculating the standard deviation of median by the equation in CH3 p.32
# You can use loop statement in this task

standard_deviation = 0.0

#TODO
div = 0.0
for i in range(len(L)):
    div+=(L[i]-Med)**2


standard_deviation=(div/(len(L)-1))**0.5


# print the value of standard deviation
print(standard_deviation)