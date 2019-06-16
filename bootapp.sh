#!/bin/sh 
#This bash called by /home/pi/.config/autostart/autoboot.desktop
jump_dir=/home/pi/PiCameraRecordingCSI
#tr -d "\r" < oldname.sh > newname.sh   #if you can't cd to .... just do this command.
cd $jump_dir
pwd
sudo python3 $jump_dir/WebStreaming.py

exit 0