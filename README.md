### Pi Camera Web Streaming and Recording to staore in files on CSI interface
直接使用RaspBian自帶庫(picamera)指令來控制攝像頭模組(CSI interface)。也可以直接在Python程序控制Pi Camera視頻, 同時將視頻流以每兩三分鐘儲存成一個檔案或存到外部存除裝置, 這個庫有許多配置，可以改變亮度，對比度，影象效果，曝光模式等...這樣除了有瀏覽遠端攝像頭之外還有非常流行的行車記錄儀功能或公共場所之監控功能.

往後可自行加強增修它的移動偵測功能, 不用持續再持續性錄影, 以節省記憶體體空間;
加強它的節電控制功能, 就可以達到移動偵測攝影的目的如夜行性動物攝影;
增強輔助功能如燈控, 如雲台控制...;

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8
### 庫文件
picamera 庫文件(Raspberry Pi專有)記得安裝

sudo apt-get update

sudo apt-get install python3-picamera  #前一版... python-picamera

### Python程序用法：(匯入相關模組)
import picamera

from time import sleep

camera = picamera.PiCamera()    #初始化對象

camera.annotate_text = "Hello world"    #嵌入文字

camera.annotate_text_size = 32  #6~160 default:32

camera.resolution = (1024, 768) #解析度(長,寬)

camera.capture(‘image.jpg’) #捕獲影象存檔

camera.vflip = True #垂直翻轉

camera.hflip = True #水平翻轉

camera.rotation = 270   #0,90,180,270 另一種方法翻轉

camera.contrast = 50    #0~100 default:  對比度

camera.brightness = 65  #0~100 default:50 攝像頭亮度

camera.image_effect = 'colorswap'

camera.awb_mode = 'sunlight'   #白平衡模式

camera.exposure_mode = 'beach' #瀑光

camera.quality = 23 #1~40(low) quality品質

camera.annotate_background = picamera.Color('blue') #嵌入圖像底色

camera.annotate_foreground = picamera.Color('yellow')

camera.start_preview()  #開啟預覽

camera.start_recording(‘video.h264’)    #控制攝像頭錄影存檔

camera.start_recording(output, format='mjpeg')  #含視頻流控制

camera.start_recording('video'+ datetime.datetime.now().strftime('%m%d%H%M%S') +'.h264',format='h264', splitter_port=2, quality=30)  #視頻流存檔

camera.split_recording('video'+ self.nowtime.strftime('%m%d%H%M%S') +'.h264', splitter_port=2) #視頻流分割存檔


sleep(5)    #程式休眠，但攝像頭繼續工作

camera.stop_recording() #停止錄影

