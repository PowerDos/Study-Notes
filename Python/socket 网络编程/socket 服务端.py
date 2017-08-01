# socket 服务器端
import socket
# 声明类型
server = socket.socket()
# 绑定端口
server.bind(('localhost',6969))
# 开始监听端口
server.listen()
print("开始监听")
# 等待请求, 并返回连接和对方地址
# conn 就是客户端连过来而在服务器为其生存的一个连接实例
conn,addr = server.accept()
print(conn,addr)
# 接收1024个字节
data = conn.recv(1024)
# 打印接收数据
print("recv:",data)
# 发送数据
conn.send("收到".encode(encoding='utf-8'))
# 关闭
server.close()


