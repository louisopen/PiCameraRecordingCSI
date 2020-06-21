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
  printf "My service.sh IP address is %s\n" "$_IP"
fi

sudo python  /home/pi/status_i2c.py &
sudo python3 /home/pi/WebStreaming.py &
#sleep 1
cd $source_dir
exit 0
