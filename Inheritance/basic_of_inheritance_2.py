# multi level inheritence

class parent:
    def __init__(self):  # instance
        print('constructor of parent class')

    def method1(self):  # instance method
        print("method 1 of parent")

    def method2(self):  # instance method
        print("method 2 of parent")


class child_1(parent):
    def __init__(self):  # instance
        print('constructor of child 1')
    def method3(self):  # instance method
        print("method 3 of child 1")

    def method4(self):  # instance method
        print("method 4 of child 1")


class child_2(parent):
    def __init__(self):  # instance
        print('constructor of child 2')

    def method5(self):  # instance method
        print("method 5 of child 2")

    def method6(self):  # instance method
        print("method 6 of child 2")


class grandchild_1(child_1):
    def __init__(self):  # instance
        print('constructor of grandchild')

    def method7(self):  # instance method
        print("method 7 of grandchild 1")


class grandchild_2(child_1, child_2):  # this clas has access to all the methods
    def method7(self):  # instance method
        print("method 8 of grandchild 2")


p = child_1()
p.method1()
p.method3()
