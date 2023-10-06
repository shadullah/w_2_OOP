# base class/ parent class, common attribute + functionality class
#?derived class, child class, common attribute

class Gadget:
    def __init__(self,brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'running laptop: {self.brand}'



class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
    
    def coding(self):
        return f'learning python'
    
class Phone(Gadget):
    def __init__(self,brand, color, price, origin,dua_sim) -> None:
        self.dua_sim = dua_sim
        super().__init__(brand, price,color, origin)

    def phn_cl(self, number,text):
        return f'sending sms to: {number} with {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.color} {self.dua_sim}'
    
class Camera:
    def __init__(self,pixel) -> None:
        self.pixel =pixel
        
    
# inheritance
myPhn = Phone('iphn',120000,'silver','china',True)

print(myPhn.brand)
print(myPhn)
