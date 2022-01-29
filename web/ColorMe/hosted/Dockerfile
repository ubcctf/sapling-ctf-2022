# Node docker image or ubuntu docker image and install node?
FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

# env values
ENV port=8987
ENV FLAG="maple{0ops_i_f0rgot_about_xss}"


# Installs latest Chromium (92) package.
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
EXPOSE 8987

# Start
CMD [ "node", "index.js" ]