-- Creating employee table
CREATE TABLE employee (
    employee_id VARCHAR(7) PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    department_id CHAR(5),
    department_name VARCHAR(100),
    manager_employee_id VARCHAR(7),
    employee_role VARCHAR(100),
    salary NUMERIC(7,2),
    hire_date DATE,
    terminated_date CHAR(10),
    terminated_reason TEXT,
    dob DATE,
    fte VARCHAR(3),
    locations varchar(50)
);