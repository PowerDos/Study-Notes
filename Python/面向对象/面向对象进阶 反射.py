# 面向对象进阶 反射
class Person(object):
    def eat(self):
        print("I am eatting")


# 实例化对象
p = Person()
print("======================反射======================")
# 判断是否存在方法 hasattr(obj,name_str)
# 动态调用方法 getattr(obj,name_str)
# 动态添加方法 setattr(obj,key,value)
# 动态删除方法 delattr(obj,name_str)
def sleep():
    print("I am sleepping")
# 通过输入去调用函数
choice = input("please input func name:").strip()
# 先判断是否存在这个函数
print(hasattr(p,choice))
if hasattr(p,choice):
    # 如果存在就调用函数
    func = getattr(p,choice)
    # 一般会先赋值再调用，是因为有些方法需要传参，
    # 无参也可以这样写 getattr(p,choice)()
    func()
else:
    if choice == "sleep":
        setattr(p,choice,sleep)
        p.sleep()
    else:
        # 动态添加属性
        setattr(p,choice,22)
        print(getattr(p,choice))
        print(hasattr(p, choice))
        # 删除方法
        delattr(p,choice)
        print(hasattr(p,choice))
































