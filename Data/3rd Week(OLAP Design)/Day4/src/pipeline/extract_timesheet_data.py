import sys
import datetime
file_path = '/home/sandesh/Desktop/Leapfrog/Data/3rd Week(OLAP Design)/Day3'
sys.path.append(file_path)

from src.utils import connect

from src.helper import execute_select_query
from src.helper import execute_insert_query

def extract_timesheet_data_from_timesheet_raw(filepath):
     query = """
     SELECT * FROM final_table
     """

     data=execute_select_query(query,connect("olap_day_2_assignement"))

     #print(data)

     # print(data[0])


     # print(data[1])

     # print(data[3])
     # print(data[100])

     #print(isinstance(data[100][2][1],datetime.time))
     data_cleaned = []
     for item in data:
          row=[]
          for i,ele in enumerate(item):
               if i==2:
                    #print(ele)
                    flag=0
                    for t in ele:
                         if isinstance(t,datetime.time):
                              row.append(t.strftime("%H:%M"+":00"))
                              flag+=1
                              break
                    if flag==1:
                         continue
                              
                      
                    
               if i==3:
                    flag=0
                    for t in reversed(ele):
                         if isinstance(t,datetime.time):
                              row.append(t.strftime("%H:%M"+":00"))
                              flag=1
                              break
                    if flag==1:
                         continue

               if i==4:
                    row.append(ele.strftime("%Y-%d-%M"))
                    continue 
               if i==5:
                    #print(str(ele))
                    row.append(str(ele))
                    continue
               if i==6 or 7 or 10 or 11 or 12:
                    row.append(str(ele))
                    continue

               row.append(ele[0])
          #print(row)
          data_cleaned.append(row)
     #print(data_cleaned)
     # for item in data_cleaned:
     #      print(len(item))
     print(len(data_cleaned))

     query_1 = """INSERT INTO timesheet(employee_id,department_id,shift_start_time,shift_end_time,
     shift_date,shift_type,hours_woked,attendence,has_taken_break,break_hour,was_charge,charge_hour,was_on_call,
     on_call_hour,num_teammates_absent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

     execute_insert_query(query_1 , connect("etl-day4"),data_cleaned)


    
    

          
    


    

            

if __name__ == '__main__':
    extract_timesheet_data_from_timesheet_raw('../../data/timesheet_2021_07_24 - Sheet1.csv')
