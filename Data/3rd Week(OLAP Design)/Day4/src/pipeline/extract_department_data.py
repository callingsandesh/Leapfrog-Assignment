import sys

file_path = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day3'
sys.path.append(file_path)


from src.utils import connect

from src.helper import execute_insert_query

def extract_department(filepath):
    with open(filepath,'r') as f:
        
        with open(filepath,'r') as f:
            data=[]
            i=0
            for line in f:
                if i == 0:
                    i+=1
                    continue

                row=line.strip().split(",")
                data.append(row)
    
    department={}
    for item in data:
        if item[3] in department:
            continue
        else:
            department[item[3]] = item[4] 
    data = [(key,value) for key,value in department.items()]
    #print(data)

    with open('../sql/insert_into_department.sql','r') as sqlFile:
        query =sqlFile.read()
    
    #print(query)
    
    execute_insert_query(query,connect("etl-day4"),data)

if __name__ =='__main__':
    extract_department('../../data/employee_2021_08_01.csv')

