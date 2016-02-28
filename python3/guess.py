#!/usr/bin/python
# -*- coding: utf-8 -*-
#filename:guess.py
from random import randint
x =randint(1,100)
for count in range(3):
	num=input('Please input a number between 0-100:')
	if int(num)==x:
		print("congratulations! you win!")
		break
else:
	print("Oops!you fail!")
