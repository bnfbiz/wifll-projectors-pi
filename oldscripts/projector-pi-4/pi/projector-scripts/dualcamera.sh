#!/bin/sh

# 100%
# omxplayer --no-keys -o hdmi --live --win 0,0,959,539 --crop 0,0,1919,1079 'rtsp://admin:wifll@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0' &
# omxplayer --no-keys -o hdmi --live --win 0,540,959,1079 --crop 0,0,1919,1079 'rtsp://admin:wifll@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0' &


# 76%
omxplayer --no-keys -o hdmi --live --win 0,0,1261,539 --crop 0,259,1919,1079 'rtsp://admin:wifll@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0' &
omxplayer --no-keys -o hdmi --live --win 0,540,1261,1079 --crop 0,259,1919,1079 'rtsp://admin:wifll@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0' &

fbi --noverbose ~/FLLLogo2022.png

