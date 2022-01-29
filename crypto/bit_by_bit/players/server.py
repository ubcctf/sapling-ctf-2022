from secrets import flag
from hashlib import sha256
from os import urandom
import scrypt

# Convert the flag (in bytes) to bits
bits = ''.join([bin(c)[2:].zfill(8) for c in flag])

# Return an encrypted string based on the bit at a certain index
def encrypt(index):
	assert(0 <= index < len(bits))

	# Generate a random salt for the given index
	salt = urandom(32)

	# Depending on the bit value, hash the flag differently
	if bits[index] == '0':
		encrypted = scrypt.hash(flag, salt, 2 ** 16).hex()
	else:
		encrypted = sha256(flag + salt).hexdigest()

	return encrypted[:32]


if __name__ == "__main__":
	while True:
		try:
			print("Which bit would you like to query for?")
			bit_index = int(input(">>> "))
			print(encrypt(bit_index))
		except Exception:
			print("Something unexpected happened, please try again!")