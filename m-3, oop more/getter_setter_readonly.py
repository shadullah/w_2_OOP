# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.


class User:
    def __init__(self, name, age, money) -> None:
         self._name=name
         self._age=age
         self.__money=money 

    # getter without any setter is readonly attribute
    @property # decorator ; Now it is converted to attribute from method
    def age(self):
         return self._age
    
    #getter
    @property
    def salary(self):
         return self.__money
    

    #setter
    @salary.setter
    def salary(self, value):
         if value < 0:
              print("salary cannot be negative")
         self.__money += value

samsu = User('kopa', 21, 12000)
# print(samsu.__money) #acessing private property will get error
# print(samsu.age()) # printing type -- method 
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)
