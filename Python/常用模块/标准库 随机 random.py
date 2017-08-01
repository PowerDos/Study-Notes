import random
# 随机产生1-3的随机整数
print(random.randint(1,3))
# randrange() 不包括最后一个数
print(random.randrange(1,3))
# 随机选取0到100之间的偶数
print(random.randrange(0,101,2))
# 随机浮点数 0-1
print(random.random())
# 随机区间的随机数
print(random.uniform(1,20))
# 随机字符
print(random.choice('abcdefg&ASD'))
# 多选字符中选取特定数量的字符
print(random.sample("asdasdasdasd",3))
# 随机选取字符串
print(random.choice(['asd', 'asdasd', 'asdasd', 'assdas']))
# 洗牌
items = [1,2,3,4,5]
print(items)
random.shuffle(items)
print(items)