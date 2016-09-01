FROM python:3.5.2

MAINTAINER tecnologia@scielo.org

RUN apt-get update && apt-get install -y supervisor
RUN apt-get install sftp
RUN mkdir -p /var/log/supervisor

COPY requirements.txt /app/requirements.txt
COPY docker/entrypoint.sh /app/docker/entrypoint.sh
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

RUN pip install -r requirements.txt

ADD docker/entrypoint.sh /app/docker/entrypoint.sh
RUN chmod +x /app/docker/entrypoint.sh

ENTRYPOINT [ "/app/docker/entrypoint.sh" ]