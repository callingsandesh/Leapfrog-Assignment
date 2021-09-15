import json
import sys
abs_filepath = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day2/'
sys.path.append(abs_filepath)

#using absolute path 
from src.utils import connect

from lxml import etree


def execute_query(query,data=None): 
    """This is the method to execute the SQL query given the query and data is optional"""
    try:
        conn = connect()
        cur = conn.cursor()
        if data:
            for item in data:
                for i,value in enumerate(item):
                    if value=='':
                        item[i]=None
                cur.execute(query,item)
        else:
            cur.execute(query)
        conn.commit()
        print(query+", successfully executed")
    except(Exception) as e:
        print(e)
    finally:
        if (conn):
            cur.close()
            conn.close()


def extraxt_data_to_table_employee_from_json(filepath):
    """ This is the method to extract data from .json or .xml to database" table employee"""

    with open(filepath,'r') as file:
        data=json.load(file)
    
    #opening the delete_from_employee_table sql query
    with open("../sql/delete_from_employee_table.sql") as sqlFile:
        query=sqlFile.readlines()
    
    query=query[0].replace('\n','')
    execute_query(query)


    #opening the extract_employee_data sql query
    with open("../sql/extract_employee_data.sql") as sqlFile:
        query=sqlFile.readlines()
    query_2 = query[0].replace('\n','')
    
    data_all=[]
    for item in data:
        row=[]
        for value in item.values():
            row.append(value)
        
        data_all.append(row)
    execute_query(query_2,data_all)


def extract_data_to_table_employee_from_xml(filepath):
    parser = etree.parse(filepath)
    columns = ('employee_id','first_name','last_name','department_id','department_name','manager_employee_id','employee_role','salary','hire_date','terminated_date','terminated_reason','dob','fte','location')
    data=[]
    for i in parser.findall('Employee'):
        values = [i.find(n).text for n in columns]
        data.append(values)
  
    #opening the delete_from_employee_table sql query
    with open("../sql/delete_from_employee_table.sql") as sqlFile:
        query=sqlFile.readlines()
    
    query=query[0].replace('\n','')
    execute_query(query)

    with open("../sql/extract_employee_data.sql") as sqlFile:
        query=sqlFile.readlines()
    
    query_2 = query[0].replace('\n','')
    execute_query(query_2,data)
    


def extraxt_data_to_table_timesheet_from_csv(filepath):
    data=[]
    with open(filepath,'r') as f:
        i=0
        for line in f:
            if i == 0:
                i+=1
                continue

            row=line.strip().split(",")
            data.append(row)

    # query_1 = "DELETE FROM timesheet"
    # execute_query(query_1)

    with open("../sql/extract_timesheet_data.sql") as sqlFile:
        query=sqlFile.readlines()
    query_2 = query[0].replace('\n','')
    
    execute_query(query_2,data)

    


if __name__ == "__main__":
    extraxt_data_to_table_employee_from_json("../../data/employee_2021_08_01.json")
    
    extract_data_to_table_employee_from_xml("../../data/employee_2021_08_01.xml")

    csv_filepaths=["../../data/timesheet_2021_05_23 - Sheet1.csv","../../data/timesheet_2021_06_23 - Sheet1.csv","../../data/timesheet_2021_07_24 - Sheet1.csv"]
    for filepath in csv_filepaths:
        extraxt_data_to_table_timesheet_from_csv(filepath)

