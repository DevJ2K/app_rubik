FROM debian:latest

RUN mkdir -p /home/backend/project_name

COPY app.py /home/backend
COPY requirements.txt /home/backend
COPY project_name /home/backend/project_name

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python3 pip
RUN pip install -r /home/backend/requirements.txt --break-system-packages
WORKDIR /home/backend

EXPOSE 4000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4000"]
