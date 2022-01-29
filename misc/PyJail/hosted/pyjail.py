def main():
    print("====================== *Welcome to PyJail* ======================")
    print("Author: Vie")
    print("There's a file in here with the flag you want. See if you can get it.")
    userinput = input('>> ')
    blacklist = ['eval', 'exec', 'rm', 'kill', '+']
    for illegal in blacklist:
        if illegal in userinput.lower():
            raise Exception()
    else:
        exec(userinput)
if __name__ == "__main__":
    main()