L = ['DAVID', 'TINA', 'BOB', 'ABBA', 'ELSA', 'HANNAH', 'JACK']
Ans = []
for i in range(len(L)):
    Na=list(L[i])
    j=1
    isP=True
    while(j<=len(Na)):
        if(Na[j-1] != Na[len(Na)-j]):
            isP=False
            break
        j+=1    
    
    if(isP):
        Ans+=L[i:i+1]
    

print(Ans)