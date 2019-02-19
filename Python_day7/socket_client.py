# Author:GaoYuCai
import socket
client=socket.socket()#声明sock类型，同时生成链接
client.connect(("localhost",6969))
while True:
    #send发不了空
    msg=input(">>:".strip())
    client.send(msg.encode())
    data=client.recv(1024)#字节
    print("recv:",data)
client.close()
