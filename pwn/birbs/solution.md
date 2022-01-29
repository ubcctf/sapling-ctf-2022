The bug here is a classic buffer overflow with `read()` being to able take in more bytes than what is allocated to the buffer. However, there is a stack canary that will crash the program if it detects a stack smashing attempt. It is not possible to naively bruteforce a 8 byte canary.
However, the buffer overflow in this challenge is in a forked process. A process that is spawned using `fork()` inherits the exact state of the process is was forked from which includes the stack canary.

Therefore, the exploit is to get the proces to keep forking and bruteforce the canary byte by byte. Specifically, you can fork the process and change the lowest byte of the canary. If you guessed right then the forked process won't crash and you now know one byte of the canary and can move onto the next byte. If you guessed wrong then the forked process will crash and you can just fork the process again and change your guess.
Doing this 256 times for each byte guarantees that you will know what the correct byte is. Repeat this for all 8 bytes and you now know the entire canary in a maximum of 256*8 guesses.

Here is a more detailed description: https://ctf101.org/binary-exploitation/stack-canaries/
