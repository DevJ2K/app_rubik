FROM node:16-alpine

WORKDIR /app

COPY app/ ./

RUN npm install

ARG HOST
ARG PORT
ENV HOST=$HOST
ENV PORT=$PORT

EXPOSE $PORT

# CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "4000" ]

CMD [ "sh", "-c", "npm run dev -- --host ${HOST} --port ${PORT}" ]
