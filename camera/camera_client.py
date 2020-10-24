import socket
import time
import picamera

# 创建一个socket连接，来连接我们的服务器，这里需要将my_server替换成服务器的ip
client_socket = socket.socket()
client_socket.connect(('192.168.1.107', 5000))

# 创建一个socket文件流
connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        # 开启摄像头，并预热两秒
        camera.start_preview()
        time.sleep(2)
        # 开始录制并传输，录制视频总长度为60秒
        camera.start_recording(connection, format='h264')
        camera.wait_recording(60)
        camera.stop_recording()
finally:
    connection.close()
    client_socket.close()
