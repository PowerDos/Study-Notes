# json
# 只能序列化反序列化列表字典之类的
# 因为考虑到不同编程语言传输处理问题
import json
info = {
    'name':'Gavin',
    'age':22
}
# 序列化
a = json.dumps(info)
print(a, type(a))
# 反序列化
b = json.loads(a)
print(b, type(b))


# pickle
# 可以序列化python所以类型
# 但反序列化，如果是函数，需要反序列化函数中，有序列化函数中的那个函数，类似java
import pickle
def pic():
    print("asdas")

a = pickle.dumps(pic)
print(a)
b = pickle.loads(a)
b()
























