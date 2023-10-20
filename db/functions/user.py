from db.table import LanguagesEnum, UsersTable
from db.engine import engine
from sqlalchemy.orm import sessionmaker


def register(telegram_id, first_name, last_name):
    """
    Register a user in the database
    """
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = UsersTable(telegram_id=telegram_id,
                          first_name=first_name, last_name=last_name, 
                          language=LanguagesEnum(int(1)))
        session.add(user)
        session.commit()

    except Exception as e:
        print(e)
        
def lang(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    user = session.query(UsersTable).filter_by(telegram_id=user_id).first()
    
    return user.language.name