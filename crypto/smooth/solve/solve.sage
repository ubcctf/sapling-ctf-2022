from Crypto.Util.number import *

##################################
#       Setup Sample Server      #
##################################

server_p = 2456782130957560538732891151621405971959468408409472151708813573713505247007699846687090593175995160728058115325345265255647291297676410001590971878318349418496000001
server_g = 38
server_flag = b'maple{sm00th_3n0ugh_t0_f!nd_th3_dl0g!!}'

server_flag = bytes_to_long(server_flag)

def encrypt(msg):
	return hex(pow(server_g, msg, server_p))[2:]

encrypted_flag = encrypt(server_flag)


##################################
#      Start Solve Script        #
##################################


# By encrypting a few messages, we can notice that the server raises 38 to the power of the given number (in hexadecimal)
# Additionally, the result is reduced modulo p for some modulus p.
# To start off, we can find this value p by querying a few times and taking the gcd – for more detail, see the Blindfolded challenge

msg1 = int('a3aa', 16)
msg2 = int('bb4b', 16)
msg3 = int('c9cc', 16)

g = 38
p = gcd(g ** msg1 - int(encrypt(msg1), 16), gcd(g ** msg2 - int(encrypt(msg2), 16), g ** msg3 - int(encrypt(msg3), 16)))

# We can see that the modulus p is prime
assert(isPrime(p))
print(len(bin(p))) # And contains ~550 bits

# To find the flag, we need to solve the equation:
# 3 ^ (flag) == enc (mod p)
# This is commonly known as the Discrete Logarithm Problem (DLP), and even the fastest algorithms run in worst case O(sqrt(p))
# Luckily for us, the challenge hints that p-1 is a smooth number, meaning it can be factored into many smaller primes
# To check this, we can use the built in SageMath factor function:

factors = list(factor(p - 1))
order = p - 1
print(factors) # [(2, 16), (3, 4), (5, 1), (7, 3), (11, 7), (13, 2), (17, 2), (19, 1), (41, 2), (47, 1), (89, 2), (181, 1), (199, 1), (227, 1), (281, 1), (331, 1), (367, 1), (457, 1), (1061, 1), (3701, 1), (22093, 1), (22573, 1), (22619, 1), (109897, 1), (121553, 1), (448139, 1), (656483, 1), (63020029654362306988583926315241749354212099370495256102253805999408482331481, 1)]


# Now, we can apply the Pohlig Hellman algorithm that solves the DLP for each of these subgroups, then combine the result at the end
# Since the last prime is 256 bits, we have to skip over it

# We're solving the equation g ^ x == q (mod p)

q = int(encrypted_flag, 16)
remainders = []
moduli = []

for i, j in factors[:-1]:
	mod = i ** j
	g2 = pow(g, order // mod, p)
	q2 = pow(q, order // mod, p)

	rem = discrete_log(q2,g2,operation="*")
	remainders.append(rem)
	moduli.append(mod)

def product(lst):
	prod = 1
	for c in lst:
		prod *= c
	return prod

partial_flag = crt(remainders, moduli)
modulus = product(moduli)

# Thus, we know that x == partial_flag (modulus)
# Note that the modulus is 302 bits and the flag is 313 bits – so we can brute force the remaining few bits

x = partial_flag
while True:
	print(len(bin(x)))
	if b'maple' in long_to_bytes(x):
		print(long_to_bytes(x))
		break
	x += modulus
