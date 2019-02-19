# Author:GaoYuCai
import  socket
server=socket.socket()
server.bind(("localhost",6969))#绑定要监听端口
server.listen()#监听
print("我要开始等电话了")
conn,addr=server.accept()#等电话
#conn客户端连过来二=而在服务器端为期生成的实例
print("电话来了")
while True:
    data=conn.recv(1024)
    print("recv:",data.decode())
    conn.send(data.upper())
server.close()