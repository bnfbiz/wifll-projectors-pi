from omxplayer import OMXPlayer
from time import sleep
import os
import sys

os.system('/usr/bin/clear')

hostname = os.uname()[1]

if hostname == 'projector-pi-1':
	stream1 = 'rtsp://admin:wifll@192.168.123.31:554/cam/realmonitor?channel=1&subtype=0'
	stream2 = 'rtsp://admin:wifll@192.168.123.33:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-2':
	stream1 = 'rtsp://admin:wifll@192.168.123.32:554/cam/realmonitor?channel=1&subtype=0'
	stream2 = 'rtsp://admin:wifll@192.168.123.34:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-3':
	stream1 = 'rtsp://admin:wifll@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0'
	stream2 = 'rtsp://admin:wifll@192.168.123.37:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-4':
	stream1 = 'rtsp://admin:wifll@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0'
	stream2 = 'rtsp://admin:wifll@192.168.123.38:554/cam/realmonitor?channel=1&subtype=0'
else:
	sys.exit()

stream1file = '/home/pi/play-stream-1.txt'
stream2file = '/home/pi/play-stream-2.txt'

streamnum=0
newstreamnum=0

while True :
	
	oldstreamnum = newstreamnum
	while newstreamnum == oldstreamnum :
		sleep(1)
		if os.path.isfile(stream1file) :
			newstreamnum=1
		elif os.path.isfile(stream2file) :
			newstreamnum=2

	if oldstreamnum != 0 :
		player.pause()
		player.quit()

	if newstreamnum==1 :
		player = OMXPlayer(stream1)
	else :
		player = OMXPlayer(stream2)

	player.play()

