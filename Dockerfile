FROM python:2.7

RUN apt-get update
RUN apt-get install -y sqlite nano 

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# RUN python db_create.py
# COPY . /usr/src/app


EXPOSE 5000

ENTRYPOINT ["python"]