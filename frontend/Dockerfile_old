FROM debian:latest

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN mkdir -p /home/frontend
COPY app /home/frontend

RUN apt-get update \
    && apt-get install -y curl \
    && apt-get -y autoclean

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash \
    && export NVM_DIR="$HOME/.nvm" \
    && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" \
    && nvm install 20 \
    && nvm use 20 \
    && nvm alias default 20

ENV NVM_DIR="/root/.nvm"
ENV NODE_VERSION="20.16.0"
ENV NVM_BIN="$NVM_DIR/versions/node/v$NODE_VERSION/bin"
ENV PATH="$NVM_BIN:$PATH"

WORKDIR /home/frontend

RUN "$NVM_BIN/npm" install

EXPOSE 4000

CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "4000" ]
