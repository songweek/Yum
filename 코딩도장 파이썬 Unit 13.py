# 13.1
x = 10
if x == 10:
    print('10입니다')

if x == 10:
    pass #TODO: x가 10일 경우 처리

#13.2
if x == 10:
    print('x의 숫자는')
    print('10입니다')

#13.3
y = 15

if y >= 10:
    print('10 이상입니다')

    if y == 15:
        print('15입니다')
        
    if y == 20:
        print('20입니다')

#13.4
a = int(input())

if a == 10:
    print('10입니다')

if a == 20:
    print('20입니다')

#13.6
b = 5
 
if b == 5                    :
    print('ok')

#13.7
c = int(input())
d = input()

if d == 'Cash3000':
    c-=3000
if d == 'Cash5000':
    c-=5000

print(c)