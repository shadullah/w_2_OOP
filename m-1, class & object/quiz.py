def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']


    def call(self):
        print('calling someone i know')



my_phone = Phone()
# print(my_phone.call())
# call()

class A:
    def __init__(self, value):
        value = 3
        self.value = value

    def change(self):
        self.value = 12


ans = []
a = A(13)
ans.append(a.value)
a.change()
ans.append(a.value)
print(ans)


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone+5}'
        return text


my_phone = Phone()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)

arr = []
arr.append(10)
arr.append(10)
print(11)

cnt = {}
i = 1
if i not in cnt:
    cnt[i] = 1
else:
    cnt[i] += 1

print(cnt)