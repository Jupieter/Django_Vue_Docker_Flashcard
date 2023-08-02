FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PATH /app:$PATH

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000

# RUN ["python", "manage.py", "runserver"]

