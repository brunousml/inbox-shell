# coding: utf-8
import logging
import zipfile
import time
import datetime
import sys
import os

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

from penne_shell import tasks

logger = logging.getLogger(__name__)


class Inspector(object):
    """
    Essa classe contém um conjunto de validações de integridade do arquivo zip e
    validações de nome dos arquivos zip.
    """

    def __init__(self, filename):
        logger.info('Inspecting file: %s' % filename)

        self._file = filename
        self._filename = filename.split('/')[-1]

    def _is_valid_zip(self):
        """
        Esse método verifica se o arquivo zip é válido.
        """
        return zipfile.is_zipfile(self._file)

    def _is_valid_filename(self):
        """
        Esse método valida o nome do arquivo zip de acordo com a regra:
        issn-acronimo_revista-volume-número-página.zip.
        """
        return True

    def is_valid(self):

        if not self._is_valid_zip():
            return (False, 'invalid zip')

        return (True, 'zip file is valid')


class EventHandler(FileSystemEventHandler):

    logfilename = 'report.log'
    files = {}

    def is_file_size_stucked(self, logpath):
        status = self.files.setdefault(logpath, 0)
        current = os.path.getsize(logpath)
        if not status == current:
            self.files[logpath] = current
            return False
        del(self.files[logpath])
        return True

    def write_log(self, logpath, message):

        logpath = logpath.split('/')
        logpath[-1] = self.logfilename
        logfile = '/'.join(logpath)

        message = datetime.datetime.now().isoformat()[:19] + ' - ' + message

        with open(logfile, 'a') as f:
            line = '%s\r\n' % message
            f.write(line)

    def on_created(self, event):
        slp_time = 3
        if self.logfilename in event.src_path:
            return False

        try:
            if event.is_directory:
                msg = 'New directory detected: %s' % event.src_path
                logger.debug(msg)
                self.write_log(event.src_path, msg)
                os.rmdir(event.src_path)
                msg = 'Directory removed: %s' % event.src_path
                logger.debug(msg)
                self.write_log(event.src_path, msg)
                return False

            msg = 'New file detected: %s' % event.src_path
            logger.info(msg)
            self.write_log(event.src_path, msg)

            while True:
                msg = 'File is being uploaded to the FTP: %s' % event.src_path
                logger.info(msg)
                self.write_log(event.src_path, msg)
                if self.is_file_size_stucked(event.src_path):
                    break
                time.sleep(10)

            inspector = Inspector(event.src_path)
            validated, validation_message = inspector.is_valid()
            msg = "Is this file valid: %s" % str(validated)
            logger.debug(msg)

            if validated:
                msg = "File is valid, sending for processing: %s" % event.src_path
                logger.debug(msg)
                self.write_log(event.src_path, msg)
                tasks.sendfile.delay(event.src_path)
                return None

            os.remove(event.src_path)
            msg = "File is not valid (%s), removed from server: %s" % (validation_message, event.src_path)
            logger.debug(msg)
            self.write_log(event.src_path, msg)

        except Exception as err:
            logger.exception(sys.exc_info()[0])
            return None


def monitor(monitored_path):

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, monitored_path, recursive=True)
    observer.start()
    logger.info('Starting to monitor the directory: %s' % monitored_path)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
