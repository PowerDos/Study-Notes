# all 如果里面有个为假就返回假
print(all([1,-5,3]))
print(all([0,1,1]))


# any 如果里面有一个为真就返回真
print(any([1,0,0]))
print(any([0,0,0]))


# 十进制转二进制
print(bin(100))


# 十进制转十六进制
print(hex(100))


# 十进制转八进制
print(oct(100))


# filter 过滤，得出大于5的数
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)


# reduce 一个一个加起来
import functools
res1 = functools.reduce( lambda x,y:x+y,range(10))
print(res1)


# frozenset
# 把列表变成不可变的
a = frozenset([1,2,3])
print(a)


# globals
# 返回当前文件所有的key:value，可以用来获取变量，也可判断一个变量存不存在
print(globals())


# locals
# 返回局部变量
def Lo():
    de = "ccc"
    print(locals())
Lo()


# hash 哈希
# 生成映射关系
# 同一个解释器进程中的hash映射值一样
print(hash("asda"))
print(hash("asda"))
print(hash("asda"))
print(hash("asda"))


# round 精确度
# 保存小数点后两位，四舍五入
print(round(1.33533,2))


# sorted 排序
a = {1:"a", 3:"c", 2:"b"}
print(a)
print(sorted(a)) # 对KEY进行排序
print(sorted(a.items())) # 对值进行排序


# zip 组合，拉链
# 返回迭代器
a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']
for i in zip(a,b):
    print(i)


# 因为import识别不了字符串，特定场合可以用__import__导入
__import__('decorator')










