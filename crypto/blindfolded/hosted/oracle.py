from Crypto.Util.number import getPrime, bytes_to_long, inverse
from secrets import flag

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

# Check that decryption works properly
assert(decrypt(encrypted_flag) == flag)

if __name__ == "__main__":
	while True:
		try:
			print("""Here are your options:\n1) Encrypt a message\n2) Decrypt a message\n3) Get the encrypted flag""")
			option = int(input(">>> "))
			if option == 1:
				msg = int(input(">>> "))
				print(encrypt(msg))
			elif option == 2:
				msg = int(input(">>> "))
				if msg == encrypted_flag:
					print("No cheating!")
				else:
					print(decrypt(msg))
			elif option == 3:
				print(encrypted_flag)
		except ValueError:
			print("Something unexpected happened, please try again!")