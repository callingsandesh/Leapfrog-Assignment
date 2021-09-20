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
    
    
    filepath='../../data/customer_dump - Sheet1.csv'
    with open('../sql/insert_into_dim_customer.sql','r') as q:
        q=q.read()
        q=q.replace("\n",' ')
    #print(q)
    extract_data(filepath,q)