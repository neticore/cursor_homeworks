FROM ubuntu:latest

RUN apt-get update && apt-get install -y python python3-pip
RUN pip install flask
COPY main.py /opt/
ENTRYPOINT FLASK_APP=/opt/main.py flask run --host=0.0.0.0 --port=8080