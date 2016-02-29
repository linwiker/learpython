#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
r = urllib.urlopen('http://z.cn/')
html = r.read()
print html
