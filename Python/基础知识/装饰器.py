# 装饰器 : 本质是函数,（装饰其他函数）
# 其他函数添加附加功能
# 原则: 1. 不能修改被装饰的函数的源代码
#       2. 不能修改被装饰的函数的调用方式
# 实现装饰器知识储备：
# 1.函数即"变量"
# 2.高阶函数
# 3.嵌套函数
import time
# ###################装饰器原理1###################### #
# 1.函数即"变量"
# 但违反了调用bar的方式
# 但实现了在不修改被装饰的函数的源代码的情况下为添加附加功能
def bar():
    time.sleep(1)
    print("running bar")


def decorate(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print("程序运行时间:%s" % (stop_time-start_time))

decorate(bar)

# ####################装饰器原理2####################### #
# 2.高阶函数
def bar():
    time.sleep(1)
    print("running bar")


def decorate(func):
    print(func)
    return func

bar = decorate(bar)
bar()


# ####################装饰器原理3####################### #
# 3.嵌套函数
def foo():
    print("running in foo")
    def bar():
        print("running in bar")
    bar()

foo()

# ------------------------------------------------------ #

# 装饰器-初级 实例1
def timer(func):
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        print("程序运行时间:%s" % (stop_time-start_time))
    return deco

@timer  # demo = timer(demo)
def demo():
    time.sleep(1)
    print("running in demo")

# ------------------------------------------------------ #

# 装饰器-进阶 实例2
def timer(func):
    # 这样如果装饰函数有传参的话就可以用这样做
    def deco(*args,**keys):
        start_time=time.time()
        func(*args,**keys)
        stop_time=time.time()
        print("程序运行时间:%s" % (stop_time-start_time))
    return deco


@timer # demo = timer(demo)
def demo(name):
    time.sleep(1)
    print("running in demo",name)

demo("Gavin")

# ------------------------------------------------------ #

# 装饰器-高级 实例3
user,passwd = 'Gavin','abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args, **kwargs)  # from home
                    print("---after authenticaion ")
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("搞毛线ldap,不会。。。。")

        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")
@auth(auth_type="local") # home = wrapper()
def home():
    print("welcome to home  page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs  page")

index()
print(home()) #wrapper()
bbs()
# ------------------------------------------------------ #


