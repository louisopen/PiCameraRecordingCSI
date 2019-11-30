#!/usr/bin/env python3
#coding=utf-8
#Python camera program on Raspberry pi Linux
#滾動式影像資訊儲存(四天)於USB disk

import io
import glob  
import os
import picamera
import logging
import datetime
import socketserver
#import WriteFilePath    #my WriteFilePath.py
from threading import Condition, Thread
from http import server

PAGE="""\
<html>
<head>
<title>picamera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<p>The UART default setting is 9600,N,8,1</p>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""
# <img src=%s width="140" height="80" /> % read(open('chick_medium.jpg','r'))

def check_disk_remove(stringPath):
    now = datetime.datetime.now()
    lastday = now - datetime.timedelta(days=4)     #4天前
    try:
        #$rm /media/pi/BACKUP/video/video051515* 
        #filelist = glob.glob(stringPath +'/video'+ lastday.strftime('%m%d*'))
        #for file in filelist:
        #    os.remove(file)
        filelist = glob.glob(stringPath + '/video*')
        for file in filelist:
            if file < str(stringPath + '/video' + lastday.strftime('%m%d*')):
                #print file
                os.remove(file)
    except Exception as e:
        logging.warning(e)

def pathMedia():    #存儲到外部USB裝置, 預先定義好USB Disk label:BACKUP
    #now = datetime.datetime.now()
    #PathMdeia = os.getcwd()+'/upload/'+ now.strftime('%Y%m%d') +'/'  #當前目錄+...
    #PathMdeia = os.getcwd()     #可以使用當前目錄下/Video...這樣就不用外掛USB Disk(如果你是玩玩)
    PathMdeia = '/media/pi/BACKUP'      #檔案存放在外掛USB disk目錄下 /BACKUP
    try:
        if os.path.isdir(PathMdeia):       
            #logging.warning('Here is the media')    #USB media + Driver name
            if os.path.isdir(PathMdeia +'/video'):
                logging.warning('Here have the media&path')    #USB media + Driver name
            else:
                os.makedirs(PathMdeia +'/video') 
                logging.warning('Create directory /video')    #USB media + Driver name

            check_disk_remove(PathMdeia +'/video')
            return PathMdeia +'/video'
        else:
            logging.warning('The media been change to /dev/null')
            return '/dev/null'
    except:
        logging.warning('been change to /dev/null')
        return '/dev/null'

class StreamingOutput(object): 
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()
        #self.output_file = io.open(filename, 'wb')
        #self.output_sock = sock.makefile('wb')
        self.lastime = datetime.datetime.now()

    def write(self, buf):
        self.nowtime = datetime.datetime.now()
        camera.annotate_text = self.nowtime.strftime('%Y-%m-%d %H:%M:%S')  #看到嵌入的時間走動
        try:
            if (self.nowtime-self.lastime).seconds > 120:
                #logging.warning(self.nowtime,self.lastime)
                print(self.nowtime,self.lastime)
                self.lastime = self.nowtime    
                #camera.split_recording('video'+ self.nowtime.strftime('%m%d%H%M%S') +'.h264', splitter_port=2) #另一port,儲存本地
                camera.split_recording(pathMedia()+'/'+'video'+ self.nowtime.strftime('%m%d%H%M%S') +'.h264', splitter_port=2) #另一port,儲存USB
        except:
            #logging.warning('Storage have some issue')
            print('Storage have some issue: %s'% e)

        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

    def flush(self):
        self.buffer.flush()
        #self.condition.flush()
        logging.warning('Here is flush')

    def close(self):
        self.buffer.close()
        #self.condition.close()
        logging.warning('Here is close')

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
            #WriteFilePath.write_IMG(content)   #Debug for saving
        elif self.path == '/stream.mjpg':       #http://ip:8000/stream.mjpg  資料流同時遠地下載 
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning('Removed streaming client %s: %s',self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()



class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):  #multi task 多線程
    allow_reuse_address = True
    daemon_threads = True
    
with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    #camera.led = True  #Camera模組上的紅色LED 關閉
    #camera.exif_tags['Artis'] = 'haha!'
    lastime = datetime.datetime.now()
    output = StreamingOutput()
    camera.rotation = 270   #rotation 0,90,180,270
    #camera.contrast = 50    #0~100 default:
    #camera.brightness = 65  #0~100 default:50
    #camera.image_effect = 'colorswap'
    #camera.awb_mode = 'sunlight'   #白平衡模式
    #camera.exposure_mode = 'beach' #瀑光
    #camera.quality = 23 #1~40(low) quality
    #camera.annotate_background = picamera.Color('blue')
    #camera.annotate_foreground = picamera.Color('yellow')
    camera.annotate_text_size = 32  #6~160 default:32
    
    camera.start_recording(output, format='mjpeg')  #default splitter_port=1

    #camera.start_recording('video'+ datetime.datetime.now().strftime('%m%d%H%M%S') +'.h264', format='h264', splitter_port=2, quality=30) #另一port,儲存本地     
    camera.start_recording(pathMedia()+'/'+'video'+ datetime.datetime.now().strftime('%m%d%H%M%S') +'.h264', format='h264', splitter_port=2, quality=30) #另一port,儲存USB
    #camera.start_recording('/dev/null', format='h264', splitter_port=2, quality=30, motion_output=stream)
    #camera.wait_recording(5)
    #logging.warning('Video start recording...')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
        camera.stop_recording(splitter_port=2)
