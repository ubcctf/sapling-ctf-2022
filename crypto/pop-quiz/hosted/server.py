from Crypto.Util.number import getPrime
from secrets import flag


def challenge1():
	x = getPrime(128)
	modulo = getPrime(64)
	print(f"1. What is the value of {x} modulo {modulo}?")
	user_input = int(input(">>> ").strip())
	assert(user_input == x % modulo)

def challenge2():
	x = getPrime(32)
	y = getPrime(32)
	modulo = getPrime(64)
	print(f"2. Solve for z in the equation: {x} * z == {y} mod {modulo}. (The == means equivalence)")
	user_input = int(input(">>> ").strip())
	assert(x * user_input % modulo == y % modulo)

def challenge3():
	x = getPrime(4)
	exp = getPrime(5)
	result = x ** exp
	print(f"3. What is the value of z in the equation: {x} ^ z = {result}? (The caret [^] refers to exponentiation)")
	user_input = int(input(">>> ").strip())
	assert(user_input == exp)

def challenge4():
	base = getPrime(32)
	exp = getPrime(32)
	modulo = getPrime(64)
	print(f"4. What is the value of {base} ^ {exp} modulo {modulo}?")
	user_input = int(input(">>> ").strip())
	assert(user_input == pow(base, exp, modulo))

def challenge5():
	base = getPrime(16)
	exp = getPrime(20)
	modulo = getPrime(20)
	result = pow(base, exp, modulo)
	print(f"5. What value of z satisfies: {base} ^ z == {result} modulo {modulo}? (You can enter any such z value)")
	user_input = int(input(">>> ").strip())
	# Prevent user from sending an absurdly large value
	if user_input >= (1 << 256):
		raise Exception
	assert(result == pow(base, user_input, modulo))

def challenge6():
	p = getPrime(10)
	q = getPrime(10)
	N = p * q
	print(f"6. What are the two prime factors of {N}? Enter your answer as space-separated numbers with the smallest first. e.g.: `23 35`")
	user_input = input(">>> ").strip()
	assert(user_input == f"{p} {q}" or user_input == f"{q} {p}")

def challenge7():
	p = getPrime(64)
	q = getPrime(64)
	N = p * q
	print(f"7. What are the two prime factors of {N}? Enter your answer as space-separated numbers with the smallest first. e.g.: `23 35`")
	user_input = input(">>> ").strip()
	assert(user_input == f"{p} {q}" or user_input == f"{q} {p}")


challenges = [challenge1, challenge2, challenge3, challenge4, challenge5, challenge6, challenge7]
NUM_CHALLENGES = len(challenges)

START_MESSAGE = f"""
Welcome to the pop quiz! Progress through these {NUM_CHALLENGES} challenges for a special treat.

Here are some useful resources that may help you along the way:
- khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
- brilliant.org/wiki/modular-arithmetic/
- artofproblemsolving.com/wiki/index.php/Modular_arithmetic/Introduction

We'd also recommend Python for working with the large numbers coming up!
"""
if __name__ == "__main__":
	print(START_MESSAGE)
	for i in range(NUM_CHALLENGES):
		# Repeat the challenge until the user responds correctly
		while True:
			try:
				challenges[i]()
				break
			except ValueError:
				print("Please input an integer")
			except AssertionError:
				print("Incorrect answer")
			except Exception:
				print("Something unexpected occured, please try again and let the organizers know")
				exit()
	print(flag)