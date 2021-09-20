import sys
filepath='/home/sandesh/Desktop/new_leapfrog/Leapfrog-Assignment/Data/3rd Week(OLAP Design)/weekend_assignement'
sys.path.append(filepath)

from src.utils import connect

from src.helper import execute_insert_query


def extract_data(filepath,query=None):
    data=[]
    with open(filepath,'r') as f:
        flag=0
        for line in f:
            row=[]
            if flag==0:
                flag=1
                continue
            row=line.strip().split(',')
            data.append(row)
            
    execute_insert_query(query,connect('ecomm_warehouse'),data)

if __name__=='__main__':
    data_filepath=['../../data/customer_dump - Sheet1.csv','../../data/product_dump - Sheet1.csv','../../data/sales_dump - Sheet1.csv']
    query_filepath=['../sql/insert_into_customer_dump.sql','../sql/insert_into_product_dump.sql','../sql/insert_into_sales_dump.sql']
    query=[]
    for fp in query_filepath:
         with open(fp,'r') as q:
             q=q.read()
             q=q.replace("\n",' ')
             query.append(q)
    #print(query)
    
    for i in range(3):
        extract_data(data_filepath[i],query[i])