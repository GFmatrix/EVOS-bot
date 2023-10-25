from db.table import CartTable, ProductsTable, UsersTable
from db.engine import engine
from db.functions.product import get_product_by_id
from sqlalchemy.orm import sessionmaker

def add_to_cart(product_id, count:int, telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user_id = session.query(UsersTable).filter_by(telegram_id=telegram_id).first().id
    product = session.query(CartTable).filter_by(product_id=product_id, user_id=user_id).first()
    if product:
        session.query(CartTable).filter_by(id=product.id).update({'count':int(count)+int(product.count)})
        session.commit()
        return    
    else:
        cart = CartTable(product_id=product_id, count=count, user_id=user_id)
        session.add(cart)
        session.commit()
        return

def get_product_price(product_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.query(ProductsTable).filter_by(id=product_id).first()
    return product.price

def remove_from_cart(_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.query(CartTable).filter_by(id=_id).delete()

def get_cart_via_tg_id(telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user_id = session.query(UsersTable).filter_by(telegram_id=telegram_id).first().id
    products = session.query(CartTable).filter_by(user_id=user_id).all()
    for product in products:
        pr = get_product_by_id(product.product_id)
        product.price = pr.price
        product.name = pr.name
    return products
