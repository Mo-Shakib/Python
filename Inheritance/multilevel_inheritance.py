class Parent_Class: # Base class
    def method1(self):  # instance method
        print('This is method 1 in Parent_Class')

    def method2(self):
        print('This is method 2 in Parent class')


class child(Parent_Class): # Derived class 1
    def method3(self):  # instance method
        print('This is method 3 in Child class')


class grandchild(child): # Derived class 2
    def method4(self):  # instance method
        print('This is method 4 in grandchild Class')


ch1 = grandchild() # object of derived class 2
ch1.method1()
ch1.method2()
ch1.method3()
ch1.method4()
