import logging
# FORMAT = '%(name)s: %(levelname)s: %(asctime)s: %(message)s'
# logging.basicConfig(level=logging.DEBUG,
#                     filename='logger.txt', filemode='a', format=FORMAT)
# logger = logging.getLogger(__name__)
# logger.info('Hello')
# logger.debug('Hello')
FORMAT = '%(name)s: %(levelname)s: %(asctime)s: %(message)s'
logger = logging.getLogger(__name__)

formatter = logging.Formatter(FORMAT)
handler = logging.FileHandler('prod.txt', mode='w')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.critical('Hello')
logger.debug('Hello')
