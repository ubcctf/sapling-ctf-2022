# Poem Me Writeup
"Poem Me" is functionally similar to the previous XSS challenge "Color Me". This is a challenge where the GET query parameter "poem" is a potential vector for JS injection. The problem? 

```js
function sanitizeInput(msg){
    if (msg.includes("<script>") || msg.includes("</script>")){
        return "BAD INPUT";
        
    } else return msg;
}


app.get('/', (req, res) => {
    //if there's a query parameter called "poem" then we gotta make sure and clean it!
    if (req.query.poem && typeof(req.query.poem) == 'string'){
        let input = req.query.poem.toLowerCase();
        //Get rid of script tags. Now I'm protected against XSS! 
        let cleaned = sanitizeInput(input);
        res.send(template(cleaned, ""));
    } else {
        res.send(template("", ""));
    }
})
```

The program has an XSS sanitizer! So if we do specify a `poem` query parameter, whatever is inside it will be filtered of any `<script>` tags. Seems like all hope is lost, hey?

Well, not quite! `<script>` tags aren't the only potential method of inline JavaScript execution, they just happen to be the most direct. Any **event handlers** or **source attributes** are also valid places to execute JavaScript. For example:

```HTML
<img src=a.website.that.does.not.exist onerror=alert(1);></img>
```

The `onerror` is an event handler which expects some form of JS code to execute. In this case, we have the `onerror` pop an alert when the image doesn't load. 

Another example is using `src` attributes:

```HTML
<iframe src=javascript:alert(1);></iframe>
```

While the `src` attribute itself is looking for some URL, you can instead specify a JS URI and it will execute accordingly. 

Either payload will work for this challenge as neither of them use `<script>` tags! From here, the methodology to get the flag is the same: get yourself a webhook, modify your payload to steal a user's cookies, and report your XSS url to the admin to get the flag!

```
maple{why_m4ke_ur_0wn_5anitizers_wh3n_D0mpur1fy_ex1sts}
```