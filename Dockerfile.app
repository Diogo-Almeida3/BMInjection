FROM python:3.10-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

COPY src/   /

COPY gunicorn_starter.sh gunicorn_starter.sh

RUN chmod +x gunicorn_starter.sh

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

COPY files/flag.txt /flag.txt

ENTRYPOINT [ "./gunicorn_starter.sh" ]