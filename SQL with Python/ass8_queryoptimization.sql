
-- Add index on orders.customer_id
USE company_db;

CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

SHOW INDEX FROM orders;

-- Use EXPLAIN to analyze a query
EXPLAIN SELECT * FROM orders
WHERE customer_id = 1;

-- Optimized JOIN query
EXPLAIN
SELECT
    c.name,
    c.city,
    o.order_id,
    o.order_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city = 'Surat';

-- Task 4: When an index should not be used

-- Indexes should not be used when:
-- 1. The table is very small.
-- 2. The column has very few unique values.
-- 3. The table has frequent INSERT, UPDATE, or DELETE operations.
-- 4. The query returns a large percentage of the table's rows.
-- 5. The index is not useful for the query condition.