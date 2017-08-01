# 迭代器
# 可以直接作用于for循环的对象叫做可迭代对象
# 可以被next()函数调用并不断返回下一个值得对象称为迭代器：Iterator
# 迭代器和可迭代对象不同
# list、dict、str虽然是可迭代对象，但却不是迭代器
# 但可以用iter()把，list、dict、str变成迭代器
# range(返回的就是迭代器),所以比较快
# 底层很多东西都是用迭代器，但由于python的封装，我们很多时候用的都感觉不是迭代器
b = range(0,8)
print(type(b))
f = ['a', 'b', 'c']
g = iter(f)
print(type(g))













