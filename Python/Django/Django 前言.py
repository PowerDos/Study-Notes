# Django 安装
# pip3 install django

# 在D:\Python\Python36\Scripts下有django-admin.exe

# 生成网站
# D:\Python\Python36\Scripts>

# 进入目录
# cd FirstSite

# 启动网站
# python manage.py runserver

# D:\Python\www\FirstSite>python manage.py runserver
# Performing system checks...
#
# System check identified no issues (0 silenced).
#
# You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.
# April 20, 2017 - 13:07:41
# Django version 1.11, using settings 'FirstSite.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
# [20/Apr/2017 13:08:00] "GET / HTTP/1.1" 200 1716
# Not Found: /favicon.ico

# 创建完
# FirstSite
#     -FirstSite
#         -init
#         -settings # 配置文件
#         -url  # URL对应关系
#         -wsgi # 遵循WSIG规范。uwsgi + nginx
#     -manage.py # 管理Django程序
                 #  - python manage.py
                 #  - python manage.py startapp xxx
                 #  - python manage.py makemigrations
                 #  - python manage.py migrate


# 创建APP
# python manage.py startapp cmdd
# python manage.py startapp admin
# APP目录
    # migrations  # 数据修改表结构
    #   -__init__.py
    # __init__.py
    # admin.py # Django为我们提供的后台管理
    # apps.py # 配置当前APP
    # models.py # ORM,写指定的类 通过命令就可以创建数据库结构
    # tests.py # 单元测试
    # views.py # 写业务代码


# 配置模板目录
# 'DIRS': [os.path.join(BASE_DIR, 'templates')],
# 配置静态目录
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )










