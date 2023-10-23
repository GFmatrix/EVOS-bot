from db.table import CartTable, ProductsTable
from db.engine import engine
from sqlalchemy.orm import sessionmaker

def get_product_by_name(product_name):
    '''
    Return product object by name
    '''
    Session = sessionmaker(bind=engine)
    session = Session()
    
    res = session.query(ProductsTable).filter_by(name=product_name).first()
    
    return res if res else None

def get_product_by_id(product_id):
    '''
    Return product object by id
    '''
    Session = sessionmaker(bind=engine)
    session = Session()
    
    res = session.query(ProductsTable).filter_by(id=product_id).first()
    
    return res if res else None

def update_product_count(product_cart_id, count=0):
    Session = sessionmaker(bind=engine)
    session = Session()
    if count == 0:
        product = session.query(CartTable).filter_by(id=product_cart_id).first()
        count = product.count
        return count
    session.query(CartTable).filter_by(id=product_cart_id).update({'count':count})
    session.commit()
    return  