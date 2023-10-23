from db.table import ProductsTable, CategoriesTable
from db.engine import engine
from sqlalchemy.orm import sessionmaker

def flatten_tuples_list(tuple_list):
    return [item[0] for item in tuple_list]

def get_categories():
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(CategoriesTable.name).all()
    
    return flatten_tuples_list(res) if res else None


def get_products_from_cat_name(category_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    cat_id = session.query(CategoriesTable).filter_by(name=category_name).first().id
    
    res = session.query(ProductsTable.name).filter_by(category_id=cat_id).all()
    return flatten_tuples_list(res) if res else None