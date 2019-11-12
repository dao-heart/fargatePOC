FROM python:3.5-slim

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 8081

CMD ["python", "app.py"]
