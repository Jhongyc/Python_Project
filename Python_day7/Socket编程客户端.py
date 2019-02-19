# Author:GaoYuCai
import socket
client=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
client.connect(("localhost",6969))#只接受一个参数，那就传入一个元组
client.send(b"Hello World!")
data=client.recv(1024)
print("client_rev_data:",data)
client.close()
