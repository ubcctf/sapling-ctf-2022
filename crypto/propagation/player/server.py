from Crypto.Cipher import AES 
import os 
import traceback 

# ======= AES and CBC stuff =======
key = os.urandom(16) # This is 16 bytes of cryptographically random data, there's no way you can bruteforce or guess this
cipher = AES.new(key, AES.MODE_ECB) # This says ECB mode, but we'll never encrypt more than 16 bytes at a time, so this is just AES with no mode

# pads the message to a multiple of 16 bytes
def pad(msg):
    bytes_of_padding = (16 - len(msg)) % 16
    pad_bytes = bytes([bytes_of_padding]) # creates a single byte that has the numerical value of the number of bytes of padding you want
                                          # this padding scheme is called PKCS, don't worry about it, just know it pads the message to 16 bytes
    return msg + pad_bytes * bytes_of_padding

# strip the padding off
# don't worry about this function
def strip_padding(block):
    last = block[-1]
    if last < 16 and all([last == b for b in block[-1 * last:]]):
        # we have a padded msg, strip it off
        return block[:-1*last]
    else:
        # no padding
        return block

# splits the message into 16 byte chunks
# msg must be a multiple of 16 bytes long
def blockify(msg):
    blocks = []
    for i in range(0,len(msg),16):
        blocks.append(msg[i:i+16])
    return blocks

def xor(a,b):
    assert len(a) == len(b)
    return bytes([x ^ y for x,y in zip(a,b)])

def encrypt(ptxt):
    iv = os.urandom(16)
    print(f"[+] Generating IV {iv.hex()}")

    print(f"[+] Encrypting {ptxt}")

    msg = pad(ptxt)
    print(f"[+] Padded the message out to {msg}")

    blocks = blockify(msg)
    print(f"[+] Splitting into blocks for CBC")
    for i,block in enumerate(blocks):
        print(f"[+] Block #{i+1}: {block}")

    result = b""
    last = iv 
    for block in blocks:
        next = cipher.encrypt(xor(last, block))
        result = result + next
        last = next
    return result, iv

def decrypt(ctxt, iv):
    ctxt_blocks = blockify(ctxt)
    ptxt_blocks = []
    last = iv
    for block in ctxt_blocks:
        intermediate = cipher.decrypt(block)
        ptxt_blocks.append(xor(last, intermediate))
        last = block
    ptxt_blocks[-1] = strip_padding(ptxt_blocks[-1])

    print(f"[+] Decryption results:")
    for i,block in enumerate(ptxt_blocks):
        print(f"[+] Block #{i+1}: {block.hex()}, {block}")

    result = b"".join(ptxt_blocks)
    return result

# ======= Challenge stuff =======
def contains_invalid(s):
    return ("," in s) or (":" in s) or ("admin" in s)

def register_user():
    user = input("Input your username: ")
    passwd = input("Input your password: ")

    if contains_invalid(user) or contains_invalid(passwd):
        print(f"I'm afraid I can't let you do that! `{user}` or `{passwd}` contains in invalid character")
        return

    print(f"Creating user with username: `{user}` and password: `{passwd}`")
    token = f"user:{user},admin:false,passwd:{passwd}" # No one is an admin except for me!

    ctxt, iv = encrypt(token.encode())
    print(f"Here's your token! Use this to login when we add the login feature: {ctxt.hex()},{iv.hex()}")

def admin_login():
    token_hex = input("Input your token: ")
    ctxt_hex, iv_hex = token_hex.split(",")

    token = bytes.fromhex(ctxt_hex.strip())
    iv = bytes.fromhex(iv_hex.strip())

    userdata = decrypt(token, iv)
    data = {}
    try:
        kv_pairs = userdata.split(b",")
        for kv in kv_pairs:
            key, value = kv.split(b":")
            data[key] = value

        if data[b"admin"] == b"true":
            f = open("flag.txt", "r")
            print(f"Flag! {f.read()}")
        else:
            print(f"Wait a minute! You aren't admin! Your token is {userdata}")
    except Exception as e:
        print(f"Oh no something has gone wrong")
        traceback.print_exc()

menu = """Welcome to Super CBC Land! The slightly more cryptographically secure social media platform for the discerning cryptographer
Options:
[1] Register a new user
[2] Administrator login (For admins only!)
"""
if __name__ == "__main__":
    while True:
        print(menu)
        inp = input("> ")
        if inp == "1":
            register_user()
        elif inp == "2":
            admin_login()
        else:
            print(f"Invalid option `{inp}`")