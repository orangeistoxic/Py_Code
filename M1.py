L = [13, 4, 7, 2, 1, 9]
m = 2

ans = L[:1] *(m-1) + L +L[len(L)-1:]*(m-1) 
print(ans)