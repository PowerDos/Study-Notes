# socket 客户端 shh
import socket
client = socket.socket()
# 连接
client.connect(('localhost',9999))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0 :continue
    client.send(cmd.encode(encoding='utf-8'))
    resLen = client.recv(1024)
    print("命令长度",resLen)
    received_size = 0
    while received_size < int(resLen):
        data = client.recv(1024)
        received_size += len(data)
        print(data.decode(encoding='utf-8'))
client.close()














