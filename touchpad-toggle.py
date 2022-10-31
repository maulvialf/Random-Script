#!/usr/bin/env python

import os

os.system('synclient | grep Touc > mousestat')

baca = open('mousestat')

stat = baca.read()

if '1' in stat:
	os.system('synclient TouchpadOff=0')
else:
	os.system('synclient TouchpadOff=1')