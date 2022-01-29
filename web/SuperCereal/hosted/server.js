const express = require('express');
const app = express()
const port = process.env.port || 3000;
const cookieParser = require('cookie-parser');
const nodeSerial = require('node-serialize');
app.use(cookieParser())


//MIDDLEWARES
app.set('view engine', 'ejs');

app.use(express.urlencoded({
  extended: true
}));


// index page
app.get('/', function(req, res) {
  if (req.cookies.profile){
    const str = new Buffer(req.cookies.profile, 'base64').toString();
    const obj = nodeSerial.unserialize(str);
    if (obj.cereal){
      const cereal = escape(obj.cereal);
      return res.render('pages/index', {
      favcereal: cereal
      });
    }

  } else {
    return res.render('pages/index', {
      favcereal: "Looks like you haven't added your secret cereal to our vault yet! Add one in secret :)"
  });
  }

});


// get secret
app.get('/secret', function(req, res) {
  if (req.cookies.profile){
  const str = new Buffer(req.cookies.profile, 'base64').toString();
  const obj = nodeSerial.unserialize(str);
  if (obj.cereal){
    const cereal = escape(obj.cereal);
    res.render('pages/secret', {
    favcereal: cereal
    });
  }

} else {
  res.render('pages/secret', {
    favcereal: ""
    });
  }

 
});


// create secret
app.post('/secret', function(req, res) {
  if (req.body != undefined && req.body != {} && req.body.favCereal != null && typeof req.body != 'string') {

    serialized = nodeSerial.serialize({
        cereal  : req.body.favCereal
      });

    const cerealCookie = Buffer.from(serialized).toString('base64')

    res.cookie('profile', cerealCookie, {
    maxAge: 900000,
    httpOnly: true
    });

    res.redirect('/');
  } else {
    res.redirect('/');
  } 
});



app.listen(port, () => {
  console.log(`Listening at localhost:${port}`)
})