# __author__ = 'Gavin'
import sys
import time
# 打印环境变量
print(sys.path)
# 打印本脚本绝对路径
print(sys.argv)
# 标准输出 不换行
for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)

