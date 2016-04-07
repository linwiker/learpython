#/usr/bin/env python
# -*- coding: utf-8 -*-

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

import time
if __name__ == '__main__':
    time.sleep(1)
    print("clock1:%s" % time.clock())
    time.sleep(1)
    print("clock2:%s" % time.clock())
    time.sleep(1)
    print("clock3:%s" % time.clock())