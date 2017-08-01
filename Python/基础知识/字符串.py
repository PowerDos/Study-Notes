# 字符串
name = 'my name is Gavin'
# 查找
print(name.find("n"))
# 字符串剪切
print(name[name.find("name"):])
# 判断是否是阿拉伯数字
print(name.isalnum())
# 判断是否是合法变量名
print(name.isidentifier())
# 判断是否是标题(及首字母是否是大写)
print(name.istitle())
# 字符串连接
print("-".join(['1', '2', '3']))
# 不足长度后面补全
print(name.ljust(50, "*"))
# 不足长度前面补全
print(name.rjust(50,"*"))
# 去掉空白符
print("\tname\n".lstrip())  # 去掉左边空白符
print("\tname\n".rstrip())  # 去掉右边空白符
print("  name   is ".strip())  # 去掉两边空白符
# 字符转换
p = str.maketrans("abcdef", "123456")
print("name is Gavin".translate(p))
# 字符串替换
print("name is Gavin".replace("name", "NAME"))
# 将字符串按某个字符分割成列表
print("name,is,Gavin".split(","))
# 大小写转换
print("Name IS gAVIN".swapcase())


