#!/bin/bash

sleep 30  # waiting for the wifi network

sudo python /home/pi/programs/temprature/temprature.py >> /home/pi/programs/log1.txt 2>&1 &
sudo python /home/pi/programs/human_detect/human_detect.py >> /home/pi/programs/log2.txt 2>&1 &
echo "test" >> /home/pi/programs/test.txt
