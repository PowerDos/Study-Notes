# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块
# 可以持久化任何pickle可支持的python数据格式
import shelve

d = shelve.open('shelve_test')  # 打开一个文件

# 持久化过程
# info = {"age":21,"job":'IT'}
# name = ["Gavin", "male"]
# d["name"] = name  # 持久化列表
# d["info"] = info  # 持久化类

# 读出文件
print(d.get("name"))
print(d.get("info"))

d.close()