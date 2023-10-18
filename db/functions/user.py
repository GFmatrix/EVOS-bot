from db.table import UsersTable, UsersWordsTable, LanguagsEnum
from db.engine import engine
from sqlalchemy.orm import sessionmaker


def register(telegram_id, first_name, last_name, learn_lang=1, translate_lang=2):
    """
    Register a user in the database
    """
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = UsersTable(telegram_id=telegram_id,
                          first_name=first_name, last_name=last_name,)
        session.add(user)
        session.commit()

    except Exception as e:
        print(e)