# Author:GaoYuCai
import  socket
server=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
server.bind(("localhost",6969))#绑定要监听的端口
server.listen()#监听
print("我要开始等电话了")
conn,addr=server.accept()#等待电话打进来
print("电话来了")
data=conn.recv(1024)
print("server_rev_data",data)
conn.send(b"OK!")