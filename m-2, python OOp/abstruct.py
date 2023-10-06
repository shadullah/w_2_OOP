from abc import ABC, abstractmethod
#abdsturct base class

class Animal(ABC):
    @abstractmethod  # enforce all derived cls to have a eat method
    def eat(self):
        print('hey nana! eating banna')
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.category= 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('hey nana!a')

layka = Monkey('lucky')
layka.eat()