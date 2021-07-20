#16.1
for a in range(100):
    print('Hello, world!')

for a in range(100):
    print('Hello, world!', a)

#16.2
for a in range(5, 12):
    print('Hello, world!', a)

for a in range(0, 10, 2):
    print('Hello, world!', a)

for a in range(10, 0, -1):
    print('Hello, world!', a)

for a in reversed(range(10)):
    print('Hello, world!', a)

count = int(input('반복할 횟수를 입력하세요: '))
 
for a in range(count):
    print('Hello, world!', a)

#16.3
b = [10, 20, 30, 40, 50]
for i in b:
    print(i)

c = ('apple', 'orange', 'grape')
for d in c:
    print(d)

for letter in 'Python':
    print(letter, end=' ')

for letter in reversed('Python'):
    print(letter, end=' ')

#16.5
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i * 10, end=' ')

#16.6
d = int(input())
for i in range(1, 10):
    print(d, '*', i, '=', d*i)