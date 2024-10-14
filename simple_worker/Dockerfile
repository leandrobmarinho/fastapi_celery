FROM python:3.8-slim

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  git \
  libpq-dev \
  libffi-dev \
  cargo \
  openssl \ 
  netcat-openbsd \
  gcc \
  locales && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY teste.txt .

#COPY app.py /app.py
ADD . /simple_worker
WORKDIR /simple_worker

ENTRYPOINT celery -A tasks worker --loglevel=info
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']