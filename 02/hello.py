#!/usr/local/bin/python3
import os

# hello
print('Hello, world!')

# condition
a, b = 0, 1
if a < b:
    print('a ({}) is less than b({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

print('foo' if a < b else 'bar')

# loops
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
print('Done')

c = [1, 3, 4]
for i in c:
    print(i)

current_directory = os.path.dirname(os.path.realpath(__file__))
fh = open(os.path.join(current_directory, 'text.txt'))
for line in fh.readlines():
    print(line, end='')


# function
def is_prime(n):
    if n == 1:
        print('1 is special')
        return False
    for x in range(2, n // 2):
        if n % x == 0:
            print('{} equals {} x {}'.format(n, x, n // x))
            return False
    else:
        print(n, 'is a prime number')
        return True

for m in range(1, 20):
    is_prime(m)


# generator
def primes(primes_n=1):
    while True:
        if is_prime(primes_n):
            yield primes_n
        primes_n += 1

for y in primes():
    if y > 100:
        break
    print(y)
