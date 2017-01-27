#!/usr/bin/python2
#!encoding = utf-8

import sys
import utils
reload(sys)
sys.setdefaultencoding('utf-8')

for line in utils.match_win():
	print '[' + line     + ']'
	print "command=wmctrl -c "+line
	print "icon="
	print "subtext=close " + line
