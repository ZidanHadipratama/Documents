FROM python:3.9-slim

RUN useradd -m web

RUN mkdir /app

WORKDIR /app

RUN pip install --no-cache-dir Flask

COPY app.py .

RUN chown -R web:web /app

USER web

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]

