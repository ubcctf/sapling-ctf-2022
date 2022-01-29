# Node docker image or ubuntu docker image and install node?
FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

# env values
ENV port=8989
ENV FLAG="maple{1_H4ve_gr0ssly_misunderst0od_hoW_CsPs_w0rk}"

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
EXPOSE 8989

# Start
CMD [ "node", "index.js" ]