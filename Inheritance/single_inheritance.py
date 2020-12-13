class Parent_Class:
    def method1(self):  # instance method
        print('This is method 1 in Parent_Class')
    def method2(self):
        print('This is method 2 in Parent_Class')

class child_class(Parent_Class):
    def method3(self):  # instance method
        print('This is method 3 in Child_Class')

ch1 = child_class()
ch1.method1()
ch1.method2()
ch1.method3()