class family:
    def __init__(self, address) -> None:
        self.address = address


class School:
    def __init__(self, id, lvl) -> None:
        self.id = id
        self.lvl = lvl

class sports:
    def __init__(self,game) -> None:
        self.game = game

class Student(family, School, sports):
    def __init__(self, address, id, level, game) -> None:
        School.__init__(self,id,level)
        sports.__init__(self,id,level)
        super().__init__(address)

        