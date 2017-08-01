# SQLAlchemy
# 安装SQLAlchemy
# pip3 install SQLAlchemy
# ORM
# orm英文全称object relational mapping,就是对象映射关系程序，
# 简单来说我们类似python这种面向对象的程序来说一切皆对象，
# 但是我们使用的数据库却都是关系型的，为了保证一致的使用习惯，
# 通过orm将编程语言的对象模型和数据库的关系模型建立映射关系，
# 这样我们在使用编程语言对数据库进行操作的时候可以
# 直接使用编程语言的对象模型进行操作就可以了，而不用直接使用sql语言。

# orm的优点：
# 隐藏了数据访问细节，“封闭”的通用数据库交互，ORM的核心。
# 他使得我们的通用数据库交互变得简单易行，并且完全不用考虑该死的SQL语句。
# ORM使我们构造固化数据结构变得简单易行。

# 缺点：
# 无可避免的，自动化意味着映射和关联管理，代价是牺牲性能（早期，这是所有不喜欢ORM人的共同点）。
# 现在的各种ORM框架都在尝试使用各种方法来减轻这块（LazyLoad，Cache），效果还是很显著的。

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# 创建表


# echo=True 表示打印详细信息，可以省略
engine = create_engine("mysql+pymysql://root:abcdef123@localhost/test",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'User'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


Base.metadata.create_all(engine)  # 创建表结构






























