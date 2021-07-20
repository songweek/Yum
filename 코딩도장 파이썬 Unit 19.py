#19.1
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

#19.2
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

#19.3
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#19.5
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

#19.6(모르겠음 ㅠㅠ)
a = int(input())
for i in range(a):
    for j in range(a*2-1):
        k = a - 1
        while k 