from Crypto.Util.number import long_to_bytes, inverse

N = 640203263008444282715761
e = 65537
ciphertext = 400260416204680499515181

# We can use an online factorization calculator (https://www.alpertron.com.ar/ECM.HTM) 
# Or mathematical software like SageMath to factor N

p = 773368062113
q = 827811871697
assert(p * q == N)

# Decrypt the message knowing p and q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

msg = pow(ciphertext, d, N)
print(f'Flag: {long_to_bytes(msg)}')