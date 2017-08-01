# 函数
def fun1():
    print("function")
    return 0
# x = fun1()


# 过程
def fun2():
    print("过程")
    # 默认返回None
# y = fun2()


# 参数
def fun3(x, y):
    print(x)
    print(y)
# 普通调用
fun3(1, 2)
# 关键字调用
fun3(y=3, x=9)
# 关键字不能写在位置参数之前
# 比如 fun3(x=9, 3)


# 默认参数
def fun4(x,y=2):
    print(x)
    print(y)

fun4(4, 6)
fun4(6)

# 局部变量


def change_name(name):
    print("name:", name)
    name = "gg"
    print("name1:", name)

name = "Gavin"
change_name(name)
print(name)


# 改全局变量
name = "Xiao"


def change():
    global name
    name = "Ming"
    print("g:", name)

change()
print(name)

# 只有整形，字符串之类的不能再函数里面被改，但列表，数组之类的可以在函数里面被改
# 高阶函数 函数参数是函数
# a.把一个函数名但参数
# b.把一个函数当返回值
def add(a, b, f):
    return f(a)+f(b)

result = add(-10, 19, abs)
print(result)


# 非固定参数
# *args会把多传入的参数变成一个元组的形式
# **keys 会把多传入的参数变成字典dict
def indist(names, age, *args, **keys):
    print("姓名：", names, "年龄:", age, "字典：", args, "列表：", keys)

key = {"key1": 1, "key2": 2}
indist("Gavin", "20", key, "a", "b", sex="male", color="red")


# 匿名函数
calc = lambda x:x*3
print(calc(3))

# lambda 是定义匿名函数，n是传入参数
a = lambda n:print("ccc",n)
a(1)