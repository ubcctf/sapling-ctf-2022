The Cryptographer's Codex vol 4
---

Good job figuring out the last challenge!

You saw that ECB mode has one crucial weakness, each block gets encrypted and decrypted exactly the same way, no matter where it's located in the ciphertext. This led you to be able to move blocks around to wherever you wanted and have the plaintext change in the same way.

So now that we know ECB is bad, how can we circumvent this problem? How can we make our cipher mode not have this problem?

Block chaining
---

Blocks should be encrypted differently based on where they are in the plaintext, so how about we encrypt a block differently based on the previous block?

If we try to move the block like we did with ECB, it'll fail because the previous block will be different, so this seems promising

Let's do it like this
1. Assume we've encrypted the previous block to C_0, and now we want to encrypt plaintext block P_1
2. Let the next ciphertext block be AES(C_0 XOR P_1), basically xor the new plaintext block with the last _ciphertext_ block before encrypting with AES

But then what about the first block? It has no previous block to be XORd against. Well for that we introduce whats called an Initialization Vector, or IV for short. We basically just decide on some 16 bytes of random data, and this ensures each message is unique.

This cipher mode is called Cipher Block Chaining, or CBC for short. Wikipedia has an [excellent diagram](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)) showing how exactly the encryption and decryption for CBC work.


The challenge
---

CBC mode was quite widespread for a long time and lacks any glaring weaknesses like ECB. However it's design leads it to have various pitfalls, one of which you'll need to exploit.

To find weaknesses in older cryptographic methods, it's often useful to look at their successors. For example CBC being ECB's successor makes it evident ECB's weakness in being too deterministic. One successor to CBC mode is Galois/Counter mode, or GCM mode for short.

One main feature that GCM provides is a built in message authentication code, which can basically be thought of as a tag that says "yes this message is exactly what I sent, and has not been modified in any way". In essence it prevents attackers from being able to modify the ciphertext.

Knowing that this is something that CBC lacks, try to solve the challenge!

Tips
---
1. This challenge is structured extremely similarly to cut and paste, so take a look at some of the tips from that challenge. What still applies?
2. Remember the given `client.py` is just a starting point. It's possible you'll need to make modifications to it in order to return some information that it's just printing right now
3. Remember that the AES key will be different each time you connect to the server, you have to do everything in one connection
4. The code to solve this challenge is very short (you could probably golf it down to one or two lines), the difficulty lies in realizing what kind of manipulations you can make to the ciphertext. Once you realize the trick, you'll see that you have a lot of power over the resulting plaintext
5. Stare at the wikipedia diagram for CBC. Stare at it the entire time while writing your solution. Trust me, it'll help