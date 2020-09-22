# Parameterized Constructor
class Employee:
    #parameterized constructor
    def __init__(self,name,no):
        self.name = name # instance variable
        self.no = no # instance variable
        print(self.name, 'Created')
        print(self)
    

emp1 = Employee('Shakib', 1) # instance 1
emp2 = Employee('Jhon', 2)  # instance 2
print(emp1.name)
print(emp2.name)
