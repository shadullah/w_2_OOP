class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("vat mangsho khay")

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print("ok now")

    def __add__(self, other):
        return self.age + other.age
    def __mul__(self, other):
        return self.weight + other.weight
    def __len__(self):
        return self.height
    
    def __gt__(self, other):
        return self.age > other.age

sakib = Cricketer('sakib', 38, 68, 91, 'BD')
mush = Cricketer('sakib', 8, 20, 91, 'BD')
# sakib.eat()
# sakib.exercise()

print(45+63)
print('sakib' + 'rakib')
print([23,98] + [5,6,7,8])
print(sakib + mush)
print(sakib * mush)
print(len(sakib))
print(sakib>mush)
