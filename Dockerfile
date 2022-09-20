FROM python:3.9-slim-buster

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV PORT=3000

EXPOSE 3000

CMD ["python", "app.py"]