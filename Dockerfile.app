FROM python:3.10-alpine

LABEL author="Pedro Abreu"

LABEL version="1.0"

COPY gunicorn_starter.sh gunicorn_starter.sh

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

COPY src/   /

ENTRYPOINT ["./gunicorn_starter.sh"]