#!/bin/bash

/usr/bin/clear

case `/bin/hostname` in
    projector-pi-1 | projector-pi-2 | projector-pi-5 | projector-pi-6 )
        while true;
        do
            /usr/bin/killall -9 omxplayer.bin
            /bin/sleep 2
            /home/pi/projector-scripts/fll-flip-projectors.py
        done
        ;;
    projector-pi-3 | projector-pi-4 | projector-pi-7 | projector-pi-8 | projector-pi-9 | projector-pi-10 )
        while true;
        do
            /usr/bin/killall -9 omxplayer.bin
            /bin/sleep 2
            /home/pi/projector-scripts/fll-projectors-4.py
        done
        ;;
    *)
        echo "Unknown projector configuration, exiting"
        exit 1
        ;;
esac