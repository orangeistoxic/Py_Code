"""(1)"""

class Stock:
    def __init__(self,id='0000',name='None',price=0.0):
        self.id=id
        self.name=name
        self.price=price
    def __str__(self):
        return  self.id + ';' + self.name +';'+  str(self.price) 
    def __repr__(self):
        return self.__str__()


L = [Stock(), 
     Stock(id = '2330', name = 'TSMC', price = 438.0), 
     Stock(id = '1301', name = 'Formosa', price = 85.1),
     Stock(id = '2303', name = 'UMC', price = 38.05)]
print(L)


"""(2)"""


class StockKey:
    def __init__(self,index=''):
        self.index=index
    def __call__(self,sto):
        if self.index=='id':
            return sto.id
        elif self.index=='name':
            return sto.name
        elif self.index=='price':
            return sto.price


L.sort(key = StockKey('id'))
print(L)
L.sort(key = StockKey('name'))
print(L)
L.sort(key = StockKey('price'))
print(L)
