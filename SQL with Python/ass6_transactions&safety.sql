USE company_db;

-- Create accounts table
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10,2)
);

-- Insert accounts
INSERT INTO accounts VALUES
(1, 'Aayushee', 10000),
(2, 'Riyaa', 5000);

-- Rollback example
START TRANSACTION;

INSERT INTO accounts VALUES
(3, 'Priya', 7000);

ROLLBACK;

SELECT * FROM accounts;

-- Commit example
START TRANSACTION;

INSERT INTO accounts VALUES
(3, 'Priya', 7000);

COMMIT;

SELECT * FROM accounts;

-- Transfer ₹2,000 from Aayushee to Riyaa
START TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 2;

COMMIT;

SELECT * FROM accounts;