import time
# 列表生成式 主要是让代码跟简介
# 列表，一次性生成，放在内存，占用太多空间
list = [ i*2 for i in range(10)]
print(list)

# 杂项
# a, b = b, a+b
# 实际为
# t = (b, a+b)
# a = t[0]
# b = t[1]
a = 1
b = 2
a, b = b, a+b
print(a,b)

# 生成器
# 只有在调用时才会生成相应的数据

# 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator


# 生成器只能一个一个的取，不能取上一个
# 只有一个__next__() 方法


g = ( i*2 for i in range(100000))
print(g)
print(g.__next__())
print(g.__next__())

# 斐波拉契数列的推算
# 函数中包含yield关键字，这个函数就不再是一个普通函数，而是一个generator
# 函数是顺序执行，遇到return 时才结束
# 但generator是，在没次调用__next__()的时候执行，遇到yield语句时返回
# 再次执行时从上次返回的yield语句出继续执行
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield  b
        a,b = b,a+b
        n += 1
    return 'done'

f = fib(100)
print(f.__next__())
print("执行其他的再去执行fib的下一个")
print(f.__next__())


# 并行实例
# 通过生成器可以实现并行效果，可以做到在单线程中并发
# 生产者消费者模型
# send 也是调用yield ,但同时可以给yield传值

def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
       baozi = yield
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("Gavin")







