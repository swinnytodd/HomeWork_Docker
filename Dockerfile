FROM python:3.8-alpine3.12
WORKDIR /app

COPY hello.py .

CMD python3 hello.py