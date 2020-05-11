def is_leap(year):
    leap = False

"""
Conditions:
1. The year can be evenly divided by 4, is a leap year, unless:
2. The year can be evenly divided by 100, it is NOT a leap year, unless:
3. The year is also evenly divisible by 400. Then it is a leap year.

"""    
    #logic here
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))

# 12 May, 2020; 01:07 AM