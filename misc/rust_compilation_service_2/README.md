Rust compilation service #2
---

As it turns out, many things can go wrong...

I'm going to make an intern stare at all the incoming rust files so they can make sure nothing suspicious is in the files before we compile them. The security team said not to compile random stuff, but just looking at them should be fine right?

Note: Our intern will be looking at the files with vscode, with the rust-analyzer plugin installed

Note: Once again, the flag is located at /chal/flag.txt

Author's note
---
If people are struggling to solve this one, maybe release the dockerfile + server.py so they can experiment locally

Getting the exploit to run remotely with the various moving parts can be a bit finicky, even after one figures out the core exploit 