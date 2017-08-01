# socket 客户端
import socket
# 什么socket类型，同时生成socket连接对象
client = socket.socket()
# 连接设备
client.connect(('localhost',6969))
# 发送数据
client.send(b"Hello World")
# 接收数据,接收1024个字节
data = client.recv(1024)
print("recv:",data.decode(encoding='utf-8'))
# 关闭客户端
client.close()


