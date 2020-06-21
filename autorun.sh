#!/bin/bash
#This bash called by autoboot.desktop or rootcron   #autoboot.desktop存放到/home/pi/.config/autostart/
#chmod =777 autoboot.desktop
#
#tr -d "\r" < autorun.sh > newname.sh    #if you can't cd to .... just do this command. #置入新系統時若發生此訊息
#tr -d "\r" < autorun.sh > newname.sh    #if you got ...Syntax error: end of file unexpected (expecting "then")
#mv newnme.sh autorun.sh
#chmod =755 autorun.sh
#
#sudo nano .bashrc   	#最後行添加 sh autorun.sh  同時(近端/遠端)啟動
#
source_dir=$PWD
#jump_dir=/home/pi/T29
#jump_dir=/home/pi/T60
#jump_dir=/home/pi/T40
#cd $jump_dir

#sleep 1
#python $jump_dir/T29_main.py
#python $jump_dir/T60_main.py
#python $jump_dir/T40_main.py
cd $source_dir
exit 0
