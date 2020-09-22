class Student:
    def __init__(self, name, id):
        self.name = name # instance variable
        self.id = id # instance variable
        # print('Student object created')


s1 = Student('Bob', 11)
s2 = Student('Ross', 21)

print(s1.name, s1.id)
print(s2.name, s2.id)
s2.id = 111 #updating s2.id 
print(s2.name, s2.id) # printng after updateing
