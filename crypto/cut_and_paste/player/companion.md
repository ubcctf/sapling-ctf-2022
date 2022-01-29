The Cryptographer's Codex vol 2
---

Welcome to challenge 2, where we'll be jumping straight into a modern encryption algorithm! Now you may think that just because this is a real encryption algorithm that Zoom really did use in their software that this challenge is going to be hard to solve.

But that isn't the case! Cryptography can often times be mathematically unbreakable, but present many flaws and pitfalls when brought to the real world.

So let's take a look at how that can happen

How does modern encryption work?
---

What do you do when you want to make a message secret? The most common solutions use something that's called a _block cipher_.

What is a block cipher? It's a function that takes 16 bytes and a key, and encrypts it. The standard block cipher, AES, is extremely extremely good at doing this. It's been analyzed and tested to hell and back and no one has been able to break it. How it works is a bit complicated so you don't need to worry about it.

As a quick example. With the key "catscatscatscats"
- The encryption of "mymessageiscool!" is 7560e6979e56348cfe27616e0ca8567b
- The encryption of "mymessageiscool?" is 59acdc0dbe8c2432c673bb05c2034c62
- See how the results are completely different even though the inputs are very similar? That's a security feature of AES!
- AES is secure in that if I gave you just "7560e6979e56348cfe27616e0ca8567b", you would have no idea what my original message was without the key. But if you had the key, you can recover the original message just by running the decryption algorithm

You might be wondering, if we have this perfect block encryption function, how could we possibly try to break any encryption? Didn't you say AES is unbreakable (1)?

Well let me ask you, you have this function that encrypts 16 bytes exactly, how do you encrypt more? How do you, for example, encrypt 100 bytes?

Block cipher modes
---
Block cipher modes are what allows you to do variable size encryption. Let's consider the most simple block cipher mode

Here's how you encrypt a variable number of bytes
1. Add bytes to the end of the message in a special format so you know that you should remove it later
2. Keep adding bytes until the message is a multiple of 16, this is called "padding"
3. Split it into a bunch of 16 byte messages and encrypt them all
4. Append it all together, and send it off

This is called Electronic Code Book, or ECB mode for short. It has a few glaring weaknesses, which you'll have to discover to solve the challenge!

Some tips
---
1. Open up `ecb_testing.html` and play around with it, it gives a simple UI for visualizing blocks of a message and the resulting blocks of the plaintext
    - What happens when you edit half of a ciphertext? What does it decrypt to? What if you edit more/less of a block?
    - What happens if you change the order of blocks?
2. What exactly do you have to do to get the flag? What do you need to trick the server into thinking?
3. Look at the challenge title! CTF challenges often hide little hints in the challenge titles
4. In CTF challenges you should be constantly thinking about what you have control over, and how you can abuse this control. In this setup you have three things you can control
    - The username and password you send when you register a user
    - The bytes you send to the server when it asks for a token
5. What happens if your token is incomplete? Will the server accept it? How badly can you mangle your token and still have the server be ok with it?
6. The server uses `input()` to get your username and password, so you're limited to normal alphanumeric and punctuation characters, you can't input arbitrary bytes in there. How can you work around this?

What can you do with this? How can you trick the server into encrypting something that you can use?

(1) Here's hoping anyway