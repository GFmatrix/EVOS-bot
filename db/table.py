from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, DateTime
import datetime
meta = MetaData()
Base = declarative_base()
    
class UsersTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    telegram_id = Column(Integer, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)