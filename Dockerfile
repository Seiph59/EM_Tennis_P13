FROM python:3.6.13-buster
ENV PYTHONUNBUFFERED=1
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PWD=$DB_PWD
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/