**Logical modelling**

The list of possible entities are:

1. department (Dimension table)
1. employee (Dimension table)
1. punch\_apply\_date (Dimension table)
1. paycode (dimension table)
1. attendence (Fact table)

Now I will give the description of the entities , description of their attributes and the attributes domain.


|Entity|Description|Domain|
| :- | :- | :- |
|department|The list of departments present in the hospital.||
|<p>**Attributes**:</p><p>department\_id</p><p></p><p>department\_name</p>|<p></p><p>Identifier of the entity department,PK</p><p>The name of the department</p>|<p></p><p>Fixed length character</p><p>Text</p>|
|employee|The person working on the hospital||
|<p>**Attributes:**</p><p>employee\_id</p><p></p><p>name</p><p>department\_id</p><p></p><p>manager\_employee\_id</p><p></p><p>employee\_role</p><p>salary</p><p>hire\_date</p><p>terminated\_date</p><p>dob</p><p>fte</p><p>location</p>|<p></p><p>Identifier of the entity employee,PK</p><p>First\_name+last\_name</p><p>ID referencing the entity department,FK</p><p>ID referencing the employee\_id of the same table,FK</p><p>The role of an employee</p><p>The salary of the employee</p><p>The hire date of employee</p><p>The terminated date of employee</p><p>Data of birth</p><p>Full time equivalent</p><p>The address of an employee</p>|<p></p><p>Integer</p><p></p><p>Text</p><p>Valid id from table department</p><p>Valid employee\_id from same table</p><p>Text</p><p>Money</p><p>Date</p><p>Date</p><p>Date</p><p>Float</p><p>Text</p>|
|punch\_apply\_date|Everyday attendance sheet||
|<p>**Attributes:**</p><p>date</p><p>day\_of\_month</p><p>month</p><p>Year</p><p>week\_day</p>|<p></p><p>Valid date,PK</p><p>The day of the date</p><p>The month of the date</p><p>The year of the date</p><p>The week day,</p><p>monday=0...sunday=6</p>|<p></p><p>Date</p><p>CHAR(2)</p><p>CHAR(2)</p><p>CHAR(4)</p><p>CHAR</p>|
|paycode|The paycode of the customer||
|<p>**Attributes:**</p><p>Id</p><p>paycode\_name</p>|<p></p><p>Identifier of the entity paycode,PK</p><p>The name of the paycode</p>|<p></p><p>CHAR(1)</p><p>Text</p>|
|attendence|The daily attendence of the employee||
|<p>**Attributes:**</p><p>id</p><p></p><p>employee\_id</p><p></p><p>cost\_center</p><p>punch\_in\_time</p><p>punch\_out\_time</p><p>punch\_apply\_date</p><p>paycode\_id</p><p>hours\_worked</p>|<p></p><p>Identifier of the entity attendence,SK,FK</p><p>Id referencing the entity employee\_id,FK</p><p>The cost center code</p><p>The date and time of punch in.</p><p>The date and time of punch out.</p><p>The date of the punch apply.</p><p>ID referencing the paycode table.</p><p>The number of hours worked on a particular paycode.</p>|<p></p><p>Auto generated</p><p></p><p>Valid id from table employee</p><p>CHAR(5)</p><p>Time Stamp</p><p>Time Stamp</p><p>Date</p><p>CHAR</p><p>Float</p><p></p><p></p>|

*FIG:Table showing the entities,attributes,attributes description and attributes domain of the entities.*



As per the above listed entities and looking at their relationship , I go for snowflake schema for dimensionality modelling.

The ER diagram is drawn below.

![Image of ER Diagram]
(https://github.com/callingsandesh/Leapfrog-Assignment/blob/main/Data/3rd%20Week(OLAP%20Design)/Day1/doc/logical%20model%20hospital%20warehousing(SNOWFLAKE).png)
*FIG:Logical ER diagram of Hospital warehouse(SNOWFLAKE SCHEMA)*




**Physical modelling**


This is the part where I will physically implement the model into the database.For that purpose we are gonna use PostgreSQL relational database.It is an open source DBMS.

It uses the Standard Query Language(SQL) to create,update,alter ,delete the tables or any rows in the database.
Firstly , I made the dummy datas for each table with some tuples in it in the Excel sheet.
Then , I have used python and the driver of PostgreSQL which is Psycopg2 to push the 
Data of .xlsx file into the Postgre DBMS.I have used Jupyter Notebook to write all of the code .
The physical implementation code of the hospital warehouse  is presented below in my github repository link:



VISIT THE LINK PLEASE FOR PHYSICAL IMPLEMENTATION + REQUIREMENT IMPLEMENTATION:
LINK:
<https://github.com/callingsandesh/Leapfrog-Assignment/blob/main/Data/3rd%20Week(OLAP%20Design)/Day1/hospital%20datawarehouse.ipynb> 


**Requirements**:

A

i) 

The clients can know what time the employee started and left from the fact table  by querying the punch\_in\_time and punch\_out\_time from the Fact table.

The number of hours worked is also in the dimension table .So it can be easily fetched , and to get the total number of hours worked we can use the GROUP BY statement.

We can use the paycode\_id to know the paycode , and fetch the respective paycode,

ii)

So, the employee can be on paycode “CALL” if they have “CALL” on the column paycode.

B.	To solve this issue we can make a separate column in the Fact table which     has columns like morning\_shift,day\_shift,evening\_shift.  

C. Their is a attribute called week\_day which denotes the day of the week .So,

`     `We can extract the weekend .

D. So, to know this we have see the attendance table , and see the paycode\_type is           “CHARGE” 

E. So, to analyze the data on a biweekly basis , we can simple get data skipping 13 days from the punch\_apply\_date.

F.We have the attributes employee\_role in the employee table(dimention\_table) from which we can fetch the information.

G.We have the department\_id in the employee table , so we can GROUP BY department of employee table and SUM up the salary, to get the total salary distribution of the respective departments. 











**References:**

1. *Draw.io (<https://app.diagrams.net/> )*
1. PostgreSQL ( <https://www.postgresql.org/> )
1. Psycopg2 ( <https://www.psycopg.org/docs/> )
1. Python Programming language  (<https://www.python.org/> )
1. Jupyter Notebook  (<https://jupyter.org/> )
1. VS Code 
1. Leapfrog slides
