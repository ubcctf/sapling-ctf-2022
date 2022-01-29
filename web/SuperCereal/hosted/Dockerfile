FROM node:alpine

# Just in case
RUN apk update
RUN apk add --update curl

# Create app directory
WORKDIR /usr/src/app

# env values
ENV port=8990

# Install rest of the packages
COPY package*.json ./
RUN npm install

# App src
COPY . .

# Expose port
EXPOSE 8990

# User
RUN addgroup -S ctf && adduser -S ctf -G ctf
USER ctf:ctf

# Start
CMD [ "node", "server.js" ]