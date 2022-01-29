import solve_client
import client 

def blockify(msg):
    blocks = []
    for i in range(0,len(msg),16):
        blocks.append(msg[i:i+16])
    return blocks

def xor(a,b):
    assert len(a) == len(b)
    return bytes([x ^ y for x,y in zip(a,b)])

# test both methods to make sure they both work, since method 1 caused some strange errors

# method 1
ctxt,iv = solve_client.register_user("a"*11 + "b"*16, "bb")

c_blocks = blockify(bytes.fromhex(ctxt))

# i overthought my own challenge lul, you can just xor the block, you don't need the intermediate at all
# oops... w/e

zeroed = c_blocks[0] + b"\x00"*16 + c_blocks[2] + c_blocks[3]
intermediate = solve_client.admin_login(zeroed.hex(), iv)

goal = b",admin:true,aaaa"
frankenstein = c_blocks[0] + xor(goal, intermediate) + c_blocks[2] + c_blocks[3]

solve_client.admin_login(frankenstein.hex(), iv, flag=True)

# method 2
# wait this is way smarter
ctxt,iv = client.register_user("a", "bb")
iv_b = bytes.fromhex(iv)
modified_iv = xor(iv_b, xor(b"user:a,admin:fal", b"admin:true,user:")) 
# no corruption of the token at all, other than the order
# which is pretty slick if i do say so myself

client.admin_login(ctxt,modified_iv.hex())