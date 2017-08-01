import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# 创建引擎
# echo=True 表示打印详细信息，可以省略
engine = create_engine("mysql+pymysql://root:abcdef123@localhost/test",
                       encoding='utf-8')
# 生成orm基类
Base = declarative_base()

# 创建类
class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" % (self.id,self.name)

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)

# 生成session实例
Session = Session_class()

# 查询数据
# all() 取出所有数据
# print("===================取出所以数据===================")
# data = Session.query(User).filter_by(name="Gavin").all()
# print(data)
# print(data[0].name)
# print(data[0].password)
# print(data[0].id)

# first() 取出第一条数据
# print("===================取出第一条数据===================")
# data = Session.query(User).filter_by().first()
# print(data)
# print(data.name)
# print(data.password)
# print(data.id)

# first() filter可以用>号
print("\n===================条件查询===================")
data = Session.query(User).filter(User.id>1).all()
print(data)

# 多条件查询
print("\n===================多条件查询===================")
data = Session.query(User).filter(User.id>1).filter(User.id<3).first()
print(data)


# 更改数据
print("\n===================更改数据===================")
data.name = "Gavin change the name"
data.password = "12345666"

# 提交，可以同一修改、删除、添加数据
Session.commit()