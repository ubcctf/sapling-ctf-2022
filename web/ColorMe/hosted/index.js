const express = require('express');
const app = express()
const port = process.env.port || 3030;
const admin = require('./adminbot');

app.use(express.urlencoded({
  extended: true
}));

const template = (colour, adminmessage) => `
<html>

<head>
<style>
H1 { text-align: center }
H2 { text-align: center }

</style>
</head>

<h1> Welcome to colours as a service :) </h1>
${colour === '' ? '': `<h1> ${colour} </h1>`}
<h2>change colours with the buttons below!</h2>

  <a href='/?colour=blue' id=col>blue</a>
  <a href='/?colour=red' id=col>red</a>
  <a href='/?colour=yellow' id=col>yellow</a>
  <a href='/?colour=orange' id=col>orange</a>
  <a href='/?colour=green' id=col>green</a>
  <a href='/?colour=purple' id=col>purple</a>
  <a href='/?colour=pink' id=col>pink</a>

<h3>Have a new colour you want to try out? Type it below!<h3>

<form action="/?colour=">
  <label for="colour">New Colour:</label>
  <input type="text" id="colour" name="colour"><br><br>
  <input type="submit" value="Submit">
</form>

<h4> Something wrong with the colours? let us know! Submit a URL to us and an admin will check it out. </h4>

<form action="/report" method=POST>
  <label for="url">Submit URL here</label>
  <input type="text" id="site" name="site"><br><br>
  <input type="submit" value="Submit">
</form>

${adminmessage === '' ? '': `<p> ${adminmessage} </p>`}


<script>
nospace = "${colour}".replace(" ", '');
for (let i = 0; i < document.getElementsByTagName('h1').length; i++) {
  document.getElementsByTagName('h1')[i].style.color = nospace;
}
</script>

</html>
`;

app.get('/', (req, res) => {
  return res.send(template(req.query.colour || "", ""));
})

function isValidUrl(msg){
  //https://stackoverflow.com/questions/5717093/check-if-a-javascript-string-is-a-url
  var res = msg.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
  return (res!=null);
}

app.post('/report', (req, res) => {
  if (req.body != undefined && req.body != {} && req.body.site != null && typeof req.body != 'string') {
    if (isValidUrl(req.body.site)){
      admin.visit(req.body.site).then(res.send(template("", "Thanks! An admin will check it out shortly.")));
      return;
    } else {
      return res.send(template("", "That doesn't look like a valid HTTP/HTTPS link!"));
    }
  } else {
    return res.send(template("", "Error with link! Try sending it again?"));
  }
})

app.listen(port, () => {
  console.log(`Listening at localhost:${port}`)
})