'''
follow by the examples on class
input list = [1, 10, 12, 2, 3, 320, 506]
your output list = ['Y001', 'Y010', 'Y012', 'Y002', 'Y003', 'Y320', 'Y506’]
write your program below
'''
L = [57, 99287, 1, 333, 9876, 20, 5446, 22, 3, 4444, 2, 777, 837]
#TODO
#you need to create a list follow by L(id) list

def Leng(inpt):
    inpt=str(inpt)
    return len(inpt)
leng=sorted(list(map(Leng,L)))
global num
num=leng[-1]
def MainFunc(inpt):
    inpt=str(inpt)
    return 'Y'+'0'*(num-len(inpt))+inpt
output=list(map(MainFunc,L))
print(output)


'''
print your result in the last part of program
hint:you need to use lambda function and map concept to finish this homework
'''
