class calcu:
    brand = 'Casio ms-100'

    def add(self, num1, num2):
        sum = num1+num2
        return sum

cal=calcu()
res = cal.add(5,5)
print(res)