#!/bin/bash

/usr/bin/clear

if [ `/bin/hostname` == "projector-pi-0" ]; then
    while true;
    do
        /bin/sleep 2
        /home/pi/projector-scripts/control-screen-flip.py
    done
elif [ `/bin/hostname` == "projector-pi-9" ]; then
    while true;
    do
        /usr/bin/killall -9 omxplayer.bin
        /bin/sleep 2
        /home/pi/projector-scripts/fll-flip-projectors.py
    done
elif [ `/bin/hostname` == "projector-pi-10" ]; then
    while true;
    do
        /usr/bin/killall -9 omxplayer.bin
        /bin/sleep 2
        /home/pi/projector-scripts/fll-flip-projectors.py
    done
else
    while true;
    do
        /usr/bin/killall -9 omxplayer.bin
        /bin/sleep 2
	/home/pi/projector-scripts/fll-projectors-4.py
#        /home/pi/projector-scripts/fll-flip-projectors.py
    done
fi
