FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

# env values
ENV port=8988
ENV FLAG="maple{why_m4ke_ur_0wn_5anitizers_wh3n_D0mpur1fy_ex1sts}"


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
EXPOSE 8988

# Start
CMD [ "node", "index.js" ]