# socket 服务端 shh
import socket
import os
server = socket.socket()
# 绑定端口
server.bind(('localhost',9999))
# 开始监听
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令：",data)
        # 发送指令
        cmd_res = os.popen(data.decode(encoding='utf-8')).read()
        if len(cmd_res) <= 0:
            cmd_res = "DOS无返回值"
        # 注意中文encode后占三个字节
        conn.send(str(len(cmd_res.encode(encoding='utf-8'))).encode(encoding='utf-8'))
        conn.send(cmd_res.encode(encoding='utf-8'))
        cmd_res = ""
server.close()











