# Parameterized Constructor
class Employee:
    #parameterized constructor
    def __init__(self,name):
        self.name = name # instance variable
        print(self.name, 'Created')

emp1 = Employee('Shakib') # instance 1
emp2 = Employee('Jhon')  # instance 2
print(emp1.name)
print(emp2.name)