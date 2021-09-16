import sys
file_path = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day3'
sys.path.append(file_path)

from src.helper import execute_select_query
from src.utils import connect

def extract_data_from_ecommerce():
    """This is a method to extract data from ecommerce database"""

    query = """
    SELECT s.user_id , u.username,p.id,c.id,c.name,
    p.price,s.price,s.quantity,(p.quantity-s.quantity),
    s.updated_at  
    FROM sales s
    INNER JOIN users u
        ON s.user_id = u.id
    INNER JOIN products p
        ON s.product_id = p.id
    INNER JOIN categories c 
        ON  p.category_id = c.id
    """
    data=execute_select_query(query,connect("ecommerce_dumb"))
    return data

