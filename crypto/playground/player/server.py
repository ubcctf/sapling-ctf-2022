from baby_aes import f
from secret import flag 

def xor(a,b):
    assert len(a) == len(b)
    return bytes([x ^ y for x,y in zip(a,b)])

def lh(xs):
    return xs[:16]

def rh(xs):
    return xs[16:]

def round(xs):
    l = lh(xs)
    r = rh(xs)
    return r + xor(l, f(r))

def encrypt(ptxt):
    assert len(ptxt) == 32

    ctxt = ptxt
    for _ in range(16): 
        # round and round it goes
        ctxt = round(ctxt)
    return ctxt

enc_flag = encrypt(flag)

menu = """I modified AES to make it more old school, give it a try. Encrypt 32 bytes of your choice"""
def main():
    print("Encrypted flag: ", enc_flag.hex())
    while True:
        print(menu)
        hex = input("> (hex) ")
        ptxt = bytes.fromhex(hex)
        if len(ptxt) != 32:
            print("I said 32 bytes!")
        else:
            print(encrypt(ptxt).hex())


if __name__ == "__main__":
    main()