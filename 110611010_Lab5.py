import math
import sys
"""
This homework may need to use math library

You need to fix #TODO part to finish homework
test_number is your input
you can test number and output in terminal by following command:
"python Lab5.py (your number)"
Ex:python Lab5.py 97
"""

test_number = int(sys.argv[1])
print(test_number)
# TODO part
'''
you need write 2 program(Ch03, page16)
1.Naive algorithm
2.Quick algorithm
In this 2 program, you need to print "test_number is prime" if your input is a prime number
and you need to print "not a prime number" if your input is not a prime number
Hint:'break' can help you finish program faster

Therefore, when you run "python Lab5.py 97", you should see the result is

97
test_number is prime
test_number is prime

Meanwhile, when you run "python Lab5.py 6", you should see the result is

6
not a prime number
not a prime number
'''

n_i = 2
n_prime = True
while (n_i < test_number):
    if (test_number % n_i != 0):
        n_i += 1
    else:
        n_prime = False
        break
if (n_prime):
    print("test_number is prime")
else:
    print("not a prime number")

q_i = 2
number_sqrt = test_number ** 0.5
q_prime = True
while (q_i < number_sqrt):
    if (test_number % q_i != 0):
        q_i += 1
    else:
        q_prime = False
        break
if (q_prime):
    print("test_number is prime")
else:
    print("not a prime number")
