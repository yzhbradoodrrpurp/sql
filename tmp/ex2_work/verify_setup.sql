/* Verification-only setup for Basic SQL Exercise 2. */

/* Permit the two assignment-requested values in the disposable test DB. */
ALTER TABLE instructor DROP CONSTRAINT instructor_salary_check;
ALTER TABLE course DROP CONSTRAINT course_credits_check;

CREATE TABLE employee (
    employee_name varchar(50) PRIMARY KEY,
    street varchar(100),
    city varchar(50)
);

CREATE TABLE works (
    employee_name varchar(50),
    company_name varchar(100),
    salary numeric(10,2)
);

CREATE TABLE company (
    company_name varchar(100),
    city varchar(50),
    PRIMARY KEY (company_name, city)
);

CREATE TABLE manages (
    employee_name varchar(50),
    manager_name varchar(50)
);

INSERT INTO employee VALUES
    ('Alice', '1 Main St', 'Shanghai'),
    ('Bob', '2 Park Rd', 'Beijing'),
    ('Carol', '3 Lake Ave', 'Shanghai'),
    ('Dave', '4 Hill Rd', 'Shenzhen');

INSERT INTO works VALUES
    ('Alice', 'First Bank Corporation', 12000),
    ('Bob', 'Small Bank Corporation', 9000),
    ('Carol', 'Tech Corporation', 15000);

INSERT INTO company VALUES
    ('First Bank Corporation', 'Shanghai'),
    ('Small Bank Corporation', 'Beijing'),
    ('Small Bank Corporation', 'Shanghai'),
    ('Tech Corporation', 'Beijing'),
    ('Tech Corporation', 'Shanghai');
