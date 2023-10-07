"""
#inheritence
class Animal:
    pass

#Dog is a animal
class Dog(Animal):
    pass

class Tiger(Animal):
    pass

class furniture:
    pass

class Chair(furniture):
    pass
"""

class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return 'engine started'
    
class Driver:
    def __init__(self) -> None:
        pass

# car "has a" engine
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()