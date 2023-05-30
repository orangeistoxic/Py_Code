addr = 'jameschengcs@nctu.edu.tw;emily@nycu.edu.tw;edf@ntu.edu.tw;aabbcc@gmail.com'
def parseMails(addr):
    L1=addr.split(sep=';')
    class mail:
        def __init__(self,name,domain):
            self.name=name
            self.domain=domain
        def __str__(self):
            return '{\'account\': \''+self.name+'\', \'domain\': \''+self.domain+'\' }'
        def __repr__(self):
            return self.__str__()
    

    def func(stri):
        s=stri.split(sep='@')
        e=mail(s[0],s[1])
        return e
    L2=list(map(func,L1))

    class key1:
        def __call__(self,email):
            return email.domain
        
    L2.sort(key=key1())

    return L2

print(parseMails(addr))