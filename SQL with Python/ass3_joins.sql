CREATE DATABASE company_db;

USE company_db;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
);

INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing');

INSERT INTO employees (emp_id, emp_name, dept_id, salary) VALUES
(101, 'Aayushee', 1, 60000),
(102, 'Rahul', 1, 55000),
(103, 'Priya', 1, 70000),
(104, 'Amit', 2, 45000),
(105, 'Neha', 2, 52000),
(106, 'Rohan', 3, 65000),
(107, 'Karan', NULL, 40000);

-- display employee name with department name
SELECT e.emp_name, d.dept_name FROM employees e 
INNER JOIN departments d 
ON e.dept_id = d.dept_id;

-- display employee erning more than 50,000
SELECT * FROM employees WHERE salary > 50000;

-- display department-wise total salaray
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- display deparment more than 2 employees
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;

-- display employee without department
SELECT e.emp_id, e.emp_name, e.salary
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
