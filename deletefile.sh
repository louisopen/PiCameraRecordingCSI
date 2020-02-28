#!/bin/sh
#Bash location="/home/pi/"
#crontab -e
#*/60 * * * * /bash/sh /home/pi/deletefile.sh    #every 60 minutes running

PATHNAME=/media/pi/BACKUP/video
FILENAME="video*.h264"
DELDAY=3        #4 day

#find directory
#-mtime +4
#file name list
#rm -f deleted files

find $PATHNAME -name $FILENAME -type f -mtime +$DELDAY                 #list file for rm & temp.log
#find $PATHNAME -mtime +$DELDAY -type f -name $FILENAME
#find $PATHNAME -mtime +$DELDAY -type f -name $FILENAME |xargs rm -f
find $PATHNAME -name $FILENAME -type f -mtime +$DELDAY -exec rm {} \;   #rm
#find $PATHNAME -name $FILENAME -type f -mtime +$DELDAY -exec rm {} \; >/dev/null 2>&1
