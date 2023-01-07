# syntax=docker/dockerfile:1

FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]