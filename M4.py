L = [1, 2, 5]

St=1
while (1):
    isA=True
    for i in range(len(L)):
        if(St == L[i]):
            isA=False
            break
    
    for i in range(len(L)):
        if(not(isA)):
            break
        for j in range(len(L)):
            if(St==L[i]+L[j]):
                isA=False
                break


    for i in range(len(L)):
        if(not(isA)):
            break
        for j in range(len(L)):
            if(not(isA)):
                break
            for k in range(len(L)):
                if(St == L[i] + L[j] + L[k] ):
                    isA=False
                    break 

    if(isA):
        break
    else:
        St+=1

print(St)