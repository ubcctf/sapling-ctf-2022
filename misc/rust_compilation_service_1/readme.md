Rust compilation service #1
---

I saw someone complaining about having to pipe a shell script to install rustup, so I decided to make a website where people can upload their rust projects to be compiled!

What could go wrong?

Note: The flag is located at /chal/flag.txt

Note: The server expects the zip file to just contain the cargo project directly, with no parent directory

ie: The zip file should be like this
```
src/
Cargo.toml
```

Not like this
```
myproject/
  src/
  Cargo.toml
```