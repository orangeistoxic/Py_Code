L = [10, 1, 20, 30, 8, 5, 9, 3, 13, 11, 16, 4]
Gr=int(len(L)/4)

L1=L[2:len(L):4]+L[3:len(L):4]+L[0:len(L):4]+L[1:len(L):4]
TheLast=L1[len(L1)-1:]
L1.pop()
L3=L1*Gr
L4=L3[0:len(L3):Gr]
LAns=L4[0:Gr*4]+TheLast

print(LAns)
print(L1)
