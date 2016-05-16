#/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
from core import main
from conf import settings

base_dir = os.path.dirname(os.path.dirname(__file__))
print(base_dir)
sys.path.append(base_dir)

if __name__ == '__main__':
    pass