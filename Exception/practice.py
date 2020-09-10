# task - take 4 input in a list and check that is the list palendrom or not. have to handle Typeerror, value error and indexerror.
l = []
try:
    for i in range(4):
        num = int(input())
        l.append(num)
    lr = list(reversed(l))
    count = 0
    for x, y in zip(l, lr):
        if x == y:
            count+= 1
        else:
            count = 0
    if count == len(l):
        print('Yes')
    else:
        print('No')
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
except IndexError:
    print('Index error')
except Exception:
    print('Other error')