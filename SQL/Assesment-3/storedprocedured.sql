USE sqlassesment;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO students (name, email, is_active)
VALUES
('Aayushee', 'aayushee@gmail.com', TRUE),
('Rahul', 'rahul@gmail.com', FALSE),
('Priya', 'priya@gmail.com', TRUE);

SELECT * FROM students;

DELIMITER &&

CREATE PROCEDURE GetStudentsByStatus(IN p_status BOOLEAN)
BEGIN
    SELECT *
    FROM students
    WHERE is_active = p_status;
END &&

DELIMITER ;

CALL GetStudentsByStatus(TRUE);
CALL GetStudentsByStatus(FALSE);