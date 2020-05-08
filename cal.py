num1 = int(input("Enter first number: ")) #first input
op = input("Enter a valid opration: ") # opration
num2 = int(input("Enter second number: ")) # second input
if op == '+': # first condition
    result = num1 + num2
    print('Result: ' + str(num1) + ' + ' + str(num2) + ' = ' + str(result))
elif op == '-':
    result = num1 - num2
    print('Result: ' + str(num1) + ' - ' + str(num2) + ' = ' + str(result))
elif op == '*':
    result = num1 * num2
    print('Result: ' + str(num1) + ' * ' + str(num2) + ' = ' + str(result))
elif op == '/':
    result = num1 / num2
    print('Result: ' + str(num1) + ' / ' + str(num2) + ' = ' + str(result))
else:
    print("You entered: '" + op + "', It's a invalid opration!")

# Python calculotor by Mohammad Shakib (imoshakib.bd@gmail.com)
# 08 May, 2020; 09:21 AM