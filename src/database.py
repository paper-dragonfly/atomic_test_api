from sqlalchemy import Column, Integer, String, Sequence 
from sqlalchemy.orm import declarative_base 

# Create instance of Base class which does decarative mapping
Base = declarative_base() 

# Create table schema
class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, Sequence("user_user_id_seq"), primary_key=True)
    username = Column(String(50))
    team = Column(String(50))

    def __repr__(self): # returns info in nice formatting
        return "<User(user_id='%s',name='%s', team='%s')>" % (
            self.username,
            self.team,
        )

