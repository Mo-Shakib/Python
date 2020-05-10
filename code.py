# Codeforces problem 1A; 10 May, 2020

n, m, a = map(int, input().split()) # taking 3 int input

# 1st steatment

if n % a == 0:
    a1 = n // a
else:
    a1 = n // a + 1

# 2nd statement    

if m % a == 0:
    a2 = m // a
else:
    a2 = m // a + 1

# Output

print(a1 * a2)