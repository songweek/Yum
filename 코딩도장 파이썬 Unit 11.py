a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a)
print(100 in a)
print(100 not in a)
print(30 not in a)

print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('P' in 'Hello, Python')

b = [0, 10, 20, 30]
c = [9, 8,7,6]
print(b+c)

print(list(range(0, 10))+ list(range(10, 20)))
print(tuple(range(0, 10))+ tuple(range(10, 20)))

print('Hello, ' + 'world!')

print([0, 10, 20, 30] * 3)

print(list(range(0, 5, 2)) * 3)
print(tuple(range(0, 5, 2)) * 3)
print('Hello' * 3)

print(len(a))
print(len(range(0, 10, 2)))

hello = 'Hello, world!'
print(len(hello))

print(a[0])
print(a[2])
print(a[4])

d = range(0, 12, 2)
print(d[2])

print(hello[7])

print(a[-1])
print(a[-5])
print(d[-3])
print(hello[-4])

print(a[len(a)-1])

del a[2]
print(a)

print(a[0:4])
print(a[4:-1])
print(a[2:8:3])
print(a[:6])
print(a[6:])
print(a[:6:2])
print(a[6::2])

print(a[0:len(a)])

r = range(10)
print(r[4:7])
print(r[4:])
print(r[:7:2])
print(list(r[:7:2]))

hello = 'Hello, world!'
print(hello[2:9])
print(hello[:9:2])

a[2:5] = ['a', 'b', 'c']
print(a)
del a[2:5]
print(a)

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])