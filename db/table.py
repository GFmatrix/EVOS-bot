from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BigInteger, Column, Enum, ForeignKey, Integer, String, MetaData, DateTime
import datetime
import enum
meta = MetaData()
Base = declarative_base()
    
class LanguagesEnum(enum.Enum):
    uz = 1
    
class UsersTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    telegram_id = Column(Integer, unique=True)
    cart = Column(String, nullable=True)
    language = Column(Enum(LanguagesEnum))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

class CategoriesTable(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)
    
class ProductsTable(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(BigInteger)
    category_id = Column(Integer, ForeignKey('categories.id'))
    photo = Column(String, default="https://placehold.co/300x200?text=Mahsulot+Rasmi")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)