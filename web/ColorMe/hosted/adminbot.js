const puppeteer = require('puppeteer');
const SECRET = process.env.FLAG || "fakeflag{bonk}";

async function visit(url) {
  const browser = await puppeteer.launch({
                headless: true,
                args: [
        '--no-sandbox',
        '--disable-default-apps',
        '--disable-extensions',
        '--disable-gpu',
        '--disable-sync',
        '--disable-translate',
        '--hide-scrollbars',
        '--metrics-recording-only',
        '--mute-audio',
        '--no-first-run',
        '--safebrowsing-disable-auto-update'
                ]
            });
  const page = await browser.newPage();
  await page.setCookie({
            name: 'flag',
            value: SECRET,
            domain: 'localhost',
            samesite: 'none'
        });
  //await page.goto(url, {timeout: 5000});

  console.log(url);
  if (url.indexOf('https://colorme.ctf.maplebacon.org/') != -1) {
    // This is such a hack. Sorry omfg
    url = url.replace('https://colorme.ctf.maplebacon.org/', 'http://localhost:8987/');
    console.log(url);
  }
  console.log('goto');
  await page.goto(url, {timeout: 5000});

  await new Promise(resolve => setTimeout(resolve, 500));
  console.log("admin is visiting url:");
  console.log(url);


  //await new Promise(resolve => setTimeout(resolve, 500));
  await page.close();
  await browser.close();
  console.log("admin visited url");
};


module.exports = { visit }
