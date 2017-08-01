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

# 统计
print("====================统计数目====================")
num = Session.query(User).filter(User.name.like("G%")).count()
print(num)

# 分组
print("====================分组查询====================")
from sqlalchemy import func
print(Session.query(func.count(User.name),User.name).group_by(User.name).all() )
