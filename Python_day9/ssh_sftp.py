# Author:GaoYuCai
import paramiko

transport=paramiko.Transport(('hostname',22))
transport.connect(username="root",password="gyc123")
sftp=paramiko.SFTPClient.from_transport(transport)
sftp.put("/tmp/localtion.py","/tmp/test.py")
sftp.get("remove_path","local_path")
transport.close()
