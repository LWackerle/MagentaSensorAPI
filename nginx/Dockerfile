### PART 1: Docker will build a PROD-ready version of the (React)Webapp
FROM node:12.13.1-alpine AS builder

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install all used packages
COPY ./webinterface/*.json ./
RUN npm install

# Prepare for production build
COPY ./webinterface/public /usr/src/app/public
COPY ./webinterface/src /usr/src/app/src

# Build the webapp
RUN npm run build

### PART 2: Docker will build the Nginx image with the (React)Webapp
FROM nginx:1.16.1-alpine


# Prepare needed directories
RUN mkdir -p /usr/share/nginx/webinterface

# COPY all needed nginx related files (config & ssl)
COPY ./nginx.conf /etc/nginx/nginx.conf

# Get webapp files from previous step (see PART 1)
COPY --from=builder /usr/src/app/build /usr/share/nginx/html/webapp

EXPOSE 80
