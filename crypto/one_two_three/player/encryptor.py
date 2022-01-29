from Crypto.Cipher import AES 
import os 

# ======= AES and CTR stuff =======
key = os.urandom(16) # This is 16 bytes of cryptographically random data, there's no way you can bruteforce or guess this
cipher = AES.new(key, AES.MODE_ECB)

# pads the message to a multiple of 16 bytes
def pad(msg):
    bytes_of_padding = (16 - len(msg)) % 16
    pad_bytes = bytes([bytes_of_padding]) # creates a single byte that has the numerical value of the number of bytes of padding you want
                                          # this padding scheme is called PKCS, don't worry about it, just know it pads the message to 16 bytes
    return msg + pad_bytes * bytes_of_padding

def xor(a,b):
    assert len(a) == len(b)
    return bytes([x ^ y for x,y in zip(a,b)])

def encrypt(ptxt):
    # Make the keystream
    keystream = b""
    counter = 1
    while len(keystream) < len(ptxt):
        # Note: this doesn't work if counter ends up greater than 255, don't worry about it, it isn't relevant to the solution
        counter_byte = bytes([counter])
        keystream = keystream + cipher.encrypt(pad(counter_byte))
        counter +=1

    # Do the encryption
    keystream = keystream[:len(ptxt)]
    return xor(ptxt, keystream)

# ======= Challenge stuff =======
secret = open("secret.txt", "r")
out = open("secret.enc", "w")

# Encrypt each line
for line in secret.readlines():
    ptxt = line.encode()
    ctxt = encrypt(ptxt).hex()
    out.write(ctxt + "\n")

out.close()