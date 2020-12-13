string =  input()
dicx = {}
output = ''

for i in string:
    if i in dicx:
        dicx[i] += 1
    else:
        dicx[i] = 1
for x, y in dicx.items():
    if y != 1:
        output += (x + str(y))
    else:
        output += x
print(output)

# t = int(input())
# if t % 2 == 0:
#     print('All hail R@D!X2.0 - BUCC Week')
# else:
#     print('"Hola BUCCians!!"')