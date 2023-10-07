# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod

class shopping: 
    cart =[]
    origin = 'china'

    def __init__(self,name, location) -> None:
        self.name = name # instance attribute
        self.location = 'jam er maj khane'
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying {item} for price:{price} remain {remaining}') 

    @staticmethod
    def multiply( a,b):
        res = a*b
        print(res)

    @classmethod
    def hudai(self, item):
        print("hudai dekhi", item)

boshun = shopping('dhara', 'loc')
# boshun.purchase('lungi', 500, 1000)
boshun.hudai('lungi')
# boshun.hudai('lungi')
shopping.hudai('lungi')

# static method
shopping.multiply(4,6)
boshun.multiply(4,6)

# shopping().purchase(2,3,3)