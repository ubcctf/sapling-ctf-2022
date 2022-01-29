from Crypto.Util.number import *
from math import gcd

##################################
#       Setup Sample Server      #
##################################

flag = b"maple{d0nt_f0rg37_t0_h@sh!!}"

def encrypt(msg):
	return pow(msg, e, N)

def decrypt(msg):
	return pow(msg, d, N)

flag = bytes_to_long(flag)
p = getPrime(512)
q = getPrime(512)
N = p * q
e = 65537

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

encrypted_flag = encrypt(flag)
assert(decrypt(encrypted_flag) == flag)


##################################
#      Start Solve Script        #
##################################


# Query for the encrypted flag:
enc_flag = encrypted_flag
e = 65537

print(2 * enc_flag)
'''
We can find the modulus, N, by encrypting a few random messages (m1, m2, ..)
In this case, c1 == m1^e (mod N), c2 == m2^e (mod N), c3 == m3^e (mod N)

Rearranging each equation leads to: m1^e - c1 == m2^e - c2 == m3^e - c3 == 0 (mod N)
Since each of these expressions are multiples of N, the GCD will also be N if we query enough times
'''

m_1234 = encrypt(1234)
m_9876 = encrypt(9876)
m_111111 = encrypt(111111)

N = gcd(1234 ** e - m_1234, 9876 ** e - m_9876, 111111 ** e - m_111111)

'''
Unfortunately, naively factoring N won't work well (because it's quite large at 1024 bits)
However, consider what happens when we ask the oracle to decrypt (2 * enc_flag):
- Returns (2 * enc_flag) ^ d == (2 ^ d) * (enc_flag ^ d) == (2 ^ d) * flag (mod N)
- We can find (2 ^ d) by asking the oracle to decrypt 2!
'''

dec_2flag = decrypt(2 * enc_flag)
dec_2 = decrypt(2)

flag = dec_2flag * inverse(dec_2, N) % N

print(long_to_bytes(flag))