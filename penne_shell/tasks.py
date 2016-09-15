# coding: utf-8
import sys
import os
import logging

from celery import Celery

from penne_shell.api_clients import FrontDesk
from penne_shell import settings
logger = logging.getLogger(__name__)

celery_broker = 'amqp://%s//' % settings.RABBITMQ_HOST
app = Celery('tasks', broker=celery_broker)

fd = FrontDesk()


@app.task
def uploadfile(filename, depositor, safe_mode):
    logger.info('Scheduling file to be sent: %s' % filename)

    try:
        fd.uploadfile(filename, depositor)
    except Exception as err:
        logger.exception(sys.exc_info()[0])

    if safe_mode:  # skiping to remove files from server.
        return

    os.remove(filename)
