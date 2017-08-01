# 多线程 继承调用
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        print("running on number:" ,self.num)

        time.sleep(3)

t1 = MyThread(1)
t2 = MyThread(2)
t1.start()
t2.start()

















