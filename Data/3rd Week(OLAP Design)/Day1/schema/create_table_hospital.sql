--creating database
CREATE DATABASE hospital_warehouse;

--creating table department
CREATE TABLE department(
        department_id CHAR(5) PRIMARY KEY,
        department_name TEXT
        
    );

--creating table employee
CREATE TABLE employee(
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        department_id CHAR(5),
        manager_employee_id INTEGER,
        employee_role TEXT,
        salary MONEY NOT NULL,
        hire_date DATE NOT NULL,
        terminated_date DATE NOT NULL,
        terminated_reason TEXT,
        dob DATE NOT NULL,
        fte FLOAT,
        LOCATION TEXT,
        
        CONSTRAINT fk_employee_department_department_id
        FOREIGN KEY(department_id) REFERENCES department(department_id)
        
    );

--creating table punch_apply_date
CREATE TABLE punch_apply_date(
        date DATE PRIMARY KEY,
        day_of_month VARCHAR(2),
        month VARCHAR(2),
        year CHAR(4),
        week_day CHAR
        
        
    );

--creating table paycode
CREATE TABLE paycode(
        id CHAR PRIMARY KEY,
        paycode_name TEXT
    );

CREATE TABLE attendence(
        id SERIAL PRIMARY KEY,
        employee_id INTEGER,
        cost_center CHAR(5),
        punch_in_time TIMESTAMP,
        punch_out_time TIMESTAMP,
        punch_apply_date DATE,
        paycode_id CHAR,
        hours_worked FLOAT,
        
        CONSTRAINT fk_attendence_employee_employee_id
        FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
        
        CONSTRAINT fk_attendence_punch_apply_date_date
        FOREIGN KEY(punch_apply_date) REFERENCES punch_apply_date(date),
        
        CONSTRAINT fk_attendence_paycode_id
        FOREIGN KEY(paycode_id) REFERENCES paycode(id)
        
        
    );
