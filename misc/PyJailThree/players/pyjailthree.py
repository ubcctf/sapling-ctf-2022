def main():
    print("====================== *Welcome to PyJail 3: The Threequel.* ======================")
    print("Author: Vie")
    print("The flag file is in a file called flag.txt!")
    print("Inputs over 50 chars are banned. GL!")
    userinput = input('>> ')

    if len(userinput) > 50:
        raise Exception()
    
    blacklist = ['eval', 'exec', 'import', 'os', '=', 'txt', 'read', 'dict', ';', ':', '\n', 'flag', 'subprocess', 'write', 'input', '_', 'getattr', 'globals', 'update']
    for illegal in blacklist:
        if illegal in userinput.lower():
            print("Illegal Char: " + illegal)
            print("Goodbye :)")
            raise Exception()
    else:
        exec(userinput)
if __name__ == "__main__":
    main()
