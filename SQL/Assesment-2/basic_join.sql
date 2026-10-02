
USE sqlassesment;

CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT
);

CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    teacher_id INT
);

INSERT INTO teachers (name, department_id)
VALUES
('Rahul', 1),
('Priya', 2),
('Amit', 1);

INSERT INTO courses (title, teacher_id)
VALUES
('Python Basics', 1),
('SQL Fundamentals', 2),
('Web Development', 3);

SELECT 
    c.title AS course_title,
    t.name AS teacher_name
FROM courses c
INNER JOIN teachers t
    ON c.teacher_id = t.id; 