import logging

logging.basicConfig(filename='i.cfg',format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                    datafmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')
