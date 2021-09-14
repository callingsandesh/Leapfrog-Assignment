#!/usr/bin/env python
# coding: utf-8

# ## DataWarehousing(Physical Implementation)

# In[5]:


import psycopg2



# In[2]:







# #### Defining connect() method so we can use it laster through out our code

# In[6]:


def connect():
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="hospital_warehouse")
    
    return connection


# ### Creating tables in the database hospital_warehouse

# In[175]:


import logging

## Data preprocession and population the data into warehouse

# In[176]:


import pandas as pd


# In[177]:


employee_2021_08_01 = pd.read_excel('data/employee_2021_08_01.xlsx')


# In[178]:


employee_2021_08_02 = pd.read_excel('data/employee_2021_08_02.xlsx')


# In[179]:


employee_2021_08_03 = pd.read_excel('data/employee_2021_08_03.xlsx')


# In[180]:


employee_2021_08_02 == employee_2021_08_03


# In[181]:


employee_2021_08_02.iloc[14]


# In[182]:


employee_2021_08_03.iloc[14]


# ## Checking into department 

# In[183]:


employee_2021_08_03['department_name'].count()


# In[184]:


employee_2021_08_03['department_name'].unique()


# In[185]:


employee_2021_08_03['department_id'].unique()


# In[186]:


len(employee_2021_08_03['department_id'].unique())


# In[187]:


len(employee_2021_08_03['department_name'].unique())


# In[188]:


df_department = employee_2021_08_03[['department_id','department_name']]


# In[189]:


department = {}
for row in df_department.itertuples(index=False):
    id=int(row.department_id)
    department[id] = row.department_name


# In[190]:


department


# In[191]:


df_department = pd.DataFrame(list(department.items()),columns=['id','department_name'])


# In[192]:


df_department


# #### pushing above dataframe into table "department"

# In[193]:


import logging
try:
    connection = connect()
    cursor = connection.cursor()
    
    for key,value in department.items():
        query = "INSERT INTO department VALUES(%s,%s)"
        cursor.execute(query,(key,value))
        connection.commit()
    print("Data sucessfully inserted into department")
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")


# ## Checking into employee table(dimention table)

# In[194]:


employee_2021_08_03.columns


# In[195]:


employee_table = employee_2021_08_03[['employee_id', 'first_name', 'last_name', 'department_id', 
                  'manager_employee_id', 'employee_role', 'salary',
                   'hire_date', 'terminated_date', 'terminated_reason', 'dob', 'fte',
                   'location']]


# In[196]:


employee_table.dtypes


# In[197]:


len(employee_table.columns)


# ### Inserting into employee table of database

# In[198]:


import logging
try:
    connection = connect()
    cursor = connection.cursor()
    
    for row in employee_table.itertuples(index=False):
        query = "INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            data = [int(row.employee_id) , row.first_name , row.last_name , int(row.department_id)
               ,int(row.manager_employee_id),row.employee_role,row.salary,row.hire_date,row.terminated_date,row.terminated_reason,row.dob
               ,row.fte,row.location]
        except:
            data = [int(row.employee_id) , row.first_name , row.last_name , int(row.department_id)
               ,row.manager_employee_id,row.employee_role,row.salary,row.hire_date,row.terminated_date,row.terminated_reason,row.dob
               ,row.fte,row.location]
        #print(data)
        if data[4]=='-':
            data[4]=None
        else:
            data[4]=int(data[4])
        if str(data[9])=='nan':
            data[9]=None
        
        print(data)
            
            
            
            
        cursor.execute(query,data)
        connection.commit()
    print("Data sucessfully inserted into employee")
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")


# ## Checking into timesheet_2021_05_23,timesheet_2021_06_23,timesheet_2021_07_24 file

# In[199]:


timesheet_2021_05_23 = pd.read_excel('data/timesheet_2021_05_23.xlsx')


# In[200]:


timesheet_2021_06_23 = pd.read_excel('data/timesheet_2021_06_23.xlsx')


# In[201]:


timesheet_2021_07_24 = pd.read_excel('data/timesheet_2021_07_24.xlsx')


# In[202]:


timesheet = pd.concat([timesheet_2021_05_23,timesheet_2021_06_23,timesheet_2021_07_24])


# In[203]:


timesheet.shape


# In[204]:


timesheet['paycode'].head(10)


# In[205]:


timesheet['paycode'].unique()


# In[206]:


len(timesheet_2021_05_23['paycode'].unique())


# In[207]:


pay_code = list()


# Total number of paycode types

# In[208]:


paycode = {
    'A':timesheet_2021_05_23['paycode'].unique()[0],
    'B':timesheet_2021_05_23['paycode'].unique()[1],
    'C':timesheet_2021_05_23['paycode'].unique()[2],
    'D':timesheet_2021_05_23['paycode'].unique()[3],
    'E':timesheet_2021_05_23['paycode'].unique()[4]
}


# In[209]:


paycode


# ### Inserting into table paycode of database

# In[210]:


import logging
try:
    connection = connect()
    cursor = connection.cursor()
    query="INSERT INTO paycode VALUES(%s,%s)"
    for key , value in paycode.items():
        cursor.execute(query,(key,value))
        connection.commit()
    print("Data sucessfully inserted into table paycode")
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")


# ## Checking into punch_apply_date from timesheet file

# In[211]:


from datetime import datetime


# In[212]:


timesheet['punch_apply_date']


# In[213]:


