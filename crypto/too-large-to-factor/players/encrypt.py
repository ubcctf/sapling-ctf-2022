# https://en.wikipedia.org/wiki/RSA_(cryptosystem)
from secrets import flag
from Crypto.Util.number import bytes_to_long, getPrime, inverse

p = getPrime(512)
q = getPrime(512)
# This time, I've made sure the modulus is unfactorable!
N = p * q
e = 3

msg = bytes_to_long(flag)
ciphertext = pow(msg, e, N)

# What could go wrong with a smaller message?
assert(msg < (1 << 256))

# Double-check that our decryption process works
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
assert(msg == pow(ciphertext, d, N))

print('Good luck factoring my modulus!')
print(f'N: {N}')
print(f'e: {e}')
print(f'ciphertext: {ciphertext}')