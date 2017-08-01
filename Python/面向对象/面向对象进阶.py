# 面对对象进阶
class Person(object):
    '''
    面向对象进阶
    '''
    className = "Gavin"
    def __init__(self,name):
        self.name = name

    @staticmethod  # 静态方法，实际上跟类无关系，单纯的函数
    def eat():
        print("%s is eatting %s" % ("Gavin","banana"))

    @classmethod # 类方法，只能访问类变量，不能访问实际变量
    def talk(self):
        print("%s is talking" % self.className)


    #把一个方法变成静态属性有什么卵用呢？既然想要静态变量，那直接定义成一个静态变量不就得了么？
        # well, 以后你会需到很多场景是不能简单通过 定义 静态属性来实现的，
        # 比如 ，你想知道一个航班当前的状态，是到达了、延迟了、取消了、还是已经飞走了，
        #  想知道这种状态你必须经历以下几步:
            # 1. 连接航空公司API查询
            # 2. 对查询结果进行解析
            # 3. 返回结果给你的用户
        # 因此这个status属性的值是一系列动作后才得到的结果，所以你每次调用时，
        # 其实它都要经过一系列的动作才返回你结果，但这些动作过程不需要用户关心，
        #  用户只需要调用这个属性就可以，明白 了么？
    @property #把一个方法编程静态属性
    def sleep(self):
        print("%s is sleepping" % self.name)

    @sleep.setter # 可以给sleep这个方法赋值
    def sleep(self,where):
        print("%s is sleepping in %s " % (self.name,where))

    def run(self):
        print("%s is running" % self.name)
    def __call__(self, *args, **kwargs):
        print("__call__方法")

p = Person("Gavin")
p.eat()
p.talk()
p.sleep
p.sleep = "bed"
# 打印类说明的注释
print("\n打印类说明的注释--->",p.__doc__)
# 打印p对象在哪个模块里
print("\n打印p对象在哪个模块里 -> ",p.__module__)
# 输出类本身
print("\n输出类本身 -> ",p.__class__)

# * __call__方法
p()

# 查看类中的所有成员,通过类去调用，调用类中的所以成员
print("\n通过类去查看成员:\n",Person.__dict__)
# 通过实例化对象去调用，通过对象去调用，调用被示例成员6
print("通过对象去查看成员:\n",p.__dict__,"\n")



















