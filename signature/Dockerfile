FROM python:3.10

WORKDIR /app

COPY . .


ARG PORT
ENV PORT=$PORT
ENV TERM=xterm-256color

RUN touch after_sed.txt

RUN sed s/PORT/${PORT}/g project_info > after_sed.txt

CMD [ "python", "display_signature.py" ]
