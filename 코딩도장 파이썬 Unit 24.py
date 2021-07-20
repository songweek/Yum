#24.1
print('Hello, world!'.replace('world', 'Python'))

a = 'Hello, world!'
a = a.replace('world!', 'Python')
print(a)

table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

print('apple pear grape pineapple orange'.split())

print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

print('python'.upper())

print('PYTHON'.lower())

print('   Python   '.lstrip())

print('   Python   '.rstrip())

print('   Python   '.strip())

print(', python.'.lstrip(',.'))

print(', python.'.rstrip(',.'))

print(', python.'.strip(',.'))

print('python'.ljust(10))

print('python'.rjust(10))

print('python'.center(10))

print('python'.rjust(10).upper())

print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

print('apple pineapple'.find('pl'))

print('apple pineapple'.rfind('pl'))

print('apple pineapple'.index('pl'))

print('apple pineapple'.rindex('pl'))

print('apple pineapple'.count('pl'))

#24.2
print('I am %s.' % 'james')

name = 'maria'
print('I am %s.' % name)

print('%f' % 2.3)
print('%10s' % 'python')

print('%-10s' % 'python')

print('Today is %d %s.' % (3, 'April'))

print('Hello, {0}'.format('world!'))

print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))

print('{0} {0} {1} {1}'.format('Python', 'Script'))

print('Hello, {} {} {}'.format('Python', 'Script', 3.6))

print('Hello, {language} {version}'.format(language='Python', version=3.6))

language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

print('{0:>10}'.format('python'))

print('{:>10}'.format('python'))

print('%03d' % 1)
print('{0:03d}'.format(35))

print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))

print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))

print('{0:0>10.2f}'.format(15))

print('{0: >10}'.format(15))
print('{0:>10}'.format(15))
print('{0:x>10}'.format(15))
