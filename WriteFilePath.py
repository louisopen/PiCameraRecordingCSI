#!/usr/bin/env python
#coding=utf-8
import datetime
import os
#filePath = "/home/pi/camera/DCIM/"
def write_CSV(str):
    #獲得當前系統時間的字串
    localtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    year = datetime.datetime.now().strftime('%Y')  #年
    month = datetime.datetime.now().strftime('%m') #月
    day = datetime.datetime.now().strftime('%d') #日

    filePath = os.getcwd()+'/upload/'+ year +'_'+ month +'/day'+ day +'/'  #當前目錄+...
    fileName = year +'_'+ month +'_'+day + '.csv'
    try:
      if not os.path.exists(filePath):
        os.makedirs(filePath)
        out=open(filePath + fileName,'w')   #建立一個檔案寫入
      else:
        out=open(filePath + fileName,'a')   #建立或添加在檔案
    except Exception as e:
      print(e)
    finally:
  
    print(filePath + fileName)
    #在該檔案中寫入當前系統時間字串
    out.write(localtime +'_'+ str + '\r\n')
    out.close()
    return

def write_userLog(str):
    #獲得當前系統時間的字串
    localtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    year = datetime.datetime.now().strftime('%Y')  #年
    month = datetime.datetime.now().strftime('%m') #月
    day = datetime.datetime.now().strftime('%d') #日

    filePath = os.getcwd()+'/upload/'+ year +'_'+ month +'/day'+ day +'/'  #當前目錄+...
    fileName = 'user'+year +'_'+ month +'_'+day + '.txt'
    try:
      if not os.path.exists(filePath):
        os.makedirs(filePath)
        out=open(filePath + fileName,'w')   #建立一個檔案寫入
      else:
        out=open(filePath + fileName,'a')   #建立或添加在檔案
    except Exception as e:
      print(e)
    finally:
      
    print(filePath + fileName)
    #在該檔案中寫入當前系統時間字串
    out.write(localtime +'_'+ str + '\r\n')
    out.close()
    return

def write_myLog(str):
    #獲得當前系統時間的字串
    localtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    year = datetime.datetime.now().strftime('%Y')  #年
    month = datetime.datetime.now().strftime('%m') #月
    day = datetime.datetime.now().strftime('%d') #日

    filePath = os.getcwd()+'/upload/'+ year +'_'+ month +'/day'+ day +'/'  #當前目錄+...
    fileName = 'log_'+year +'_'+ month +'_'+day + '.txt'
    try:
      if not os.path.exists(filePath):
        os.makedirs(filePath)
        out=open(filePath + fileName,'w')   #建立一個檔案寫入
      else:
        out=open(filePath + fileName,'a')   #建立或添加在檔案
    except Exception as e:
      print(e)
    finally:

    print(filePath + fileName)
    #在該檔案中寫入當前系統時間字串
    out.write(localtime +'_'+ str + '\r\n')
    out.close()
    return
