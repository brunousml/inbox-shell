# coding: utf-8
import logging
import os

from celery import Celery

logger = logging.getLogger(__name__)

celery_broker = 'amqp://guest@localhost//'
app = Celery('tasks', broker=celery_broker)


@app.task
def uploadfile(filename):
    logger.info('Scheduling file to be sent: %s' % filename)
    os.remove(filename)
    pass
