class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount

    def withdrw(self, amount):
        if amount<self.min_withdraw:
            print( f'fokira. you can withdraw above {self.min_withdraw}')
        
        elif amount>self.max_withdraw:
            print( f'bank fokir hoye jabe.. you can withdraw maximum: {self.max_withdraw}')
        
        else:
            self.balance -= amount
            print( f'here is your money {amount}')
            print(f'you balance after withdraw {self.get_balance()}')
        
dbbl =Bank(15000)
dbbl.withdrw(25)
dbbl.withdrw(55000000000)
dbbl.withdrw(550)