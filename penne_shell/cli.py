# coding: utf-8

import click
import logging
import logging.config

from penne_shell.penne_shell import monitor

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'penne_shell': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}


def _config_logging(logging_level='INFO'):

    LOGGING['loggers']['penne_shell']['level'] = logging_level

    logging.config.dictConfig(LOGGING)


@click.command()
@click.argument('monitored_path')
@click.option(
    '--logging_level', '-l', default='INFO',
    type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
)
def main(monitored_path, logging_level):
    _config_logging(logging_level=logging_level)
    monitor(monitored_path)

if __name__ == "__main__":
    main()
