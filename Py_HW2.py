# Q1
L1 = [10, 20, 30,'ABC', '123', '456']           
a1=int(len(L1)/2)+len(L1)%2
L1=L1[a1:]+L1[:a1]
print(L1)

# Q2
L2 = [10, 20, 30,40,'ABC', '123', '456']
a2=int(len(L2)/2)+len(L2)%2
L2=L2[a2:]+L2[:a2]
print(L2)

# Addition
def swap_list(input_list):
    a= int(len(input_list)/2)+len(input_list)%2
    output_list = input_list[a:]+input_list[:a]
    return output_list
