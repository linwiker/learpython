#!/usr/bin/env python
from string import maketrans

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example......wow!!!"
print str.translate(trantab)
print str.translate(trantab,'ex')
