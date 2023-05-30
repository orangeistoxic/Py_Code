class student: # design a class, datatype
    id = ''
    name = ''
    age = 0
    scores = []
James = student() # object instancing
James.id = 'A123'
James.name = 'James'
James.age = 18
James.scores = [90.0, 100.0, 85.0]
print(James.id)
print(James.name)
print(James.age)
print(James.scores)
print(type(James))