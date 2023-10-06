class Bank:
    def __init__(self, holder_name, initial_depo) -> None:
        self.holder_name=holder_name #public attribute
        self._branch='bonani'
        self.__balance = initial_depo #private attribute

    def deposite(self, amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
            return amount
        else:
            print('fokir taka nai')


rafsan = Bank('choto bro', 10000)
rafsan.deposite(2000)
print(rafsan.get_balance())
rafsan.withdraw(2000)
print(rafsan.holder_name)
print(rafsan.get_balance())

print(rafsan._branch)
# print(rafsan.get_balance)
        