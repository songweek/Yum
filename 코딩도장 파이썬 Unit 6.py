x=10
print(x)

y='Hello, world!'
print(y)

print(type(x))
print(type(y))

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

a, b = b, a
print(a)
print(b)

d=None
print(d)

e = a + b
print(e)

a+=20
print(a)

f=input('문자열을 입력하세요:')
print(f)

g=int(input('첫 번째 숫자를 입력하세요:'))
h=int(input('두 번째 숫자를 입력하세요:'))
print(g+h)

i, j = input('문자열 두 개를 입력하세요:').split()
print(i)
print(j)

k, l = input('숫자 두 개를 입력하세요:').split()
k=int(k)
l=int(l)
print(k+l)

m, n = map(int, input('숫자 두 개를 입력하세요:').split())
print(m+n)

o, p = map(int, input('숫자 두 개를 콤마로 구분해서 입력하세요:').split(','))
print(o+p)

q, r, s = map(int, input('숫자 세 개를 입력하세요').split())
print(q+r+s)
