#!/usr/bin/env python
# -*- coding: utf-8 -*-
num=int(raw_input('please input a score:'))
if 90<= num <=100:
    print 'A'
elif  70<= num <= 89:
    print 'B'
elif  60 <= num <=69:
    print 'C'
elif   0 <= num <=59:
    print 'D'
else:
    print "Invalid score"
    
