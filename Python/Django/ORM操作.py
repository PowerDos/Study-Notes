# ORM操作
# 创建类
# 1.根据类自动创建数据库表
#
# 2.根据类对数据库表中的数据进行各种操作
#
#     a.先写类
#     from django.db import models
#
#
#     # app01_userinfo
#     class UserInfo(models.Model):
#         # id列，自增，主键
#         # 用户名列，字符串类型，指定长度
#         username = models.CharField(max_length=32)
#         password = models.CharField(max_length=64)
#
#
#     b.注册APP
#
#         INSTALLED_APPS = [
#             'django.contrib.admin',
#             'django.contrib.auth',
#             'django.contrib.contenttypes',
#             'django.contrib.sessions',
#             'django.contrib.messages',
#             'django.contrib.staticfiles',
#             'app01',
#         ]
#     c.执行命令
#         python manage.py makemigrations
#         python manage.py migrate
#




# #######################使用Mysql数据库####################### #
# 在setting文件夹中的DATABASES中写入
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'cloudcoin',
#         'USER': 'root',
#         'PASSWORD': 'abcdef123',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }
#
# 执行命令
#     python manage.py makemigrations
#     python manage.py migrate
#
# ** ** ** ** ** 注意 ** ** ** ** ** *
#     Django默认使用MySQLdb模块链接MySQL
#     主动修改为pymysql，在project同名文件夹下的__init__文件中添加如下代码即可：
#         import pymysql
#         pymysql.install_as_MySQLdb()
#
# ############################################################# #


# #########################Django增删改查######################## #

# 插入数据
# 推荐用第一种和第三种
# 方法一
# models.UserInfo.objects.create(
#     username='root',
#     password='123456',
#     status=1
# )
# 方法二
# obj = models.UserInfo(
#     username = 'Gavin',
#     password = '123456',
#     status = 1
# )
# obj.save()
# 方法三
# dic = {'username':'Gavin2','password':'123456','status':1}
# models.UserInfo.objects.create(**dic)
#
#
# 查询数据
# 1.查询所有数据
#   #拿到的数据<QuerySet [<UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>]>
#   #print(models.UserInfo.objects.all())
#
# result = models.UserInfo.objects.all()
# for row in result:
#     print(row.id,row.username,row.password,row.status)
#
# 2.过滤查询
#
# result = models.UserInfo.objects.filter(username='Gavin')
# for row in result:
#     print(row.id, row.username, row.password, row.status)
#
# 3.删除
# models.UserInfo.objects.filter(id=1).delete()
#
# 4.更新
#   更新全部
# models.UserInfo.objects.all().update(password='123')
#   更新一个
# models.UserInfo.objects.filter(id=3).update(password='1233asd')


























