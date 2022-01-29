# (Colours as a Service) Color Me

## Instructions for hosting

1. There's a `start.sh` script you can run that will simply call the correct docker build and run commands.
2. Alternatively you can do this manually:

```bash
docker build . -t web-poemme
docker run -p 8987:8987 -t web-poemme
```
The port `8988` is used for this. If this changes, let me know. 

## Important notes

**AS IT CURRENTLY STANDS, THE ADMIN BOT WILL NOT VISIT LOCALHOST DOMAINS WHEN BUILT WITH DOCKER**. This is just a quirk about docker and localhost. It will not be an issue once the challenge gets a real domain (and the cookie will be put on the domain). To test the admin bot, just `node index.js` after `npm i`.