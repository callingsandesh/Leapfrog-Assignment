import sys
import os
filepath='/home/sandesh/Desktop/new_leapfrog/Leapfrog-Assignment/Data/Week_4/day1'
sys.path.append(filepath)

from src.utils import connect

from src.helper import execute_insert_query


def extract_data(filepath,query):
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
    print("\n")
    execute_insert_query(query,connect('week_4_data-validation'),data)

if __name__=='__main__':
    data_filepath=os.listdir('../../data')

    query = ['INSERT INTO timesheet_raw VALUES(%s,%s,%s,%s,%s,%s,%s)',
            'INSERT INTO sales VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            'INSERT INTO employee_raw VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,
            'INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s)' ,
            'INSERT INTO timesheet VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,
            'INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,
            'INSERT INTO product VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'   
            ]
    for i in range(len(query)):
        extract_data("../../data/"+data_filepath[i],query[i])
