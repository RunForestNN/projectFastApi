FROM python:latest

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install psycopg2

COPY . /app

CMD ["python"]