# Rotating Tree

Password checker that looks for each character in a tree that rotates each key to the root, 
then verifies password by verifying structure of tree is the same.

## Simple version

Alphabet is dumped into the tree, then structure of the tree is checked every time a char
of the password is inserted one at a time (structure guarantees solution is unique)

### Solution

Brute forcing character by character works, simple_solve.py`illustrates this, alternatively
can brute force by looking at least frequent character that changes at a time.

