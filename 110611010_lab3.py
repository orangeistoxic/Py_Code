"""
This homework need binary concept to
understand how to use bit operation

You need to fix "#TODO part" to finish homework

Hint:convert int into binary expression
A
0b10001100
0b1110001
0b11001000
0b11000111

when B[4]=192
0b10001100
0b1110001
0b11001000
0b11000000 "192"

when B[4]=191
0b10001100
0b1110001
0b11001000
0b10111111 "191"

M
0b11111111
0b11111111
0b11111111
0b11110000
"""
A = [140, 113, 200, 199]
B1 = [140, 113, 200, 192]
B2 = [140, 113, 200, 191]
M = [255, 255, 255, 240]
s_A_B1 = 0
s_A_B2 = 0
'''
You need to follow spec to test 2 cases:
1.A and B1 are in the same domain or not
2.A and B2 are in the same domain or not
'''
#TODO part

#check result is zero or nonzero


for i in range(0,4):
    s_A_B1+=((A[i] & M[i]) - ( B1[i] & M[i])) ** 2
for i in range(0,4):
    s_A_B2+=((A[i] & M[i]) - ( B2[i] & M[i])) ** 2
    

print(s_A_B1)
print(s_A_B2)