#23.1
a = [[10, 20], [30, 40], [50, 60]]
print(a)
print(a[0][0])
a[0][1] = 1000
print(a[0][1])
print(a[1][1])
print(a[2][1])

#23.2
for x, y in a:
    print(x, y)

for i in a:
    for j in i:
        print(j, end=' ')
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()


i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1

    i = 0

while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1

#23.3
b = []
 
for i in range(10):
    b.append(0)
 
print(b)

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    b.append(line) 
print(b)

c = [[0 for j in range(2)] for i in range(3)]
print(c)

d = [[0] * 2 for i in range(3)]
print(d)

e = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
f = []    # 빈 리스트 생성
 
for i in e:
    line = []
    for j in range(i):
        line.append(0)
    f.append(line)
print(f)

#23.4
g = [[10, 20], [30, 40]]
h = g
h[0][0] = 500
print(g)
print(h)

j = [[10, 20], [30, 40]]
i = h.copy()
i[0][0] = 500
print(i)
print(j)

k = [[10, 20], [30, 40]]
import copy
l = copy.deepcopy(k)
l[0][0] = 500
print(k)
print(l)


