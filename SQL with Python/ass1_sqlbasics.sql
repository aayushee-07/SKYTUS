CREATE DATABASE sqlwithpython;

USE sqlwithpython;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

INSERT INTO students (student_id, name, department,year,marks) VALUES
(1, 'Aayushee', 'IT', 3, 85),
(2, 'Rahul', 'CSE', 3, 78),
(3, 'Priya', 'IT', 2, 92),
(4, 'Amit', 'CSE', 3, 67),
(5, 'Neha', 'ECE', 2, 88),
(6, 'Rohan', 'IT', 3, 74);

-- display all students records  
SELECT * FROM students;

-- dispaly only name and department of the students-- 
SELECT name, department FROM students;

--  Find students with marks greater than 75
SELECT * FROM students WHERE marks > 75 ;

-- Display students from CSE department
SELECT * FROM students WHERE department = 'CSE' ;

-- Sort students by marks and Display top 3 scorers
SELECT * FROM students
ORDER BY marks DESC 
LIMIT 3 ;
