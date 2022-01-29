# make sure everything here is either pretty simple or mentioned in the companion
# this challenge is just to get people up to speed with this stuff anyway

f = open("flag.txt.enc", "r")
lines = f.readlines()

for guess in range(256):
    res = ""
    for line in lines:
        for c in line:
            res += chr(ord(c) ^ guess)
    print(guess, res)