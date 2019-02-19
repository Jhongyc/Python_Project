# Author:GaoYuCai
import socket
import os
server=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
server.bind(("localhost",6969))
server.listen()
print("Watting....")
conn,addr=server.accept()
print("Get....")
while True:
    data=conn.recv(1024)
    if not data:
        print("client has lost...")
        break
    res=os.popen(data.decode()).read()
    conn.send(res)

server.close()




