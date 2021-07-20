#22.1
a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

b = [10, 20, 30]
b.append([500, 600])
print(b)
print(len(b))

c = [10, 20, 30]
c.extend([500, 600])
print(c)
print(len(c))

d = [10, 20, 30]
d.insert(2, 500)
print(d)
print(len(d))

e = [10, 20, 30]
e.pop()
print(e)

f = [10, 20, 30]
f.remove(20)
print(f)

g = [10, 20, 30, 15, 20, 40]
print(g.index(20))

h = [10, 20, 30, 15, 20, 40]
print(h.count(20))

#22.2
i = [0, 0, 0, 0, 0]
j = i
print(i is j)
j[2] = 99
print(i)
print(j)

k = [0, 0, 0, 0, 0]
l = a.copy()
print(k is l)
print(k == l)
k[2] = 99
print(k)
print(l)

#22.3
m = [38, 21, 53, 62, 19]
for i in m:
    print(i)

n = [38, 21, 53, 62, 19]
for index, value in enumerate(n):
    print(index, value)

o = [38, 21, 53, 62, 19]
i = 0
while i < len(o):
    print(o[i])
    i += 1

#22.4
p = [38, 21, 53, 62, 19]
smallest = p[0]
for i in p:
    if i < smallest:
        smallest = i
print(smallest)

largest = p[0]
for i in p:
    if i > largest:
        largest = i
print(largest)

print(min(o))
print(max(o))

print(sum(o))

#22.5
q = [i for i in range(10)]
print(q)

r = list(i for i in range(10))
print(r)

s = [i for i in range(10) if i % 2 == 0]
print(s)

t = [i + 5 for i in range(10) if i % 2 == 1]
print(t)

u = [i * j for j in range(2, 10) for i in range(1, 10)]
print(u)

#22.6
v = [1.2, 2.5, 3.7, 4.6]
for i in range(len(v)):
    v[i] = int(v[i])
print(v)

a = list(map(int, a))
print(v)

w = list(map(str, range(10)))
print(w)

x = map(int, input().split())
print(x)
print(list(x))

#22.7
z = (38, 21, 53, 62, 19)
for i in z:
    print(i, end=' ')

aa = tuple(i for i in range(10) if i % 2 == 0)
print(aa)

v = tuple(map(int, v))
print(v)

ab = (38, 21, 53, 62, 19)
print(min(ab))
print(max(ab))
print(sum(ab))

