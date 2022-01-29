const puppeteer = require('puppeteer');
const SECRET = "maple{fake_flag_not_the_real_flag}";

async function visit(url) {
  let browser, page;
  return new Promise(async (resolve, reject) => {
    try {
      browser = await puppeteer.launch({
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
        page = await browser.newPage();
        await page.setCookie({
            name: 'flag',
            value: SECRET,
            domain: 'localhost',
            samesite: 'none'
        });
        //await page.goto(query, {waitUntil : 'networkidle2' }).catch(e => void 0);
        await page.goto(url, {waitUntil : 'networkidle2' }).catch(e => console.log(e));
        await new Promise(resolve => setTimeout(resolve, 500));
        console.log("admin is visiting url:");
        console.log(url);
        await page.close();
        console.log("admin visited url");
        page = null;
    } catch (err){
        //Ming pls
        console.log(err);
    } finally {
        if (page) await page.close();
        console.log("page closed");
        if (browser) await browser.close();
        console.log("browser closed");
        //no rejectz
        resolve();
        console.log("resolved");
    }
  });
};


module.exports = { visit }