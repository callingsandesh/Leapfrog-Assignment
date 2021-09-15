Day 2 Assignment

To create a table employee , I have used the following SQL query.

-- Creating employee table

CREATE TABLE employee (

`   `employee\_id VARCHAR(7) PRIMARY KEY,

`   `first\_name VARCHAR(30),

`   `last\_name VARCHAR(30),

`   `department\_id CHAR(5),

`   `department\_name VARCHAR(100),

`   `manager\_employee\_id VARCHAR(7),

`   `employee\_role VARCHAR(100),

`   `salary NUMERIC(7,2),

`   `hire\_date DATE,

`   `terminated\_date CHAR(10),

`   `terminated\_reason TEXT,

`   `dob DATE,

`   `fte VARCHAR(3),

`   `locations varchar(50)

);

The description of different data types use to create the attributes of entity employee are described below:

- employee\_id: VARCHAR(7) is used as it has 7 characters in the id , and sometimes it also has 6 characters or it can vary but cannot exceed 7 characters.
- first\_name: VARCHAR(30) is used as a name as different people have different lengths of characters in name, which is a varying character.
- last\_name:VARCHAR(30) is used as a last\_name as different people have different lengths of characters in name, which is a varying character.
- department\_id:CHAR(5) is used as the department\_id can have only  5 characters .
- department\_name:VARCHAR(100) is used as the name of the department can have varying length of characters, but it cannot exceed 100 characters.
- manager\_employee\_id:VARCHAR(7) is used as it has 7 characters in the id , and sometimes it also has 6 characters or it can vary but cannot exceed 7 characters.
- employee\_role:VARCHAR(100) is used as the name of the role can have varying length of characters , but it cannot exceed 100 characters.
- salary:NUMERIC(7,2) is used as the salary can have only 2 scales from the decimal point and the salary is not bigger than 5 figures.
- hire\_date:DATE is used as it is the date of the hire.
- terminated\_date:CHAR(10) is used as the date is not in the correct format of postgres and the date is only 10 characters long. Example: ‘01-01-1700’
- dob:DATE is used as date of birth is the date.
- fte:VARCHAR(3) is used as it has varying length and it has a maximum of 3 characters.
- location:VARCHAR(50) is used as it can have the varying length of characters in the name of location and the total characters cannot exceed 50.


To create a table timesheet , I have used the following SQL query.

--Creating timesheet table

CREATE TABLE timesheet(

`   `employee\_id VARCHAR(7),

`   `cost\_center CHAR(5),

`   `punch\_in\_time TIMESTAMP,

`   `punch\_out\_time TIMESTAMP,

`   `punch\_apply\_time DATE,

`   `hours\_worked NUMERIC(3,1),

`   `paycode VARCHAR(7)

);

The description of different data types use to create the attributes of entity timesheet are described below:

- employee\_id:VARCHAR(7) is used as it has 7 characters in the id , and sometimes it also has 6 characters or it can vary but cannot exceed 7 characters.
- cost\_center: CHAR(5) is used as it has only 5 characters.
- punch\_in\_time:TIMESTAMP is used as it has both date and time.
- punch\_out\_time:TIMESTAMP is used as it has both date and time.
- punch\_apply\_time:DATE is used as it is the punch date.
- hours\_worked:NUMERIC(3,1) is used as it can have only one precision after decimal point and two precision after decimal as a person cannot work more than 2 digits hours.
- paycode:VARCHAR(7) is used as the code is of varying characters but does not exceed 7 characters.


