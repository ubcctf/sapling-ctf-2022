const express = require('express');
const pug = require('pug');
const xss = require("xss");
const crypto = require('crypto');
const _ = require('lodash');
const admin = require('./adminbot');

const PORT = process.env.PORT || 8999;

const app = express();
app.use(require('body-parser').json())
app.use(express.static('public'));

let reviews = new Map();

let greetings = [
    "Hello There :)",
    "Welcome to my Gallery",
    "My Gallery",
    "Hi!",
    "Valentina's Gallery"
];

app.get('/', function (req, res) {
    greeting_index = Math.floor(Math.random() * greetings.length);
    const template = pug.compileFile('public/templates/index.pug');
    res.end(template({msg: greetings[greeting_index]}));
});

app.get('/add_review', function (req, res){
    const review_templ = pug.compileFile('public/templates/addreview.pug');
    res.end(review_templ());
});

app.post('/add_review', function (req, res) {
    if (req.headers['content-type'] !== 'application/json'){
        return res.end("INVALID CONTENT TYPE");
    }
    
    let id = crypto.randomBytes(10).toString('hex');


    let review_template = {
        review_id: id,
        name: "Valentina",
        message: "your work is amazing!",
        stars: 5
    }

    let new_review = req.body;
    _.merge(review_template, new_review);
    let cleaned_msg = xss(new_review.message);
    reviews.set(id, cleaned_msg);

    return res.send('Thank you! Here is your review ID:' + id);
});

app.get('/view_review', function (req, res) {
  //Only admins can look owo
  if (req.socket.remoteAddress != '::1') {
    console.log("Non-admin attempted to visit /view_review");
    return res.status(403).send('Non-admins cannot access this resource');
  }

  if (reviews.length === 0){
    return res.send("no reviews to see");
  }

  let review;

  if (req.query.review_id){
    review = reviews.get(req.query.review_id);
    if (!review){
      console.log("Review does not exist");
      return res.send("No review with the given ID found");
    }
  } else {
    console.log("review ID was not given");
    return res.send("Please specify a review ID!");
  }

  return res.send(review);
});


function isValidUrl(msg){
    //https://stackoverflow.com/questions/5717093/check-if-a-javascript-string-is-a-url
    var res = msg.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
    if (msg.indexOf('http://localhost:8999') !== -1){
      return true
    }
    return (res!=null);
  }
  
app.post('/report', (req, res) => {
      if (isValidUrl(req.body.site)){
        admin.visit(req.body.site).then(res.redirect("/"));
      } else {
        console.log("user gave invalid URL:");
        console.log(req.body.site);
        return res.send("INVALID URL!"); 
      }
  });
  


app.listen(PORT, () => {
    console.log(`Listening at localhost:${PORT}`)
  })
