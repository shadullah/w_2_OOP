class phone: 
    manufactured = 'China'

# constructor
    def __init__(self, owner, brand ,price):
        self.owner = owner
        self.brand=brand
        self.price=price

    def send_sms(self,phone, sms):
        text=f'sending to {phone} {sms}'
        print(text)

myPhn = phone('sakib', 'oppo', 8000)
print(myPhn.owner, myPhn.brand, myPhn.price)

her_phn = phone('she', 'iphn', 120000)
print(her_phn.brand, her_phn.price)

her_phn.send_sms(2983, 'hi')

