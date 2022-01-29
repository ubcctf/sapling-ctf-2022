# https://en.wikipedia.org/wiki/RSA_(cryptosystem)
from secrets import flag
from Crypto.Util.number import bytes_to_long, getPrime, inverse

p = getPrime(40)
q = getPrime(40)

# Why use a 2048 bit modulus when we can go with something much smaller?
N = p * q
e = 65537

# Now we can encrypt our message!
msg = bytes_to_long(flag)
ciphertext = pow(msg, e, N)

# Make sure the msg fits within the modulus
assert(msg < 2 ** 80)

# Double-check that our decryption process works
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
assert(msg == pow(ciphertext, d, N))

print('Here you go!')
print(f'N: {N}')
print(f'e: {e}')
print(f'ciphertext: {ciphertext}')