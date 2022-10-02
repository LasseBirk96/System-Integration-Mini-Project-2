FROM python:3.10.4

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .

CMD ["python3",  "main.py"]