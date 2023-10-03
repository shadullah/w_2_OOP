def call():
    print('calling someone i dony knoe')
    return 'cl done'

class phn:
    price = 7300
    color = 'black'
    brand = 'oppo'
    features= ['camera', 'blutooth', 'wifi']

    def call(self):
        print("calling one person")

    def send_sms(self, phn, sms):
        text= f'sending sms to {phn} and massage={sms}'
        return text

myPhn = phn()
print(myPhn.features)
myPhn.call()
res=myPhn.send_sms(32198, 'I forgot to miss you')
print(res)
