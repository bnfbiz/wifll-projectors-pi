sudo raspi-config
ipconfig
ifconfig
cd /etc
ls
sudo mv dhcpcd.conf /boot/
set -o vi
sudo mv -f dhcpcd.conf /boot/
ls
ls /boot/dhcpcd.conf 
ls -s /boot/dhcpcd.conf dhcpcd.conf
sudo ls -s /boot/dhcpcd.conf dhcpcd.conf
sudo ln -s /boot/dhcpcd.conf dhcpcd.conf
sudo vi /boot/dhcpcd.conf 
sudo shutdown -r now
sudo apt-get purge libreoffice wolfram-engine sonic-pi scratch
sudo apt-get clean
sudo apt-get autoremove
ls
sudo apt-get update
set -o vi
sudo apt-get upgrade
sudo apt-get install libdbus-1-dev
sudo apt install python3-pip
pip3 install omxplayer-wrapper
pip3 install pygame
mkdir ~/.ssh
chmod 700 ~/.ssh
vi ~/.ssh/authorized_keys
scp 192.168.123.27:.ssh/id* .ssh
sudo vi /etc/hosts
cat /sys/module/kernel/parameters/consoleblank
sudo vi /boot/cmdline.txt
vi .profile 
cat >>~/.bashrc <<EOFMARK

set -o vi
EOFMARK

scp projector-pi-7:loginscript.sh .
scp projector-pi-7:FLLLogo* .
scp -r projector-pi-7:projector-scripts/ .
vi loginscript.sh 
vi projector-scripts/fll-flip-projectors.py 
less  projector-scripts/fll-flip-projectors.py 
cd projector-scripts/
grep serverSock.sendto *.py
vi ../loginscript.sh 
vi fll-projectors-4.py 
sudo shutdown -r now
sudo shutdown -h now
ls
cd projector-scripts/
ls
vi *projectors*
grep FLLLogo *
vi dualcamera.sh 
vi fll-projectors-4.py 
sudo raspi-config
vi fll-projectors-4.py 
sudo shutdown -h now
ifconfig
shutdown -r now
ps auxw|grep ssh
ssh 192.168.123.21
cd /var/log
ls
less syslog
ls
grep ssh *
less syslog
cd /boot
ls
grep ssh /var/log/*
less /var/log/syslog
touch ssh
sudo touch ssh
shutdown -r now
sudo raspi-config
sudo shutdown -r now
ls
mv FLLLogo7.png FLLLogo2022.png
cd projector-scripts/
grep 2021 *
vi *
sudo shutdown -h now
ls
cd projector-scripts/
ls
cat camera-control.py 
ls
cd
ls
rm FLLLogo[12345].png
ls
ls Music/
rmdir Music/
ls Pictures/
rmdir Pictures/
ls Videos/
rmdir Videos/
ls
ls Documents/
rmdir Documents/
rmdir Downloads/
rmdir Bookshelf/
ls Bookshelf/
rm -r Bookshelf/
ls
ls Desktop/
rmdir Desktop/
ls Templates/
ls
rmdir Templates/
ls
ls Public/
ls
rmdir Public/
ls
cat loginscript.sh 
ls
cd projector-scripts/
ls
ls backups/
rm -r backups/
ls
rm FLLLogo5.png 
ls
less beta-projectors.py 
rm beta-projectors.py 
ls
cat camera-control.py 
ls
sudo shutdown -h now
vi loginscript.sh 
vi projector-scripts/fll-flip-projectors.py 
ls
ls projector-scripts/
scp loginscript.sh projector-pi-10:.
scp projector-scripts/fll-flip-projectors.py projector-pi-10:projector-scripts/
vi projector-scripts/fll-flip-projectors.py 
sudo shutdown -h now
