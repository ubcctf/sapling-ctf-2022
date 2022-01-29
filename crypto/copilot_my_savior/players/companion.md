The Cryptographer's Codex vol 1
---

Welcome to the first cryptography challenge in the symmetric cryptography series! 

First of all lets get you up and running with how to manipulate bytes in python. If you haven't written python before, don't worry! Python is notoriously simple and easy to pick up, granted that you've written in an imperative language before.

"But what if I've only written Racket in 110?" I hear you cry, and don't worry there's a section for that as well.

### Feel free to skip anything you already know!!!

Let's dive into it! I would recommend having the python REPL open (type `python` in the command line) and following along with the code examples

## The basics
```python
# The bytes type is usually defined like this 

my_bytes = b"this is not a string, but a bytes object!"

list(my_bytes) # converts my_bytes to a list of numbers
bytes(my_list) # converts a list of numbers to a bytes object
```

A Bytes object is really just a list of numbers, and you can see that by running `list(b"my bytes")` or `b"my bytes"[0]`. There is one important detail, which is that a number in a byte array is always between 0 and 255, which is 2**8-1. For details, wait til cpsc 121!

In general
- You get bytes objects from reading stuff (ie `open("data","rb").read()`) or converting from other data formats (hex, base64)
- You usually want to work with the list of numbers (because you can then map and iterate over it easily)
- You want to convert your final result to a bytes object to print it (because python will then format it nicely for you)

## Two more important functions

```python
chr(x) # converts a decimal number x between 0 and 255 to it's character
ord(c) # converts a character c to it's corresponding byte number

ord("a") == 97
chr(97) == "a"
```

Since all bytes are numbers and we sometimes want bytes to represent characters instead of random numbers, some smart people figured out the [ascii table](https://www.asciitable.com/) and that's what `ord` and `chr` use.

## Decode and encode

Very similar to `chr` and `ord`

```python
"my string".encode() # converts from a string to bytes
b"my bytes".decode() # converts from bytes to a string
```

These can be thought of as shorthand for calling `ord`/`chr` on each character/number in a string/bytes.

## How to work with bytes

Your best friends will probably be good ol' for loops

For the imperatively minded, this will print the numbers in the array, so `101`, `121`, `32` ...
```python
for b in b"my bytes":
    print(b)
```

For the functionally minded (and those who took 110), python does have maps and filters and such
```python
list(map(lambda x: x+1, b"my bytes"))
```

My preferred method is using python [list comprehensions](https://www.w3schools.com/python/python_lists_comprehension.asp) since they're basically less clunky maps

```python
[x+1 for x in b"my bytes"]
```
## XOR

If you've taken 121 you've seen it before, but it turns out that xor is actually quite important for various parts of cryptography. If you haven't taken 121, you'll want to understand how xor works so google "bitwise XOR". Good googling skills are important!

## XOR in python

python has a xor operator, `^`

```python
x ^ y # this is x xor y
      # x and y have to be numbers
```

Since `^` only operates on numbers, you have to use one of the above strategies for actually xoring your entire bytes object.

## Files in python

This might be a bit tricky if you haven't seen this type of interface before, but here's how you work with files in python

```python
mode = "r" # Read my file as a big string
mode = "rb" # Read my file as a big bytes object 
mode = "w" # Write strings to my file
mode = "wb" # Write bytes to my file

f = open("my_filename", mode) # Open "./my_filename" with the given mode

# if you don't input a mode, the mode is assumed to be "r"

# You have to give a filename that already exists to use either r or rb
# But you can use w or wb with a file that doesnt exist, python will create the file for you

# f is a file object, the functions you can call on it are:
f.close() # Closes the file, must always be called or else bad things happen

# =============================================
# if you opened as mode = "r"
f.read()      # Returns the entire contents of the file as a big string
f.readlines() # Returns an array of strings where each string is a line from the file

# =============================================
# if you opened as mode "rb"
f.read()      # Returns the entire contents of the file as a big bytes object

# =============================================
# if you opened as mode "w"
f.write(my_string) # Writes the string into the file

# =============================================
# if you opened as mode "wb"
f.write(my_bytes)  # Writes the bytes into the file
```

This is only a basic summary, but hopefully it gives you the basic gist for how files work in python. You can read more about them [here](https://www.programiz.com/python-programming/file-operation). If you're curious about why files work like this and why you need to seek around a file then wait til 313! You'll learn all about them there.

## Bash tricks

Did you know that you can automatically make any program write to a file instead of printing out it's results?

```bash
$ python my_script.py > result.txt
```

Anything that `my_script.py` prints out will be put into `result.txt` instead of being shown on the terminal.

## For those who really want to write racket in python

Here's some functions to get you started

```python
def cons(x, xs):
    return [x] + xs

def first(b):
    return b[0]

def rest(b):
    return b[1:] # <-- python slice notation

def fn_for_bytes(b):
    if len(b) == 0:
        return # ...
    else:
        first_res = # ... fn_for_byte(first(b)) 
        rest_res =  # ... fn_for_bytes(rest(b))
        result =    # ... first_res, rest_res
        return result
```

(PS: Though all the code you'll be presented with will be in an imperative style, so you should get used to the whole imperative thing)

# Ok but how do I solve this thing???

Some advice then:
1. Look carefully at `encrypt.py`. What information do we not know? What does the `encrypt` function do? What could you do to undo it's effects if you knew the `???` value? 
2. What happens if you XOR a byte by the same byte twice?
3. Think about the `???` value. What are the possible values that it could be? Could you try to guess it? How many guesses would you need to make? How would you know if your guess was correct?