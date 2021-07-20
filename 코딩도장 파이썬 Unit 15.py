#15.1
x = 20
if x == 10:
    print('10입니다')
elif x == 20:
    print('20입니다')

a = 30
if a == 10:
    print('10입니다')
elif a == 20:
    print('20입니다')
else:
    print('10도 20도 아닙니다')

b = int(input())
 
if b == 1:
    print('콜라')
elif b == 2:
    print('사이다')
elif b == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

#15.3
c = int(input())
if 11 <= c <= 20:
    print('11~20')
elif 21 <= c <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

#15.4
age = int(input())
balance = 9000
if 7 <= age <= 12:
    balance -= 650

elif 13 <= age <= 18:
    balance -= 1050

elif 19 <= age:
    balance -= 1250

print(balance)