punch_apply_date = {}
for item in timesheet['punch_apply_date']:
    row=[]
    if item in punch_apply_date:
        pass
    else:
        #row.append(str(item)[:10])
        row.append(str(item)[8:10])
        row.append(str(item)[5:7])
        row.append(str(item)[:4])
        row.append(item.weekday())
        
        punch_apply_date[str(item)[:10]]=row
    
        
    
    


# In[214]:


punch_apply_date


# ### Inserting the date,day,month,year into the Database table "punch_apply_date"

# In[216]:


import logging
try:
    connection = connect()
    cursor = connection.cursor()
    
    query="INSERT INTO punch_apply_date VALUES(%s,%s,%s,%s,%s)"
    for key,value in punch_apply_date.items():
        cursor.execute(query,(key,value[0],value[1],value[2],value[3]))
        connection.commit()
    print("Data sucessfully inserted into table punch_apply_date")
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")


# ## Checking Into timesheets

# In[217]:


timesheet.head()


# In[218]:


str(timesheet.iloc[0][2]) == 'NaT'


# In[219]:


timesheet.columns


# In[220]:


paycode


# In[221]:


paycode_list=[]
for item in timesheet['paycode']:
    paycode_list.append(list(paycode.keys())[list(paycode.values()).index(item)])
            


# In[222]:


timesheet['paycode_id'] = paycode_list


# In[ ]:





# In[223]:


timesheet = timesheet[['employee_id', 'cost_center', 'punch_in_time', 'punch_out_time',
       'punch_apply_date', 'paycode_id','hours_worked']]


# In[224]:


timesheet.head()


# ### Inserting into database of table "attendence"

# In[225]:


import logging
try:
    connection = connect()
    cursor = connection.cursor()
    
    data = [list(x) for x in timesheet.itertuples(index=False)]
    query = "INSERT INTO attendence VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
      
    for i,item in enumerate(data,1):
        item[0] = int(item[0])
        item[1] = int(item[1])
        if str(item[2])=='NaT':
            item[2]=None
        if str(item[3])=='NaT':
            item[3]=None
        
        
            
            
            
        cursor.execute(query,(i,item[0],item[1],item[2],item[3],item[4],item[5],item[6]))
        connection.commit()
    print("Data sucessfully inserted into attendence")
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")


# # Requirements

# In[226]:


try:
    connection = connect()
    cursor = connection.cursor()
    
    query = '''
    SELECT * FROM 
    attendence
    LIMIT(20)
    
    '''
    
    cursor.execute(query)
    col = [desc[0] for desc in cursor.description]  

    df=pd.DataFrame(columns=col,data=cursor.fetchall())
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")
df


# # a.

# ### LOOKING FOR AN PARTICULAR EMPLOYEE , 1377208 , was working on a particular day or not

# In[227]:


try:
    connection = connect()
    cursor = connection.cursor()
    
    query = '''
    
    
    
    SELECT * FROM 
    attendence a
    INNER JOIN punch_apply_date p
        ON a.punch_apply_date = p.date
    INNER JOIN paycode
        ON a.paycode_id = paycode.id
    WHERE a.employee_id=1377208 AND a.punch_apply_date='2021-05-10' 
        AND paycode.paycode_name != 'BREAK'
    
    '''
    
    cursor.execute(query)
    col = [desc[0] for desc in cursor.description]  

    df=pd.DataFrame(columns=col,data=cursor.fetchall())
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")
df


# In[228]:


try:
    connection = connect()
    cursor = connection.cursor()
    
    query = '''
    
  
    
    SELECT sum(hours_worked) AS "Total Hours worked at date 2021-05-10 by employee 1377208" FROM 
    attendence a
    INNER JOIN punch_apply_date p
        ON a.punch_apply_date = p.date
    INNER JOIN paycode
        ON a.paycode_id = paycode.id
    WHERE a.employee_id=1377208 AND a.punch_apply_date='2021-05-10' 
        AND paycode.paycode_name != 'BREAK'
    
    '''
    
    cursor.execute(query)
    col = [desc[0] for desc in cursor.description]  

    df=pd.DataFrame(columns=col,data=cursor.fetchall())
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")
df


# ### charge on the day.

# In[229]:


try:
    connection = connect()
    cursor = connection.cursor()
    
    query = '''
    
  
    
    SELECT * FROM 
    attendence a
    INNER JOIN punch_apply_date p
        ON a.punch_apply_date = p.date
    INNER JOIN paycode
        ON a.paycode_id = paycode.id
    WHERE a.employee_id=1377208 AND a.punch_apply_date='2021-05-10' 
        AND paycode.paycode_name = 'CHARGE'
    
    '''
    
    cursor.execute(query)
    col = [desc[0] for desc in cursor.description]  

    df=pd.DataFrame(columns=col,data=cursor.fetchall())
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")
df


# ### on call?

# In[230]:


try:
    connection = connect()
    cursor = connection.cursor()
    
    query = '''
    
  
    
    SELECT * FROM 
    attendence a
    INNER JOIN punch_apply_date p
        ON a.punch_apply_date = p.date
    INNER JOIN paycode
        ON a.paycode_id = paycode.id
    WHERE a.employee_id=1377208 AND a.punch_apply_date='2021-05-10' 
        AND paycode.paycode_name = 'ONCALL'
    
    '''
    
    cursor.execute(query)
    col = [desc[0] for desc in cursor.description]  

    df=pd.DataFrame(columns=col,data=cursor.fetchall())
except(Exception,psycopg2.Error) as e:
    print(e)
    logging.debug("An exception was thrown!", exc_info=True)
    logging.info("An exception was thrown!", exc_info=True)
    logging.warning("An exception was thrown!", exc_info=True)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print('')
        print("PostgreSQL connection is closed")
df

