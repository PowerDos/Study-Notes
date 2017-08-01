# 面向对象 多态
# 继承可以扩展已存在的代码模块（类），它们的目的都是为了——代码重用。
# 而多态则是为了实现另一个目的——接口重用
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


def func(obj):  # 一个接口，多种形态
    obj.talk()


c1 = Cat('小明')
d1 = Dog('李明')

func(c1)
func(d1)





























