import sys
filepath='/home/sandesh/Desktop/new_leapfrog/Leapfrog-Assignment/Data/3rd Week(OLAP Design)/weekend_assignement'
sys.path.append(filepath)

from src.utils import connect

from src.helper import execute_insert_query
from src.helper import execute_select_query


def extract_data(query=None):
    split_loc = query.find("SELECT")
    select_query = query[split_loc:]
    print(select_query)
    data = execute_select_query(select_query,connect("ecomm_warehouse"))
    
    insert_query = str(query[:split_loc]) + "VALUES(%s"+",%s"*(len(data[0])-1) +")"
    
    #print(data[0])
    print(insert_query)
    execute_insert_query(insert_query,connect('ecomm_warehouse'),data)

if __name__=='__main__':
    fp=['../sql/insert_into_dim_uom.sql','../sql/insert_into_dim_brand.sql','../sql/insert_into_dim_category.sql',
       '../sql/insert_into_dim_status.sql']
    
    for f in fp:
        with open(f,'r') as q:
                q=q.read()
                q=q.replace("\n",' ')
                #print(q)
                extract_data(q)
    
    #After the above dimention table is populated now We populate the fact table.
    with open('../sql/insert_into_fact_product.sql','r') as q:
        q=q.read()
        q=q.replace("\n",'\n')
        #print(q)
        extract_data(q)