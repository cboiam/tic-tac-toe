FROM python:3.8-slim

WORKDIR /app

COPY __init__.py src/
COPY core src/core/
COPY webserver src/webserver

RUN pip install -r src/webserver/requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-w", "1", "-b", ":5000", "-k", "eventlet", "src.webserver.app:server"]