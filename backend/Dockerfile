FROM python:3.10

WORKDIR /app

COPY app.py ./
COPY requirements.txt ./
COPY project_name ./project_name

RUN pip install -r requirements.txt


ARG HOST
ARG PORT

ENV HOST=$HOST
ENV PORT=$PORT

EXPOSE $PORT
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4000"]
# CMD ["fastapi", "dev", "app.py", "--host", "${HOST}", "--port", "${PORT}"]

CMD [ "sh", "-c", "fastapi dev app.py --host ${HOST} --port ${PORT}" ]
