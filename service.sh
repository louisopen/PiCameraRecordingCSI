#!/bin/bash
#This bash called by autoboot.desktop or rootcron   #autoboot.desktop存放到/home/pi/.config/autostart/
#chmod =777 autoboot.desktop
#
#tr -d "\r" < autorun.sh > newname.sh    #if you can't cd to .... just do this command. #置入新系統時若發生此訊息
#tr -d "\r" < autorun.sh > newname.sh    #if you got ...Syntax error: end of file unexpected (expecting "then")
#mv newnme.sh autorun.sh
#chmod =711 autorun.sh

#sudo nano .bashrc   	#最後行添加 sh autorun.sh  同時(近端/遠端)啟動
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

#su pi
source_dir=$PWD
#jump_dir=/home/pi/BCON_X1608
jump_dir=/home/pi/BCON_X1716
#jump_dir=/home/pi/BCON_X1719
#jump_dir=/home/pi/WebServer
cd $jump_dir

#python ./rpi_webservice.py &
#python3 /home/pi/WebServer/app.py &
python ./app.py &
#sleep 1
cd $source_dir
exit 0
