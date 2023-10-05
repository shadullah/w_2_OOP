class Student:
    def __init__(self, name, mycls, id):
        self.name = name
        self.id = id
        self.mycls = mycls

    def __repr__(self,) -> str:
        return f'student with name: {self.name}, class: {self.mycls}, id: {self.id}'

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.id = id
        self.subject =subject

    def __repr__(self) -> str:
        return f'teacher: {self.name}, subject: {self.subject}, id: {self.id}'
    
class school:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers=[]
        self.students=[]

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee<6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra fee: {fee-6500}'
        
    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('----------OUR TEACHERS----------')
        for teacher in self.teachers:
            print(teacher)
        print('----------OUR STUDENTS----------')
        for student in self.students:
            print(student)
        return 'all done'

# alia = Student('alia', 9 , 1)
# ranver = Teacher('rander', 'algo', 101)
# print(alia)
# print(ranver)

phitron = school('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('shariya', 7000)
phitron.enroll('vijan', 9000)

phitron.add_teacher('Tom cruise', 'DS')
phitron.add_teacher('AJ', 'C++')
phitron.add_teacher('jhankar', 'python')

print(phitron)