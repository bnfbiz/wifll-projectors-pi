#!/bin/bash


RASPROOT=/mnt
BASEIMAGE="images/wifll-field-202309-patched-shrunk.img.zip"
SEASONLOGO=FLLLogo2023.png

case "$1" in
    1)
        projectorHostname="projector-pi-1"
        projectorIpAddress="192.168.123.21"
        ;;
    2)
        projectorHostname="projector-pi-2"
        projectorIpAddress="192.168.123.22"
        ;;
    3)
        projectorHostname="projector-pi-3"
        projectorIpAddress="192.168.123.23"
        ;;
    4)
        projectorHostname="projector-pi-4"
        projectorIpAddress="192.168.123.24"
        ;;
    5)
        projectorHostname="projector-pi-5"
        projectorIpAddress="192.168.123.25"
        ;;
    6)
        projectorHostname="projector-pi-6"
        projectorIpAddress="192.168.123.26"
        ;;
    7)
        projectorHostname="projector-pi-7"
        projectorIpAddress="192.168.123.27"
        ;;
    8)
        projectorHostname="projector-pi-8"
        projectorIpAddress="192.168.123.28"
        ;;
    9)
        projectorHostname="projector-pi-9"
        projectorIpAddress="192.168.123.29"
        ;;
    10)
        projectorHostname="projector-pi-10"
        projectorIpAddress="192.168.123.30"
        ;;
    *)
        echo "Not a valid image"
        ;;
esac

image=${projectorHostname}.img
echo "Processing image $image"

# cleanup any old image and recreate the new one
echo "Creating initial image copy from master"
rm -f $image
funzip $BASEIMAGE > $image

# Create loopback device for the boot and root partition
echo "Creating the loop back device"
sudo losetup -P /dev/loop0 $image

# mount root parition
echo "Mounting the filesystems"
sudo mount /dev/loop0p2 $RASPROOT
sudo mount /dev/loop0p1 $RASPROOT/boot

# Setup the hostname
echo "Setting the hostname"
if [ ! -f $RASPROOT/etc/hostname.fcs ];
then
    sudo cp -p $RASPROOT/etc/hostname $RASPROOT/etc/hostname.fcs
fi
sudo chmod 644 $RASPROOT/etc/hostname
echo $projectorHostname | sudo tee $RASPROOT/etc/hostname > /dev/null

echo "Adjusting the hosts file"
if [ ! -f $RASPROOT/etc/hosts.fcs ];
then
    sudo cp -p $RASPROOT/etc/hosts $RASPROOT/etc/hosts.fcs
fi
sudo chmod 644 $RASPROOT/etc/hosts
sudo perl -i -p -e "s/projector-pi-99/$projectorHostname/" $RASPROOT/etc/hosts

# set the IP address
echo "Setting the IP address"
if [ ! -f $RASPROOT/boot/dhcpcd.conf.fcs ];
then
    sudo cp -p $RASPROOT/boot/dhcpcd.conf $RASPROOT/boot/dhcpcd.conf.fcs
fi
sudo chmod 644 $RASPROOT/boot/dhcpcd.conf
sudo perl -i -p -e "s/192.168.123.19/$projectorIpAddress/" $RASPROOT/boot/dhcpcd.conf

# Copy in the projector configuration scripts
echo "Installing the pi user and year theme information"
for i in $SEASONLOGO loginscript.sh .profile
do
    if [ ! -f $RASPROOT/home/pi/${i}.fcs ];
    then
        if [ -f $RASPROOT/home/pi/${i} ];
        then
            cp $RASPROOT/home/pi/${i} $RASPROOT/home/pi/${i}.fcs
        fi
    fi
    cp -r files/${i} $RASPROOT/home/pi/${i}
done

echo "Installing the projector-scripts"
for i in projector-scripts
do
    if [ ! -d $RASPROOT/home/pi/${i}.fcs ];
    then
        if [ -d $RASPROOT/home/pi/${i} ];
        then
            mv $RASPROOT/home/pi/${i} $RASPROOT/home/pi/${i}.fcs
        fi
    fi
    cp -r files/${i} $RASPROOT/home/pi/${i}
done

# Update the scripts to have the current logo file
for i in fll-flip-projectors.py fll-projectors-4.py fll-projectors.py
do
    if [ ! -f $RASPROOT/home/pi/projector-scripts/${i}.fcs ];
    then
        cp $RASPROOT/home/pi/projector-scripts/${i} $RASPROOT/home/pi/projector-scripts/${i}.fcs
    fi
    perl -i -p -e "s/SEASONLOGO/${SEASONLOGO}/" $RASPROOT/home/pi/projector-scripts/${i}
done

# Update the boot command line to resize the disk
echo "Enabling auto resizing of the disk on boot"
sudo perl -i -p -e 's|$| init=/usr/lib/raspi-config/init_resize.sh  sdhci\.debug_quirks2=4|' $RASPROOT/boot/cmdline.txt

# Install the resize2fs_once script
echo "Enabling resize2fs_once"
sudo cp files/resize2fs_once $RASPROOT/etc/init.d
sudo chmod 755 $RASPROOT/etc/init.d/resize2fs_once
sudo chroot /mnt systemctl enable resize2fs_once

# Unmount the image
echo "Cleaning up the mounts and filesystems"
sudo umount /mnt/boot
sudo umount /mnt
sudo losetup -D

echo "Creating a zip file for the image"
zip -9 $image.zip $image
rm $image