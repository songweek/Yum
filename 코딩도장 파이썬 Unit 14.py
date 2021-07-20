#14.1
x = 5
if x == 10:
    print('10입니다')

else:
    print('10이 아닙니다')

#14.2
if x == 10:
    print('10입니다') 
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다') 

#14.3
if True:
    print('참')
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')
 
if None:
    print('참')
else:
    print('거짓')


if 0:
    print('참')
else:
    print('거짓')
 
if 1:
    print('참')
else:
    print('거짓')
 
if 0x1F: 
    print('참')
else:
    print('거짓')
 
if 0b1000:
    print('참')
else:
    print('거짓')
 
if 13.5:
    print('참')
else:
    print('거짓')

if 'Hello':
    print('참')
else:
    print('거짓')
 
if '':
    print('참')
else:
    print('거짓')

#14.4
b = 10
c = 20
 
if b == 10 and c == 20:
    print('참')
else:
    print('거짓')

if 0 < b < 20:
    print('20보다 작은 양수입니다')

#14.6
d = 75
e = True
 
if d >= 80 and e == True:
    print('합격')
else:
    print('불합격')


#14.7
f , g, h, i = map(int, input().split())
j = (f + g + h + i) / 4

if 0 <= f < 101 and 0 <= g < 101 and 0 <= h < 101 and 0 <= i < 101:
    if j >= 80:
        print('합격')

    else:
        print('불합격')

else:
    print('잘못된 점수')