#!/usr/bin/python2
#!encoding = utf-8

import sys
import utils
import commands
reload(sys)
sys.setdefaultencoding('utf-8')
windows = utils.get_windows()
for win in windows:
	print 'wmctrl -c '+win
	commands.getoutput('wmctrl -c '+win)
