-- find employee salary more than avg salary
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) AS avg_salary FROM employees);

-- find department with highest total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC
LIMIT 1;

-- display employee with second highest salary
-- SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees
-- WHERE salary < (SELECT MAX(salary) FROM employee));

SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
);

-- display employees working in same department as amit 
SELECT *
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);

