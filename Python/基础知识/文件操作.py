# 文件操作
# ################## 读文件 ################## #
# 打开文件 获取文件句柄
f = open('file.txt', 'r', encoding='utf-8')
# 读取文件
data = f.read()
data2 = f.read()  # 因为data时已经读完了，所以data2读不到什么东西
# print(data)
# print("data2:", data2)
# 关闭文件
f.close()

# ################## 写文件 ################## #

# 打开文件
f = open('file2', 'w', encoding='utf-8')
# 写文件
# f.write("天安门太阳升")
# 关闭文件
f.close()

# ################## 追加文件 ################## #
# 打开文件
f = open('file2', 'a', encoding='utf-8')
# 追加文件
# f.write("asdaasd\n")
# 关闭文件
f.close()

# ################## 逐行读文件readline ################## #
# 打开文件
f = open('file.txt', 'r', encoding='utf-8')
# 读前3行
for i in range(3):
    print(f.readline())
# 关闭文件
f.close()

# ################## 逐行读文件readlines ################## #
# 打开文件
f = open('file.txt', 'r', encoding='utf-8')
# 逐行打印
# readlines 只适合读小文件
for line in f.readlines():
    print(line)
# 关闭文件
f.close()

# ################## 逐行读文件跳过第10行 ################## #
# 低级写法
# 打开文件
f = open('file.txt', 'r', encoding='utf-8')
# 逐行打印
# readlines 会把整个文件读到内存，消耗空间，不建议用
for index, line in enumerate(f.readlines()):
    if index == 9:
        print('我是第十行')
        continue
    print(line)
# 关闭文件
f.close()

# 高级写法
f = open('file.txt', 'r', encoding='utf-8')
count = 0
# line in f 会一行一行读进内存，然后再一行一行从内存删除
# 也就是只读一行在内存中
for line in f:
    if count == 9:
        print("我是第10行")
        count += 1
        continue
    print(line)
    count += 1
f.close()

# ################## 读文件并移光标 ################## #
f = open("file.txt", 'r', encoding='utf-8')
# tell是记录一个一个字符移的当前位置
print(f.tell())
print(f.readline())
print(f.tell())
# seek 移动位置到10的位置
f.seek(10)
print(f.readline())
f.close()

# ################## 文件其他操作 ################## #
f = open("file.txt", 'r', encoding='utf-8')
# 读取文件编码
print(f.encoding)
# 读取IO接口号
print(f.fileno())
# 读取文件名
print(f.name)
# 因为有些文件是不能移动的，所以可以用seekbale判断是否可以移动
print(f.seekable())
# 一般写文件都会，先存到缓存文件，然后达到一定数量再一次性存入
# 强制刷新，把缓存的东西强制存储保存
f.flush()
# 文件截断，从文件头开始截
# f.truncate(10)

# ################## 文件读写 ################## #
# 读写 写是追加 ，比较常用
f = open("file.txt", 'r+', encoding='utf-8')
print(f.readline())
# 写在最后面
f.write("_______end__________")
f.close()

# 写读 无法移位写  写读应用场景比较少
f = open("file.txt", 'w+', encoding='utf-8')
print(f.readline())
f.write("_______end__________")
f.close()

# 追加读 也不怎么常用
f = open("file.txt", 'a+', encoding='utf-8')
print(f.readline())
f.write("_______end__________")
f.close()

# 读取二进制文件 应用场景：网络传输
f = open("file.txt", "rb")
print(f.readline())
f.close()

# 写二进制文件 应用场景：网络传输
f = open("file.txt", "wb")
f.write("hello binary\n".encode("utf-8"))
f.close()

# ################## 文件修改 ################## #
# 一般修改完再替换文件并删除临时文件
f = open("file.txt", "r", encoding="utf-8")
f_new = open("file.bak", "w", encoding="utf-8")
for line in f:
    if "仿佛昔日又重来" in line:
        line = line.replace("仿佛昔日又重来", "改变")
    f_new.write(line)
f.close()
f_new.close()

# ################## with自动关闭文件 ################## #
# 自动关闭文件 py3支持用with打开多文件
with open("file.txt", "r", encoding="utf-8") as f,\
        open("file", "w", encoding="utf-8"):
    for line in f:
        print(line)








