import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    #摄像头预热2秒
    time.sleep(2)
    camera.capture('foo.jpg')
