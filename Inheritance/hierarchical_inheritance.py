class Parent_Class: # Base class
    def method1(self):  # instance method
        print('This is method 1 in Parent class')

    


class child_1(Parent_Class): # Derived class 1
    def method2(self):
        print('This is method 2 in child class 1')

class child_2(Parent_Class): # Derived class 1
    def method3(self):  # instance method
        print('This is method 3 in child class 2')
        

ch1 = child_1()
ch2 = child_2()

ch1.method1()
ch2.method1()