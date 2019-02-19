# Author:GaoYuCai
import  paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="192.168.80.111",port=22,username="root",password="gyc123")
stdin,stdout,stdrr=ssh.exec_command("df -h")
result=stdout.read()
print(result.decode())
ssh.close()
