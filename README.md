# wifll-projectors-pi
WI FLL Competitio projectors for Raspberry PI

Run the script `configure-image.bash` with the command line argument of the number of the PI that you are creating the image for. See the table below for details. 

Ex.

```script
./configure-image.bash 7
```

## Raspberry Pi Configurations

| Trailer | Raspberry PI hostname | Projection Type | Description |
| ------- | --------------------- | --------------- | ----------- |
| 1 | projector-pi-1 | Full Screen | Switch between cam2 and cam4 |
| 1 | projector-pi-2 | Full Screen | Switch between cam1 and cam3 |
| 1 | projector-pi-3 | Split Screen | Top cam2 bottom cam1 |
| 1 | projector-pi-4 | Split Screen | Top cam4 bottom cam3 |
| 2 | projector-pi-5 | Full Screen | Switch between cam6 and cam8 |
| 2 | projector-pi-6 | Full Screen | Switch between cam5 and cam7 |
| 2 | projector-pi-7 | Split Screen | Top cam6 bottom cam5 |
| 2 | projector-pi-8 | Split Screen | Top cam8 bottom cam7 |
| 1 | projector-pi-9 | Split Screen | Switch between cam2/cam1 and cam4/cam3 (top/bottom) |
| 2 | projector-pi-10 | Split Screen | Switch between cam6/cam5 and cam8/cam7 (top/bottom) |

## Camera Locations

| Trailer | Camera | Position and Target |
| ------- | ------ | ------------------- |
| 1 | cam1 | Mounted on Red A pointing at Red B |
| 1 | cam2 | Mounted on Red B pointing at Red A |
| 1 | cam3 | Mounted on Blue A pointing at Blue B |
| 1 | cam4 | Mounted on Blue B pointing at Blue A |
| 2 | cam5 | Mounted on Red A pointing at Red B |
| 2 | cam6 | Mounted on Red B pointing at Red A |
| 2 | cam7 | Mounted on Blue A pointing at Blue B |
| 2 | cam8 | Mounted on Blue B pointing at Blue A |


## Notes

    load in image:
    dd if=/dev/disk4 of=<filename> bs=1m status=progress
    scp to a pi 
    use pishrink ($ wget https://raw.githubusercontent.com/Drewsif/PiShrink/master/pishrink.sh)
    (alternately: https://www.instructables.com/How-to-BackUp-and-Shrink-Your-Raspberry-Pi-Image/)

```script
    $ wget https://raw.githubusercontent.com/Drewsif/PiShrink/master/pishrink.sh
    $ chmod +X pishrink.sh
    $ sudo mv pishrink.sh /usr/local/bin
    $ ls -alh <image>
    $ sudo pishrink.sh -s <image>
    $ ls -alh <image>
    $ zip -9 <image>.gz <image>
```

)