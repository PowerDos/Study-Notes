import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# 创建引擎
# echo=True 表示打印详细信息，可以省略
engine = create_engine("mysql+pymysql://root:abcdef123@localhost/test",
                       encoding='utf-8', echo=True)
# 生成orm基类
Base = declarative_base()

# 创建类
class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)

# 生成session实例
Session = Session_class()

# 生成你要创建的数据对象
user_obj = User(name="Gavin3", password="123465")

# 此时还没创建对象呢，不信你打印一下id发现还是None
print(user_obj.name, user_obj.id)

# 把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj)

# 此时也依然还没创建
print(user_obj.name, user_obj.id)

# 现此才统一提交，创建数据
Session.commit()












