# 面向对象
# Class 类
# Object 对象
# Encapsulation 封装
# Inheritance 继承
# Polymorphism 多态


# class Person: 经典类
# class Person(object): 新式类
# 在Python 2.x 经典类是按深度优先来继承的，新式类是按广度优先继承的
# 在Python 3.x 经典类和新式类都是用广度优先继承
class Person(object):
    n = 123 # 类变量,对象没有单独改变的时候是共用的，节省开销
    __g = 333 # 变量前加'__'变成私有属性
    # 构造函数 __init__
    # 在实例化时做一些类的初始化工作
    def __init__(self,name,age):
        self.name = name # 每个对象一份
        self.__age = age # 变量前加'__'变成私有属性

    def showPrivate(self):
        print("访问私有属性:",self.__age,self.__g)

    # 私有方法
    def __PrivateFunc(self):
        print("I am private Func")

    def say(self):
        print("Hello World！%s" % self.name)

    def fly(self):
        print("funny fly")

    # 析构函数
    def __del__(self):
        print("stopping...")


class Relation(object):
    def make_friends(self,obj):
        print("%s is making friends with %s" % (self.name,obj.name))


# 多继承 Preson,Relation
class Male(Person,Relation):
    # 重构构造方法
    def __init__(self,name,age,sex):
        # Person.__init__(self,name,age)  方法一
        # 方法二，建议使用，防止父类名字改变然后需要全部改变
        # 还有个好处是，多继承的时候，只需要写一个，但方法二要写多个继承
        super(Male,self).__init__(name,age)
        self.sex = sex

    def sleep(self):
        print("I am sleepping")
    # 重写父类
    def say(self):
        print("I am Saying")
    # 重构父类方法
    def fly(self):
        Person.fly(self)
        print("I am flying")

d1 = Person('Gavin','21')
d1.say()
print(d1.n)
# 访问私有属性
d1.showPrivate()

# 当对象不会再使用时，可以自己删除
del d1

print("\n##################################\n")

# Male 对象
man = Male("Gavin","21","male")
man.sleep()
man.say()
man.fly()


print("\n###############多继承###############\n")

m = Male("小明","23","male")
m.make_friends(man)














