from math import log

# 1. What is the value of 329034532716710968771208485406976739079 modulo 17085842661946158097?
# Solution: The Python % operator acts as a modulo
ans1 = 329034532716710968771208485406976739079 % 17085842661946158097


# 2. Solve for z in the equation: 3237837517 * z == 2394524491 mod 17421128176367171563. (The == means equivalence)
# Solution: Rearranging => z == 2394524491 * (3237837517 ^ -1) mod 17421128176367171563
ans2 = 2394524491 * pow(3237837517, -1, 17421128176367171563) % 17421128176367171563


# 3. What is the value of z in the equation: 11 ^ z = 1586309297171491574414436704891? (The caret [^] refers to exponentiation)
# Solution: taking the logarithm of both sides => z = log(1586309297171491574414436704891)/log(11) 
ans3 = log(1586309297171491574414436704891, 11)


# 4. What is the value of 2863028743 ^ 2638768129 modulo 17831142954628788713?
# Solution: pow(a, b, c) in Python computes a ^ b % c
ans4 = pow(2863028743, 2638768129, 17831142954628788713)


# 5. What value of z satisfies: 56237 ^ z == 264266 modulo 975463? (You can enter any such z value)
# Solution: this problem is known as the Discrete Logarithm Problem (DLP), solveable in O(sqrt(p)) where p is the modulus
# In our case, the modulus is small enough to naively brute force values of z

product = 1
for z in range(1, 975463):
	product = 56237 * product % 975463
	if product == 264266:
		ans5 = z
		assert(pow(56237, z, 975463) == 264266)


# 6. What are the two prime factors of 373601? Enter your answer as space-separated numbers with the smallest first. e.g.: `23 35`
# Solution: the given number is small enough for us to brute force the factors one-by-one (of course, faster algorithms exist)

for p in range(2, 373601):
	if 373601 % p == 0:
		ans6 = (p, 373601 // p)


# 7. What are the two prime factors of 159364191653405770958379657249324008461? Enter your answer as space-separated numbers with the smallest first. e.g.: `23 35`
# Solution: there are more efficient algorithms for factorization, such as the General Number Field Sieve (GNFS) and Elliptic-Curve Factorization Method (ECM)
# Luckily, plenty of implementations are available online; one example is SageMath's '`factor` function
# Running `factor(159364191653405770958379657249324008461)` at sagecell.sagemath.org gives:

ans7 = (12578394223858637857, 12669676972846385773)

