A= [[1, 2, 3], [4, 5, 6]]
def transpose(A):
    B=list()
    for m in range(0,len(A[0])):
        L=list()
        for n in range(0,len(A)):
            L+=str(A[n][m])
        print(L)
        B.append(L)

    
    
    return B
B=transpose(A)
print(B)