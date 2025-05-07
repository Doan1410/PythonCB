class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def display(self):
        print("Ten ", self.name)
        print("Tuoi ", self.age)

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section= section
    def displayStudent(self):
        print("Ten : ", self.name)
        print("Tuoi :", self.age)
        print("Section : ", self.section)

a = Student("Doan Ngo","21",2)
a.displayStudent()
        