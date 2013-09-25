#!/bin/bash

for i in $(seq 3)
do
	#./luvcview -O -s 1280x960 -t 10 -f jpg
	fswebcam -r 1280x960 test.jpg
	curl --request POST --data-binary @`ls -t *.jpg | head -1` --header "U-ApiKey:6640382536cf31808bb94e83fe4e8f4c" http://api.yeelink.net/v1.0/device/4014/sensor/5736/photos
	echo "Upload photo `ls -t *.jpg | head -1` done"
	#ls -t *.jpg | head -1

	#rm `ls -t *.jpg | tail -1`
done

