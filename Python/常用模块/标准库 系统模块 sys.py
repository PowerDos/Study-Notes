# sys模块
import sys
# 命令行参数List，第一个元素是程序本身路径
# 可以读取传入的参数
print(sys.argv)

# 退出程序，正常退出时exit(0)
# sys.exit(n)

# 获取Python解释程序的版本信息
# sys.version

# 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)

# 返回操作系统平台名称
print(sys.platform)

# sys.stdout.write('please:')
# val = sys.stdin.readline()[:-1]