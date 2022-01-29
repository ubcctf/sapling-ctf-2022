from secrets import flag
from Crypto.Util.number import *
from random import randint

flag = bytes_to_long(flag)

print(len(bin(flag)))
def prod(lst):
	p = 1
	for num in lst:
		p *= num
	return p

# Generate a prime number for which p-1 is smooth (except for one factor)
while True:
	factors = prod([randint(0, (1 << 20)) for i in range(16)])
	factors *= getPrime(256)
	if isPrime(factors + 1):
		p = factors + 1
		print(p)
		break


# Also generate a primitive root

from sympy import is_primitive_root
for i in range(1, p):
	if is_primitive_root(i, p):
		print(i)

print(p, g)