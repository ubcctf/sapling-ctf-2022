import string

def xor(a, b):
    pairs = zip(a,b)
    return bytes([x ^ y for (x,y) in pairs])

def get_score(c):
    c = chr(c)
    if c in string.ascii_letters:
        return 1
    elif c == " ": 
        return 0.75
    elif c in string.punctuation or c in string.digits:
        return 0.5
    else:
        return -1

# def get_score(c):
#     character_frequencies = {
# 	'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
# 	'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
# 	'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
# 	'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
# 	'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
# 	'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
# 	'y': .01974, 'z': .00074, ' ': .13000
# 	}
#     return character_frequencies.get(chr(c).lower(), 0)

def break_col(col_bytes, do_print=False):
    # each element in this list is an english character xor'd with a byte so bruteforce it
    best_score = -1
    key = None

    for guess in range(255):
        xord = bytes([x ^ guess for x in col_bytes])
        score = sum([get_score(c) for c in xord])
        if score > best_score:
            best_score = score
            key = guess

        if do_print:
            print(">", xord, score, best_score)
    return bytes([key])

# def solve():
#     lines = open("secret.enc").readlines()

#     # convert everything to bytes
#     lines = [bytes.fromhex(line.strip()) for line in lines]

#     # get the length we're working with
#     l = min([len(line) for line in lines])

#     print(f"Length = {l}")

#     # truncate everything to that length
#     lines = [line[:l] for line in lines]

#     # transpose
#     columns = [[line[i] for line in lines] for i in range(l)]

#     keystream = b""
#     for col in columns:
#         keystream += break_col(col)

#     for line in lines:
#         print(xor(keystream, line))

def solve_full():
    lines = open("secret.enc").readlines()

    # convert everything to bytes
    lines = [bytes.fromhex(line.strip()) for line in lines]

    columns = []
    # i = column number, ranges from 0...max(line_lengths)
    for i in range(max([len(line) for line in lines])):
        # transpose
        col = []
        for line in lines:
            # as long as the line is longer than i
            if len(line) > i:
                col.append(line[i])
        columns.append(col)

    # break_col(columns[1], True)

    keystream = b""
    for col in columns:
        keystream += break_col(col)

    with open("res.txt","wb") as f:
        for line in lines:
            x = xor(keystream, line)
            print(x)
            f.write(x)



if __name__ == "__main__":
    # print("--- Playing it safe ---")
    # solve()
    print("--- Trying to do the full thing ---")
    solve_full()