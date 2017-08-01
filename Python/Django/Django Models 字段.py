# Django Models
# #########################字段介绍#########################
# AutoField(Field)
#         - int自增列，必须填入参数 primary_key=True
#
#     BigAutoField(AutoField)
#         - bigint自增列，必须填入参数 primary_key=True
#
#         注：当model中如果没有自增列，则自动会创建一个列名为id的列
#         from django.db import models
#
#         class UserInfo(models.Model):
#             # 自动创建一个列名为id的且为自增的整数列
#             username = models.CharField(max_length=32)
#
#         class Group(models.Model):
#             # 自定义自增列
#             nid = models.AutoField(primary_key=True)
#             name = models.CharField(max_length=32)
#
#     SmallIntegerField(IntegerField):
#         - 小整数 -32768 ～ 32767
#
#     PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
#         - 正小整数 0 ～ 32767
#     IntegerField(Field)
#         - 整数列(有符号的) -2147483648 ～ 2147483647
#
#     PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
#         - 正整数 0 ～ 2147483647
#
#     BigIntegerField(IntegerField):
#         - 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807
#
#     自定义无符号整数字段
#
#         class UnsignedIntegerField(models.IntegerField):
#             def db_type(self, connection):
#                 return 'integer UNSIGNED'
#
#         PS: 返回值为字段在数据库中的属性，Django字段默认的值为：
#             'AutoField': 'integer AUTO_INCREMENT',
#             'BigAutoField': 'bigint AUTO_INCREMENT',
#             'BinaryField': 'longblob',
#             'BooleanField': 'bool',
#             'CharField': 'varchar(%(max_length)s)',
#             'CommaSeparatedIntegerField': 'varchar(%(max_length)s)',
#             'DateField': 'date',
#             'DateTimeField': 'datetime',
#             'DecimalField': 'numeric(%(max_digits)s, %(decimal_places)s)',
#             'DurationField': 'bigint',
#             'FileField': 'varchar(%(max_length)s)',
#             'FilePathField': 'varchar(%(max_length)s)',
#             'FloatField': 'double precision',
#             'IntegerField': 'integer',
#             'BigIntegerField': 'bigint',
#             'IPAddressField': 'char(15)',
#             'GenericIPAddressField': 'char(39)',
#             'NullBooleanField': 'bool',
#             'OneToOneField': 'integer',
#             'PositiveIntegerField': 'integer UNSIGNED',
#             'PositiveSmallIntegerField': 'smallint UNSIGNED',
#             'SlugField': 'varchar(%(max_length)s)',
#             'SmallIntegerField': 'smallint',
#             'TextField': 'longtext',
#             'TimeField': 'time',
#             'UUIDField': 'char(32)',
#
#     BooleanField(Field)
#         - 布尔值类型
#
#     NullBooleanField(Field):
#         - 可以为空的布尔值
#
#     CharField(Field)
#         - 字符类型
#         - 必须提供max_length参数， max_length表示字符长度
#
#     TextField(Field)
#         - 文本类型
#
#     EmailField(CharField)：
#         - 字符串类型，Django Admin以及ModelForm中提供验证机制
#
#     这个基本不会用了，下面那个GenericIPAddressField
#     IPAddressField(Field)
#         - 字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制
#
#     GenericIPAddressField(Field)
#         - 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
#         - 参数：
#             protocol，用于指定Ipv4或Ipv6， 'both',"ipv4","ipv6"
#             unpack_ipv4， 如果指定为True，则输入::ffff:192.0.2.1时候，可解析为192.0.2.1，开启刺功能，需要protocol="both"
#
#     URLField(CharField)
#         - 字符串类型，Django Admin以及ModelForm中提供验证 URL
#
#     SlugField(CharField)
#         - 字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）
#
#     CommaSeparatedIntegerField(CharField)
#         - 字符串类型，格式必须为逗号分割的数字
#
#     UUIDField(Field)
#         - 字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证
#
#     FilePathField(Field)
#         - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
#         - 参数：
#                 path,                      文件夹路径
#                 match=None,                正则匹配
#                 recursive=False,           递归下面的文件夹
#                 allow_files=True,          允许文件
#                 allow_folders=False,       允许文件夹
#
#     FileField(Field)
#         - 字符串，路径保存在数据库，文件上传到指定目录
#         - 参数：
#             upload_to = ""      上传文件的保存路径
#             storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
#
#     ImageField(FileField)
#         - 字符串，路径保存在数据库，文件上传到指定目录
#         - 参数：
#             upload_to = ""      上传文件的保存路径
#             storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
#             width_field=None,   上传图片的高度保存的数据库字段名（字符串）
#             height_field=None   上传图片的宽度保存的数据库字段名（字符串）
#
#     DateTimeField(DateField)
#         - 日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
#
#     DateField(DateTimeCheckMixin, Field)
#         - 日期格式      YYYY-MM-DD
#
#     TimeField(DateTimeCheckMixin, Field)
#         - 时间格式      HH:MM[:ss[.uuuuuu]]
#
#     DurationField(Field)
#         - 长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型
#
#     FloatField(Field)
#         - 浮点型
#
#     DecimalField(Field)
#         - 10进制小数
#         - 参数：
#             max_digits，小数总长度
#             decimal_places，小数位长度
#
#     BinaryField(Field)
#         - 二进制类型
#
# ############################################################ #