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

my_user = Session.query(User).filter_by(id=1).first()
my_user.name = "Jack"

fake_user = User(name='Rain', password='12345')
Session.add(fake_user)
# 这时看session里有你刚添加和修改的数据
print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())
# 此时你rollback一下
Session.rollback()
# 再查就发现刚才添加的数据没有了。
print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())

# Session
# Session.commit()








