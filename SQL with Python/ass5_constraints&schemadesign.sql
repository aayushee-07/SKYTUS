USE company_db;

 -- Create users table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(100) UNIQUE,
  password VARCHAR(150) NOT NULL
);

-- Add foreign key between orders and users
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_amount DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
    
SHOW INDEXES FROM users;
    
-- Create index on email
CREATE INDEX idx_email ON users(email);
    
-- Create view to display user order summary
CREATE VIEW user_order_summary AS
SELECT
    u.id AS user_id,
    u.email,
    o.order_id,
    o.order_amount,
    o.order_date
FROM users u
INNER JOIN orders o
ON u.id = o.user_id;
    

