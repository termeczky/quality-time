FROM node:22.5.1-alpine3.20

LABEL maintainer="Quality-time team <quality-time@ictu.nl>"
LABEL description="Quality-time PDF render service"

RUN apk add --no-cache \
    msttcorefonts-installer=3.8.1-r1 \
    fontconfig=2.15.0-r1 \
    font-noto=23.7.1-r0 \
    freetype=2.13.2-r0 \
    ttf-dejavu=2.37-r5 \
    ttf-droid=20200215-r2 \
    ttf-freefont=20120503-r4 \
    ttf-liberation=2.1.5-r2 \
    chromium=128.0.6613.84-r0 && \
    rm -rf /var/cache/apk/* /tmp/*

RUN update-ms-fonts \
    && fc-cache -f

RUN npm install --ignore-scripts -g npm@10.8.2

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

WORKDIR /home/renderer
COPY package*.json /home/renderer/
RUN npm install --ignore-scripts

COPY src/*js /home/renderer/

RUN adduser renderer --disabled-password
USER renderer

HEALTHCHECK CMD node /home/renderer/healthcheck.cjs

ENV NODE_ENV production

CMD ["node", "/home/renderer/index.js"]
