FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/
ENV PYTHONPATH=/app
ENV QUEUE=broadcast
CMD sh -c "celery -A bugreport.celery worker --loglevel=debug --concurrency=1 --queues=\${QUEUE}"