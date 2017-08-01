# 系统模块
import os

# 获取当前目录
print(os.getcwd())

# 切换路径
# os.chdir("D:\\Python")
# os.chdir(r"D:\Python")

# 创建目录，不可递归
os.mkdir('dir4')

# 删除目录，不可递归
# 删除单级空目录，若目录不为空则无法删除，报错；
# 相当于shell中rmdir dirname
os.rmdir('dir4')

# 创建目录,可生成多层递归目录
os.makedirs('dir1/dir2/dir3')

# 删除目录，可递归
# 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.removedirs('dir1/dir2/dir3')

# 列出文件下的文件
# 返回一个列表
print(os.listdir('.'))

# 删除一个文件
# os.remove()

# 重命名文件/目录
# os.rename("oldname","newname")

# 获取文件/目录信息
print(os.stat('../for.py'))

# 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.sep)

# 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.linesep)

# 输出用于分割文件路径的字符串
print(os.pathsep)

# 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.name)

# 运行shell命令，直接显示
# print(os.system("time"))

# 获取系统环境变量
# print(os.environ)

# 返回路径规范化的绝对路径
print(os.path.abspath('.'))

# 将路径分割成目录和文件名二元组返回
print(os.path.split('D:\Python\PycharmProjects\笔记示例\常用模块'))

# 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname(os.getcwd()))

# 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.basename(os.getcwd()))

# 如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(os.getcwd()))

# 如果path是绝对路径，返回True
print(os.path.isabs(os.getcwd()))

# 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile(os.getcwd()))

# 如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(os.getcwd()))

# 返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime(os.getcwd()))
# 返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime(os.getcwd()))

# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略



