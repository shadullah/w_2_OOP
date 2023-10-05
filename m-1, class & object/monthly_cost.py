class month_cost:
    def __init__(self, name):
        self.name=name
        self.cart=[]

    def add_cart(self, item , price, quantity):
        product={'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_itm(self, item_nam):
        for item in self.cart:
            if item['item']==item_nam:
                self.cart.remove(item)
                return 
        print(f'{item_nam} is not found')



    def checkout(self, amount):
        ttl= 0
        for item in self.cart:
            # print(item)
            ttl += item['price'] * item['quantity']
        print('ttl price' , ttl)
        if amount<ttl:
            print( f'please provide {ttl - amount} more')
        else:
            extra = amount -ttl
            print(f'here is your left {extra}')

dada = month_cost('sakib')
dada.add_cart('alu', 50, 6)
dada.add_cart('dim', 12, 24)
dada.add_cart('rice', 50, 5)
# dada.add_cart('rice')

print(dada.cart)
dada.checkout(1600)
dada.remove_itm('dudu')
print(dada.cart)
