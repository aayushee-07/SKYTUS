-- count total number of students
SELECT COUNT(*) AS total_students FROM students;

-- find avg marks of students
SELECT AVG(marks) AS avg_marks FROM students;

-- find highest and lowest marks of students
SELECT MAX(marks) AS highest_marks, MIN(marks) AS lowest_marks FROM students;

-- find department wise avg marks
SELECT  department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

-- display department where avg marks > 70 
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;