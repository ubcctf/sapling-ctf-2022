const express = require('express');
const path = require('path');
//const { rawListeners } = require('process');
const app = express()
const port = process.env.port || 3000;
const admin = require('./adminbot');

app.use(express.urlencoded({
  extended: true
}));

const template = (poem, adminmessage) => `
<html>  

<head>
<style>
H1 { text-align: center }
H2 { text-align: center }
H3 { text-align: center }

</style>
</head>

<h1> Welcome to Poems As A Service :) </h1>
<h3> I used to have a Colours-As-A-Service project but it was insecure :/</h3>
<h3> However! My new project is VERY secure now - all input is passed through our <a href='/sanitizer'>high-end security algorithms!</a></h3>

${poem === '' ? '': `<h1> ${poem} </h1>`}
<br>
<br>
<h2>Check out all my fave poetry!</h2>

  <a href='/?poem=古池や蛙飛び込む水の音
  ふるいけやかわずとびこむみずのおと' id=col>Bashō: "Old Pond"</a>
  <br>
  <a href='/?poem=Who+has+seen+the+wind?+Neither+I+nor+you.' id=col>Christina Rossetti: "Who Has Seen the Wind?"</a>
  <br>
  <a href='/?poem=In+a+solitude+of+the+sea.+Deep+from+human+vanity' id=col>Thomas Hardy: The Convergence of the Twain</a>

<h4> Something wrong with my collection? let me know! Submit a URL an admin will check it out. </h4>

<form action="/report" method=POST>
  <label for="url">Submit URL here</label>
  <input type="text" id="site" name="site"><br><br>
  <input type="submit" value="Submit">
</form>

${adminmessage === '' ? '': `<p> ${adminmessage} </p>`}

</html>
`;

function sanitizeInput(msg){
    if (msg.includes("<script>") || msg.includes("</script>")){
        return "BAD INPUT";
        
    } else return msg;
}

app.get('/', (req, res) => {
    if (req.query.poem && typeof(req.query.poem) == 'string'){
        let input = req.query.poem.toLowerCase();
        console.log(input);
        let cleaned = sanitizeInput(input);
        res.send(template(cleaned, ""));
    } else {
        res.send(template("", ""));
    }
})

app.get('/sanitizer', (req, res) => {
    res.sendFile(path.join(__dirname, 'sanitizer.js'));
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
    } else {
      res.send(template("", "That doesn't look like a valid HTTP/HTTPS link!"));
      return
    }
  } else {
    res.send(template("", "Error with link! Try sending it again?"));
  }
  return
})

app.listen(port, () => {
  console.log(`Listening at localhost:${port}`)
})