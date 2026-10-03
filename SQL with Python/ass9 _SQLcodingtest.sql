-- query to find Nth highest salary

SELECT DISTINCT salary 
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1; 

-- Remove duplicate records 
CREATE TABLE duplicate_users (
    id INT PRIMARY KEY,
    email VARCHAR(100)
);

INSERT INTO duplicate_users VALUES
(1, 'a@gmail.com'),
(2, 'b@gmail.com'),
(3, 'a@gmail.com'),
(4, 'c@gmail.com'),
(5, 'b@gmail.com');

SET SQL_SAFE_UPDATES = 0;

DELETE t1
FROM duplicate_users t1
JOIN duplicate_users t2
ON t1.email = t2.email
AND t1.id > t2.id;

SET SQL_SAFE_UPDATES = 1;

SELECT * FROM duplicate_users; 

-- Find records common in two tables
SELECT
    e.emp_id,
    e.emp_name,
    d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

-- Find employees hired in the last 6 months
ALTER TABLE employees
ADD hire_date DATE;

UPDATE employees
SET hire_date = '2026-08-10'
WHERE emp_id = 101;

UPDATE employees
SET hire_date = '2026-07-15'
WHERE emp_id = 102;

UPDATE employees
SET hire_date = '2026-05-20'
WHERE emp_id = 103;

UPDATE employees
SET hire_date = '2026-04-10'
WHERE emp_id = 104;

UPDATE employees
SET hire_date = '2026-09-01'
WHERE emp_id = 105;

UPDATE employees
SET hire_date = '2026-02-15'
WHERE emp_id = 106;

UPDATE employees
SET hire_date = '2026-08-25'
WHERE emp_id = 107;

SELECT *
FROM employees
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);

--  Find continuous duplicate values
CREATE TABLE continuous_values (
    id INT PRIMARY KEY,
    value INT
);
INSERT INTO continuous_values VALUES
(1, 10),
(2, 10),
(3, 20),
(4, 30),
(5, 30),
(6, 30),
(7, 40),
(8, 50),
(9, 50);

SELECT id, value
FROM (
    SELECT
        id,
        value,
        LAG(value) OVER (ORDER BY id) AS previous_value
    FROM continuous_values
) AS temp
WHERE value = previous_value;