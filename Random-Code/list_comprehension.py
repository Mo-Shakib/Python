# author : Mohammad Shakib
# Python list comprehension

# Syntax of List Comprehension: [expression for item in list]
# example: 1
list_a = [x for x in range(10)]
print(list_a)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# example: 2
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)
# Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
