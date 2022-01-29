const express = require('express');
const app = express()
const port = process.env.port || 8989;
const admin = require('./adminbot');
const crypto = require('crypto');
const path = require('path');


let NONCE = crypto.randomBytes(10).toString('base64');

// ======== MIDDLEWARE START (not part of the challenge. You can safely ignore)
app.use(express.urlencoded({
  extended: true
}));
//// ======== MIDDLEWARE END


function newNonce(){
  NONCE = crypto.randomBytes(10).toString('base64');
}

for (let i = 0; i <= 15; i++){
  // You can't guess this nonce heHEH
  newNonce();
}


app.get('/', (req, res) => {
  res.setHeader("Content-Security-Policy", `default-src none; script-src 'nonce-${NONCE}'; style-src https://stackpath.bootstrapcdn.com;`);
  return res.sendFile(path.join(__dirname+'/static/index.html'));
})


//spag code :-)
app.get('/TwilightLink', (req, res) => {
  res.setHeader("Content-Security-Policy", `default-src none; script-src 'nonce-${NONCE}';`);
  return res.sendFile(path.join(__dirname+'/static/TwilightLink.txt'));
})

app.get('/WindWakerLink', (req, res) => {
  res.setHeader("Content-Security-Policy", `default-src none; script-src 'nonce-${NONCE}';`);
  return res.sendFile(path.join(__dirname+'/static/WindWakerLink.txt'));
})

app.get('/BOTWLink', (req, res) => {
  res.setHeader("Content-Security-Policy", `default-src none; script-src 'nonce-${NONCE}';`);
  return res.sendFile(path.join(__dirname+'/static/BOTWLink.txt'));
})

app.get('/MajorasMaskLink', (req, res) => {
  res.setHeader("Content-Security-Policy", `default-src none; script-src 'nonce-${NONCE}';`);
  return res.sendFile(path.join(__dirname+'/static/MajorasMaskLink.txt'));
})


function isValidUrl(msg){
  //https://stackoverflow.com/questions/5717093/check-if-a-javascript-string-is-a-url
  var res = msg.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
  return (res!=null);
}

app.post('/report', (req, res) => {
  if (req.body != undefined && req.body != {} && req.body.site != null && typeof req.body != 'string') {
    if (isValidUrl(req.body.site)){
      admin.visit(req.body.site).then(res.send("Thanks! An admin will check it out shortly."));
    } else {
      return res.send("That doesn't look like a valid HTTP/HTTPS link!");
      
    }
  } else {
    return res.send("Error with link! Try sending it again?");
  }
});

app.all('*', (req, res) => {
  res.setHeader("Content-Security-Policy", `default-src none; script-src 'nonce-${NONCE}';`);
  let str = decodeURI(req.url.substring(1));
  return res.status(404).send('ERROR 404: ' + decodeURI(str) + " not found");
});


app.listen(port, () => {
  console.log(`Listening at localhost:${port}`)
})