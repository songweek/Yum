#17.1
i = 0
while i < 100:
    print('Hello, world!')
    i += 1

i = 1
while i <= 100:
    print('Hello, world!', i)
    i += 1

i = 100
while i > 0:
    print('Hello, world!')
    i -= 1

count = int(input('반복할 횟수를 입력하세요:'))
i = 0
while i < count: 
    print('Hello, world!', i)
    i += 1

#17.3
#??? random.random() 실행이 안 되서 못 함

#17.4
#while True:
    #print('Hello, world!')
    

#while 1:
    #print('Hello, world!')
    

#while 'Hello':
    #print('Hello, world!')
    

#17.5
i = 2
j = 5
while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1

#17.6
c = int(input())
while c >= 1350:
    c -=1350
    print(c)
