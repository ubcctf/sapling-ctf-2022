const db = require('better-sqlite3')('db.sqlite3');
const flag = process.env.FLAG || 'maple{honk}';
const port = process.env.PORT || 3030;
const express = require('express');
const crypto = require('crypto');

const noguess = (pass) => {
  for (let i = 1; i < 10; i++){
    pass = crypto.randomBytes(15).toString('base64');
  }
  return pass;
}



db.exec(`DROP TABLE IF EXISTS users;`);
db.exec(`CREATE TABLE users(
  uid INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE,
  password TEXT,
  flag TEXT,
  title TEXT
);`);

let adminPass;

//add an admin user with a random password
db.exec(`INSERT INTO users (username, password, flag, title) VALUES (
  'admin',
  '${noguess(adminPass)}',
  '${flag}',
  'my flag'
)`);

const app = express();
app.use(express.urlencoded({
  extended: true
}));

app.use(express.static('static'));
//MIDDLEWARES
app.set('view engine', 'ejs');


app.get('/', (req, res) => {
  return res.render('pages/index')
});

app.get('/login', (req, res) => {
  return res.render('pages/login')
});


app.post('/login', (req, res) => {
  if (!req.body.username || !req.body.password) {
    return res.send('ERROR: Username/password cannot be left blank!');
  }

  const query = `SELECT * FROM users WHERE
    username = '${req.body.username}' AND
    password = '${req.body.password}'
  `;

  console.log(query);

  
  let temp;

  try {
    temp = db.prepare(query).get();
  } catch (err) {
    console.log(err);
    return res.send(err);
  }

  if (temp !== undefined) {
    return res.render('pages/dashboard', {
      notetitle: temp.title,
      note: temp.flag
    });
  }

  
  return res.send('ERROR: Invalid credentials.');
});

app.listen(port, () => {
  console.log(`Listening at localhost:${port}`)
})