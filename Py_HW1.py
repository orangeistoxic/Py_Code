n=int(input())
Total_dispatches=0
Total_dispatches+=n//50
print("Bus:",n//50)
n=n%50
Total_dispatches+=n//10
print("Truck:",n//10)
n=n%10
Total_dispatches+=n//5
print("SUV:",n//5)
n=n%5
Total_dispatches+=n
print("Motorcycle:",n)
print("Total dispatches:",Total_dispatches)