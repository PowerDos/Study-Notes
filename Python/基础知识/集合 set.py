list1 = set(['1', '2', '3', '4', '5'])
list2 = set(['3', '4', '5', '6', '7'])
# 交集
print(list1.intersection(list2))
# 并集
print(list1.union(list2))
# 差集
print(list1.difference(list2))
# 判断是否是子集 返回boolean
print(list1.issubset(list2))
# 对称差集 去掉并集
print(list1.symmetric_difference(list2))
# 判断是否存在
print('1' in list1)
print('2' not in list1)

