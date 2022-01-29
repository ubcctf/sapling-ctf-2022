from hashlib import sha256
from Crypto.Util.number import long_to_bytes
from os import urandom
import time
import scrypt

##################################
#       Setup Sample Server      #
##################################

flag = b'maple{s!d3_ch@nn3l_a77@ck5}'

# Convert the flag (in bytes) to bits
bits = ''.join([bin(c)[2:].zfill(8) for c in flag])

# Return an encrypted string based on the bit at a certain index
def encrypt(index):
	assert(0 <= index < len(bits))

	# Generate a random salt for the given index
	salt = urandom(32)

	# Depending on the bit value, hash the flag differently
	if bits[index] == '0':
		encrypted = scrypt.hash(flag, salt, 2 ** 14).hex()
	else:
		encrypted = sha256(flag + salt).hexdigest()

	return encrypted[:32]


##################################
#      Start Solve Script        #
##################################

# The exploit relies on a side channel attack, since the scrypt hash takes significantly more time due to the high
# CPU/memory cost parameter (2 ^ 16)

idx = 0
# This threshold value determines whether the bit is 1 or 0; play around with this to find a balance between scrypt and sha256
threshold = 0.1
ans = ''

while True:
	try:
		# Repeat the timed measurements for each bit a few times to ensure accuracy
		start_time = time.time()
		for i in range(5):
			encrypt(idx)
		time_elapsed = time.time() - start_time

		if time_elapsed > threshold:
			ans += '0'
		else:
			ans += '1'

		idx += 1
	except Exception:
		break

print(long_to_bytes(int(ans, 2)))
