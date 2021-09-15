import json
import sys
abs_filepath = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day2/'
sys.path.append(abs_filepath)

#using absolute path 
from src.utils import connect



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


def extraxt_data_to_table_employee_from_json_or_xml(filepath):
    """ This is the method to extract data from .json or .xml to database" table employee"""

    #if the file is json
    if ".json" in filepath:
        with open(filepath,'r') as file:
            data=json.load(file)

    #if the file is xml
    if ".xml" in filepath:
        with open(filepath,'r') as f:
            data=f.read()
    

    #quety to remove prevous data if present
    query_1 = "DELETE FROM employee"
    execute_query(query_1)


    #query to insert the data
    query_2 = "INSERT INTO employee VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    data_all=[]
    for item in data:
        row=[]
        for value in item.values():
            row.append(value)
        
        data_all.append(row)
    execute_query(query_2,data_all)
    

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


    query_2 = "INSERT INTO timesheet VALUES(%s, %s, %s, %s, %s, %s, %s)"
    
    execute_query(query_2,data)

    


if __name__ == "__main__":
    extraxt_data_to_table_employee_from_json_or_xml("../../data/employee_2021_08_01.json")
    
    extraxt_data_to_table_employee_from_json_or_xml("../../data/employee_2021_08_01.json")

    csv_filepaths=["../../data/timesheet_2021_05_23 - Sheet1.csv","../../data/timesheet_2021_06_23 - Sheet1.csv","../../data/timesheet_2021_07_24 - Sheet1.csv"]
    for filepath in csv_filepaths:
        extraxt_data_to_table_timesheet_from_csv(filepath)

