# Thanks copilot!
def encrypt(file, key):
    f = open(file, "r")
    f_out =open(file + ".enc", "w")
    for line in f:
        for c in line:
            f_out.write(chr(ord(c) ^ key))

    f.close()
    f_out.close()

key = ???
assert 0 < key < 255
encrypt("flag.txt", key)