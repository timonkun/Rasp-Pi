#!/usr/bin/env python2.7  
# -*- coding: utf-8 -*-

import os
import time
import sys
sys.path.append('/home/pi/programs/python/')
import weibo_func
import string

count = 0
WEIBO_FLAG = 0  #发微博还是传yeelink
  
while True:
	try:
		p = os.popen('sudo /home/pi/programs/temprature/dht11', 'r')
		cur_h_line = p.readline()
		cur_h = string.atof(cur_h_line)

		cur_t_line = p.readline()
		cur_t = string.atof(cur_t_line)
	
		# 错误值，PASS
		if cur_h == 0.0 and cur_t == 0.0:
			print 'Value error.'
			continue

		# 发微博
		if WEIBO_FLAG == 1:
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
		else:	#传yeelink
			yeelink_t_str = str(cur_t)
			yeelink_cmd_t = '''curl --request POST --data '{"value":''' + yeelink_t_str + \
			'''}' --header "U-ApiKey:6640382536cf31808bb94e83fe4e8f4c" \
			http://api.yeelink.net/v1.0/device/4014/sensor/8028/datapoints'''
			#print yeelink_cmd_t
			p= os.popen(yeelink_cmd_t, 'r')

			yeelink_h_str = str(cur_h)
			yeelink_cmd_h = '''curl --request POST --data '{"value":''' + yeelink_h_str + \
			'''}' --header "U-ApiKey:6640382536cf31808bb94e83fe4e8f4c" \
			http://api.yeelink.net/v1.0/device/4014/sensor/8031/datapoints'''
			#print yeelink_cmd_h
			p= os.popen(yeelink_cmd_h, 'r')
			time.sleep(300)

	except KeyboardInterrupt:  
		print 'Ctrl+C to quit.'       # CTRL+C exit
		exit(1)
