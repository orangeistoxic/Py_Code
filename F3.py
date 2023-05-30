import re

class file:
    def __init__(self,one,two,three):
        self.one=one
        self.two=two
        self.three=three

    def __str__(self):
        return '\''+self.one+'['+self.two+']'+self.three+'\''
    def __repr__(self):
        return self.__str__()
def func(stri):
    s=re.split('\[|\]',stri)
    c=file(s[0],s[1],s[2])
    return c
D = ['James[11].jpeg', 'abcdef[130].dat', 'xyz9999[10].dat', 'b[101].c', 'u[101].mp3', 'Billy[100].mp3', 'a[101].jpeg']

D=list(map(func,D))

class key1:
    def __call__(self,file):
        return int(file.two)
    
def datSort(D):
    D.sort(key=key1())
    return D

print(datSort(D))
