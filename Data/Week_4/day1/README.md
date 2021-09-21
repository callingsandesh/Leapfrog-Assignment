## DATA VALIDATION DAY 1 ASSIGNMENT

> ## The file structure of this repository:


```
data/                                   # Folder containing the datasets given as assignemt .
    *.csv
 docs/                                  # Folder containing .md files for documentation.      
    documentation.md
schema/                                 # Folder containing sql query.
    *.sql    
src/
    pipeline/                             # Folder containing python scripts    
      *.py
    helper.py
    utils.py
```

### Assignement Questions
> Create tables in database and populate the tables using the given datasets.
Please keep the name of the table and sheet name of dataset same (e.g. customer).
> Write test scripts for the following test cases
1. Check if a single employee is listed twice with multiple ids.
2. Check if part time employees are assigned other fte_status.
3. Check if termed employees are marked as active.
4. Check if the same product is listed more than once in a single bill.
5. Check if the customer_id in the sales table does not exist in the customer table.
6. Check if there are any records where updated_by is not empty but updated_date is empty.
7. Check if there are any hours worked that are greater than 24 hours.
8. Check if non on-call employees are set as on-call.
9. Check if the break is true for employees who have not taken a break at all.
10. Check if the night shift is not assigned to the employees working on the night shift.
