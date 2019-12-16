import os
import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('', 9999))
s.listen(8)
while True:
    print('服务端等待连接')
    conn, addr = s.accept()
    while True:
        data = conn.recv(10240)
        if not data:
            break
        file_name = data.decode(encoding='utf-8',errors='ignore')  # 第一次接收的是对方发来的 文件名
        print('file_name:',file_name)
        conn.send('hi!'.encode())  # 发送给对方一个反馈，防止粘包
        data1 = conn.recv(10240)
        file_size = data1.decode(encoding='utf-8',errors='ignore')   # 第二次接收的是对方发来的文件大小
        print('file_size:',file_size)
        r_size = 0    # 初始化一个大小
        try:
            f = open(file_name, 'wb')
            while r_size < int(file_size):  # 不在接收数据的条件就是接收到的数据大小 = 文件大小
               data2 = conn.recv(10240)        # 第三次接收到的是对方发来的文件信息
               f.write(data2)
               r_size += len(data2)
               print('已接受file')
            f.close()
        except:
            print('错误写入')
            pass


