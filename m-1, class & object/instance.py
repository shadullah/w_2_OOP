class shop:
    shopping_mall = 'bonshun'
    def __init__(self, buyer):
        self.buyer=buyer
        self.cart=[] # cls is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

meh = shop('meh jaben')
meh.add_to_cart('shoes')
meh.add_to_cart('phone')

# print(meh.buyer)
print(meh.cart)

nisho=shop('nisho')
nisho.add_to_cart('shirt')
nisho.add_to_cart('cap')
print(nisho.cart)