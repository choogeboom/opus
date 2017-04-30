FROM python:3.6.1-slim
MAINTAINER Christopher Hoogeboom <chris.hoogeboom@gmail.com>

RUN apt-get update && apt-get install -qq \
    build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /opus

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "opus.app:create_app()"