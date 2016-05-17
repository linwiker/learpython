#/usr/bin/env python
# -*- coding: utf-8 -*-
from core import main
from conf import settings


if __name__ == '__main__':
    d = main.MonitorServer()
    d.start()
