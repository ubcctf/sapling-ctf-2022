# Node docker image or ubuntu docker image and install node?
FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

RUN apk update && apk add python3 make g++

# env values
ENV PORT=8996
ENV FLAG="maple{ess_skew_el_inject10nz_are_pr3tty_fun}"

# Install rest of the packages
COPY package*.json ./
RUN npm install

# App src
COPY . .

# Expose port
EXPOSE 8996

# Start
CMD [ "node", "index.js" ]