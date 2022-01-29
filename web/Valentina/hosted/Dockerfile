# Node docker image or ubuntu docker image and install node?
FROM node:alpine

RUN apk update
RUN apk add --update bash curl coreutils

# Create app directory
WORKDIR /usr/src/app

# env values
ENV PORT=8999
ENV FLAG="RkxBRzE9bWFwbGV7bDBkNHNoX21vcmVfbHlrX24wZGE1aF9oYWhhX2dldF9pdH0g"

RUN apk add --no-cache \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ca-certificates \
      ttf-freefont \
      nodejs 

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Install rest of the packages
COPY package*.json ./
RUN npm install

# App src
COPY . .

# Expose port
EXPOSE 8999

# User
RUN addgroup -S ctf && adduser -S ctf -G ctf
USER ctf:ctf

# Start
CMD [ "node", "index.js"]