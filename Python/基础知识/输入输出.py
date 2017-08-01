import getpass
# 输入
name = input('name:')
age = input('age:')
Salary = input('salary:')
# 方法1
info = '''
Name:{_name}
Age:{_age}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _salary=Salary)
# 方法2
info1 = '''
Name:{0}
Age:{1}
Salary:{2}'''.format(name, age, Salary)
print(info)
print(info1)

# 密文输入
password = getpass.getpass("input password:")
