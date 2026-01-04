CREATE DATABASE IF NOT EXISTS ecommerce; -- database name ecommerce
USE ecommerce;

-- Creating users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);


-- Creating products table

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    stock INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);


-- Creating orders table

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- Creating order_items table

CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- inserting some data

INSERT INTO users (name, email) VALUES 
('Mahek','mahek@example.com'), 
('Anam','anam@example.com'),
('Charlie','charlie@example.com');

INSERT INTO products (name, stock, price) VALUES 
('Laptop', 5, 50000), 
('Mouse', 0, 500), 
('Keyboard', 10, 1500);

INSERT INTO orders (user_id, order_date) VALUES 
(1,'2026-01-01'),
(2,'2026-01-02');

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES 
(1, 1, 1, 50000),
(1, 2, 2, 500),
(2, 3, 1, 1500);


-- Queries 

--  Fetch products that are out of stock
SELECT * FROM products WHERE stock = 0;

-- Fetch orders with items and total amount
SELECT o.id AS order_id, u.name AS user_name, SUM(oi.quantity * oi.price) AS total_amount
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY o.id;

--  Top 5 users with highest spending
SELECT u.id, u.name, SUM(oi.quantity * oi.price) AS total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY u.id
ORDER BY total_spent DESC
LIMIT 5;
