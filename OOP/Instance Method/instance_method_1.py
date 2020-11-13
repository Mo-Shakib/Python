class Student:
    def __init__(self, name, id):
        self.name = name # instance variable
        self.id = id # instance variable

    def details(self): # instance method
        print(f'Name: {self.name}, ID: {self.id}')


s1 = Student('Shakib', 1) # object 1
s2 = Student('Asit', 2) # object 2

s1.details()
s2.details()