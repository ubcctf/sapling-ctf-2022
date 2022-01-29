from Crypto.Util.number import *
from secrets import *

flag = bytes_to_long(flag)

def encrypt(msg):
	return hex(pow(g, msg, p))[2:]

encrypted_flag = encrypt(flag)

if __name__ == "__main__":
	while True:
		try:
			print("""Options:\n1) Encrypt a (hex) message\n2) Get the encrypted flag\n3) Get the size of the original flag (in bits)""")
			option = int(input(">>> "))
			if option == 1:
				msg = int(input(">>> "), 16)
				assert(msg < (1 << 1024))
				print(encrypt(msg))
			elif option == 2:
				print(encrypted_flag)
			elif option == 3:
				print(len(bin(flag)) - 2)
		except Exception:
			print("Something unexpected happened, please try again!")