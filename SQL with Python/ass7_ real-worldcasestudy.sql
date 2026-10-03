USE company_db;

CREATE TABLE customers (
 customer_id INT PRIMARY KEY,
 name VARCHAR(100),
 city VARCHAR(150)
 );
 
 ALTER TABLE orders ADD customer_id INT; 
 
ALTER TABLE orders
ADD FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);

CREATE TABLE products (
   product_id INT PRIMARY KEY,
   product_name VARCHAR(150),
   price DECIMAL(10,2)
   );

CREATE TABLE order_items (
  order_id INT,
  product_id INT,
  quantity INT,
  PRIMARY KEY (order_id , product_id),
  FOREIGN KEY (order_id) REFERENCES orders (order_id),
  FOREIGN KEY (product_id) REFERENCES products (product_id)
  );
  
  INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Aayushee', 'Chikhli'),
(2, 'Rahul', 'Surat'),
(3, 'Priya', 'Navsari'),
(4, 'Amit', 'Surat'),
(5, 'Neha', 'Vadodara');

INSERT INTO products (product_id, product_name, price) VALUES
(101, 'Laptop', 50000),
(102, 'Mobile', 25000),
(103, 'Headphones', 5000),
(104, 'Keyboard', 3000),
(105, 'Mouse', 1500);

INSERT INTO orders 
(order_id, user_id, order_amount, order_date, customer_id) VALUES
(1001, NULL, 55000, '2026-01-10', 1),
(1002, NULL, 30000, '2026-01-15', 2),
(1003, NULL, 25000, '2026-02-05', 1),
(1004, NULL, 60000, '2026-02-20', 3),
(1005, NULL, 52000, '2026-03-10', 4),
(1006, NULL, 15000, '2026-03-15', 2);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1001, 101, 1),
(1001, 103, 1),
(1002, 102, 1),
(1002, 105, 2),
(1003, 102, 1),
(1004, 101, 1),
(1004, 104, 2),
(1005, 101, 1),
(1005, 103, 1),
(1006, 103, 3);

  SELECT * FROM customers;
  SELECT * FROM orders;
  SELECT * FROM products;
  SELECT * FROM order_items;
  
  -- total orders per customer
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

-- Find customers with no orders
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Highest selling product
SELECT
    p.product_id,
    p.product_name,
    SUM(oi.quantity) AS total_quantity
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC
LIMIT 1;

-- Monthly sales report
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(order_amount) AS total_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month; 

-- Customers with total purchases > 50,000
SELECT
    c.customer_id,
    c.name,
    SUM(o.order_amount) AS total_purchase
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.order_amount) > 50000;

-- Top 3 cities by revenue
SELECT
    c.city,
    SUM(o.order_amount) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC
LIMIT 3;
