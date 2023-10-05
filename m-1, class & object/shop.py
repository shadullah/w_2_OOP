class shop:
    cart =[]
    def __init__(self, buyer):
        self.buyer=buyer
    
    def add_cart(self, item):
        self.cart.append(item)

meh = shop('meh jaben')
meh.add_cart('shoes')
meh.add_cart('phone')

print(meh.buyer)
print(meh.cart)

nisho=shop('nisho')
nisho.add_cart('shirt')
nisho.add_cart('cap')
print(nisho.cart)

