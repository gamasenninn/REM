FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update
RUN apt-get install -y vim
RUN pip install --upgrade reportlab

COPY ./app /app