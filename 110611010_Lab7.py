from operator import itemgetter
from collections import Counter

"""
First part:
You can try to use split() to get the list whose element is string
"""

s = " XYZ abc XYZ abc xyz abc ABC xyz "
#TODO

# Try to print out the list and find out some elements are just "zero-length" spaces.
L=s.split(sep=' ')
print(L)

"""
Second part:
You need to count the number of occurences of each word in the list
Hint: You can use Counter which has been imported to get the dictionary. 
"""
#TODO

cnt=Counter(L)


"""
Third part:
Try to print out the results by the number of occurrences in ascending order.
Reemeber don't print out the "zero-length" words.
Hint: Sorting the dictionary 
"""
#TODO

cnt.pop('')

L2 = sorted(cnt.items(), key = itemgetter(1))

for x in range(len(L2)):
    print(L2[x][0]," = ",L2[x][1])


