#!/usr/bin/env python2.7  
import os
import time
import sys
sys.path.append('/home/pi/programs/python/')
import weibo_func
import string

count = 0
  
while True:
	try:
		p = os.popen('sudo /home/pi/programs/temprature/dht11', 'r')
		cur_h_line = p.readline()
		cur_h = string.atof(cur_h_line)

		cur_t_line = p.readline()
		cur_t = string.atof(cur_t_line)
	
		if cur_h == 0.0 and cur_t == 0.0:
			print 'Value error.'
			continue

		line_h = ' Humidity: ' + str(cur_h) + '%'
		line_t = ' Temprature: ' + str(cur_t) + '*C'

		timeStr = time.asctime()
		count += 1
		countStr = str(count) + '. '

		print countStr + timeStr
		print line_t
		print line_h
		lineStr = line_t + line_h
		weibo_func.send_weibo(weibo_type=weibo_func.TEMPRATURE_WEIBO, \
			c=countStr, t=timeStr, h=lineStr)
		print "weibo sending done."
		time.sleep(3600)

	except KeyboardInterrupt:  
		print 'Ctrl+C to quit.'       # CTRL+C exit
		exit(1)
