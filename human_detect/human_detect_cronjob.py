#!/usr/bin/env python2.7  
import os
import time
import RPi.GPIO as GPIO  
import sys
sys.path.append('/home/pi/programs/python/')
import weibo_func

GPIO.setmode(GPIO.BOARD)  
#GPIO.setmode(GPIO.BCM)  

SR501_DETECT_PIN = 11
count = 0
# GPIO 4 set up as input. It is pulled up to stop false signals  
GPIO.setup(SR501_DETECT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_OFF)  
  
#print "Make sure you have a button connected so that when pressed"  
#print "it will connect GPIO port 4 (pin 7) to GND (pin 6)\n"  
#raw_input("Press Enter when ready\n>")  
  
print "Waiting for falling edge on port 4"  
# now the program will do nothing until the signal on port 4  
# starts to fall towards zero. This is why we used the pullup  
# to keep the signal high and prevent a false interrupt  
  
#print "During this waiting time, your computer is not"   
#print "wasting resources by polling for a button press.\n"  
#print "Press your button when ready to initiate a falling edge interrupt."  
#while True:
#try:  
GPIO.wait_for_edge(SR501_DETECT_PIN, GPIO.RISING)
time_str = time.asctime()
count += 1
count_str = str(count) + '. '
print "\nRising edge detected." + count_str
#output = subprocess.Popen('sudo ./human_detect.sh', shell=True)
#os.system('sudo ./upload_yeelink.sh')
os.system('fswebcam -r 1280x960 test.jpg')
weibo_func.send_weibo( weibo_func.PICTURE_WEIBO, \
	c=count_str, t=time_str)
print "Picture upload done."

#    except KeyboardInterrupt:  
#        GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
#GPIO.cleanup()           # clean up GPIO on normal exit  
