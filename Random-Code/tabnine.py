# t = int(input())
# for i in range(t):
#     print("Hello There")
#     x,y = map(int,input().split())
#     print('x:',x)
#     print('y:',y)

class Information:
    def __init__(self, name, address, city,gender):
        self.name = name
        self.address = address
        self.city = city
        self.gender = gender

    def details(self): # instance method
        print('Name:',self.name)
        print('Address:',self.address)
        print('City:',self.city)
        print('Gender:',self.gender)

people1 = Information('Shakib','15/A Gopibag','Dhaka','Male')
people1.details()
print('==================================')
people2 = Information('Tahasin','15/A Gopibag','Dhaka','Male')
people2.details()