# 面向对象进阶 异常处理

print("####################系统自带异常####################\n")
# 缩进错误只能自己去看，因为程序解释不了，不能抓
name = {'name':'Gavin','age':'21'}
list = ['1','2']
try:
    print(name['sex'])
    print(list[1])
except KeyError as e:
    print("没有这个下标值",e)
except IndexError as e:
    print("列表下标错误",e)
# 也可以这样写，但不知是哪个出错
# except (KeyError,IndexError) as e:
# 抓住所以所有异常，不建议使用，因为不知道哪里出错
# 但可以放在最后面，抓住我们以预防的错误以外的错误
except Exception as e:
    print("捕获未知错误")
# 但没有错误的时候执行else
else:
    print("一切正常")
# 不管有没有错都执行finally
finally:
    print("不管有没有错都执行")



print("\n####################自定义异常####################\n")

class OwnException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        # 返回异常信息
        return self.message

try:
    # 自己抛出异常
    # 自定义的异常只能自己抛出
    raise OwnException("数据库连不上")
except OwnException as e:
    print(e)



# 常见异常
# AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError 输入/输出异常；基本上是无法打开文件
# ImportError 无法引入模块或包；基本上是路径问题或名称错误
# IndentationError 语法错误（的子类） ；代码没有正确对齐
# IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError 试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError 使用一个还未被赋予对象的变量
# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError 传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError 传入一个调用者不期望的值，即使值的类型是正确的























