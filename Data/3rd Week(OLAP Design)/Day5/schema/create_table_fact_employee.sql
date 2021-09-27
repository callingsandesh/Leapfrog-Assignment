CREATE TABLE fact_employee(
    employee_id SERIAL PRIMARY KEY,
    client_employee_id VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department_id VARCHAR(255),
    manager_id VARCHAR(255),
    salary FLOAT,
    hire_date DATE,
    term_date VARCHAR(255),
    term_reason VARCHAR(255),
    dob DATE,
    role_id INTEGER,
    active_status_id INTEGER,
    weekly_hours FLOAT
);

