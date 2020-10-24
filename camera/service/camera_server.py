import socket
import subprocess

# 首先我们创建一个socket监听，端口为8000，接受所有的ip连接
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen(0)

# 获取摄像头数据


def get_data():
    # 然后我们创建一个socket文件流
    connection = server_socket.accept()[0].makefile('rb')
    try:
        # 如果接受到一个客户端连接，那么我们将通过终端来打开一个播放器。
        # 如果你使用的是mplayer，则需要注释掉vlc这段。
        cmdline = ['D:/Program Files/VideoLAN/VLC/vlc.exe',
                   '--demux', 'h264', '-']
        # cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
        player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
        while True:
            # 创建一个死循环，每次读取1k的数据
            # 然后将数据传送到播放器
            data = connection.read(1024)
            if not data:
                break
            player.stdin.write(data)
    finally:
        connection.close()
        server_socket.close()
        player.terminate()


if __name__ == "__main__":
    get_data()
