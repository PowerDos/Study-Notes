import os
# 执行系统命令 成功返回0，失败返回1
# 会自动输出
os.system("dir")
# 执行命令保存结果，不会自动输出
cmd_res = os.popen("dir").read()
print("-->", cmd_res)
# 新建目录
os.mkdir("测试目录")
