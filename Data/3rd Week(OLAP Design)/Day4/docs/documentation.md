Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@callingsandesh 
callingsandesh
/
olap-design
Public
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
olap-design
/
Day4
/
docs
/
documentation.md
in
day_4
 

Tabs

8

Soft wrap
1
## Description of the schema present inside the `schema\*.sql`
2
​
3
* `schema\1_main_table.sql`
4
​
5
```
6
CREATE OR REPLACE VIEW main_table AS
7
SELECT
8
        t.employee_id,
9
        
10
        d.id as department_id,
11
        t.punch_in_time::timestamp::time AS shift_start_time,
12
        t.punch_out_time ::timestamp :: time AS shift_end_time,
13
        t.punch_apply_time as shift_date,
14
        t.hours_worked as hours_worked,
15
        CASE WHEN t.punch_in_time::timestamp::time BETWEEN '5:00' AND '9:00' THEN 'MORNING'
16
             WHEN t.punch_in_time::timestamp::time BETWEEN '9:00' AND '17:00' THEN 'DAY'
17
             WHEN t.punch_in_time::timestamp::time BETWEEN '5:00' AND  '23:59' THEN 'NIGHT'
18
             ELSE NULL
19
             END as shift_type,
20
        CASE WHEN t.paycode <> 'ABSENT' THEN 1
21
             ELSE 0
22
             END AS attendence ,
23
        
24
        CASE WHEN t.paycode = 'BREAK' THEN 1
25
             ELSE 0
26
             END as has_taken_break,
27
​
28
        CASE WHEN t.paycode = 'BREAK' THEN t.hours_worked
29
             ELSE 0
30
             END as break_hour,
31
        
32
        CASE WHEN t.paycode = 'CHARGE' THEN 1
33
             ELSE 0
34
             END as was_charge,
35
        
36
        CASE WHEN t.paycode = 'CHARGE' THEN t.hours_worked
37
             ELSE 0
38
             END  AS charge_hour,
39
        
40
        CASE WHEN t.paycode = 'ON_CALL' THEN 1
41
             ELSE 0
42
             END as was_on_call,
43
        CASE WHEN t.paycode = 'ON_CALL' THEN t.hours_worked
44
             ELSE 0
45
             END as on_call_hour
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
@callingsandesh
Commit changes
Commit summary
Create documentation.md
Optional extended description
Add an optional extended description…
 Commit directly to the day_4 branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About

