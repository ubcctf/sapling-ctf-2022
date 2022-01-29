import client 

def blockify(msg):
    blocks = []
    for i in range(0,len(msg),16):
        blocks.append(msg[i:i+16])
    return blocks

cut_from = client.register_user("aaaaaaa","true").decode()
target = client.register_user("aaaa", "bbbbbbbbbbb").decode()


cut_blocks = blockify(bytes.fromhex(cut_from))
target_blocks = blockify(bytes.fromhex(target))

res = target_blocks[0] + cut_blocks[2]

client.admin_login(res.hex())

"""
[+] Opening connection to localhost on port 1337: Done
[Client] Registering user: aaaaaaa | passwd: true
 Creating user with username: `aaaaaaa` and password: `true`
[+] Encrpyting b'user:aaaaaaa,admin:false,passwd:true'
[+] Padded the message out to b'user:aaaaaaa,admin:false,passwd:true\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
[+] Splitting into blocks for ECB
[+] Block #1: b'user:aaaaaaa,adm'
[+] Block #2: b'in:false,passwd:'
[+] Block #3: b'true\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
[Client] Registering user: aaaa | passwd: bbbbbbbbbbb
 Creating user with username: `aaaa` and password: `bbbbbbbbbbb`
[+] Encrpyting b'user:aaaa,admin:false,passwd:bbbbbbbbbbb'
[+] Padded the message out to b'user:aaaa,admin:false,passwd:bbbbbbbbbbb\x08\x08\x08\x08\x08\x08\x08\x08'
[+] Splitting into blocks for ECB
[+] Block #1: b'user:aaaa,admin:'
[+] Block #2: b'false,passwd:bbb'
[+] Block #3: b'bbbbbbbb\x08\x08\x08\x08\x08\x08\x08\x08'
[Client] Attempting login
b'Flag! temp flag \n'
"""