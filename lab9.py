class student:
    def __init__(self, id = '', name = '',age = 18, scores = [0.0, 0.0, 0.0]):
        self.id = id
        self.name = name
        self.age = age
        self.scores = scores

class SortKey:
    def __init__(self, index=0):
        self.index = index
    def __call__(self, student_1):
        if self.index==0:
            return student_1.scores[0]
        elif self.index==1:
            return student_1.scores[1]
        elif self.index==2:
            return student_1.scores[2]

Mary = student('A000', 'Mary', 20, [90, 80, 75])
James = student('A010', 'James', 20, [82, 60, 91])
Ann = student('A008', 'Ann', 19, [95, 92, 100])
Tim = student('A208', 'Tim', 21, [56, 72, 50])
L = [Mary, James, Ann, Tim]
print([i.name for i in L])
L.sort(key = SortKey()) # Sorting by scores[0]
print([i.name for i in L])

L.sort(key = SortKey(1)) # Sorting by scores[1]
print([i.name for i in L])
L.sort(key = SortKey(2)) # Sorting by scores[2]
print([i.name for i in L])
