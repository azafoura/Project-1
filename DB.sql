-- Create the products table
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(255),
  category VARCHAR(50),
  stock_level INT,
  price DECIMAL(10, 2),
  expiration_date DATE,
  low_stock_threshold INT
);

-- Insert data into the products table
INSERT INTO products (product_id, name, category, stock_level, price, expiration_date, low_stock_threshold)
VALUES
  (1, 'Whole Milk', 'Dairy', 50, 1.99, '2024-10-01', 10),
  (2, 'Bananas', 'Fruits', 100, 0.59, '2024-09-20', 20),
  (3, 'Chicken Breast', 'Meat', 75, 5.99, '2024-09-25', 15),
  (4, 'Eggs (12-pack)', 'Dairy', 200, 2.99, '2024-09-18', 30),
  (5, 'Apples', 'Fruits', 150, 0.99, '2024-09-28', 20),
  (6, 'Broccoli', 'Vegetables', 100, 1.29, '2024-09-22', 15),
  (7, 'Carrots', 'Vegetables', 120, 0.79, '2024-09-30', 25);
  (8, 'Spaghetti', 'Pasta', 120, 1.49, '2024-12-01', 25),
  (9, 'Tomato Sauce', 'Canned Goods', 140, 1.99, '2025-01-15', 20),
  (10, 'Cheddar Cheese', 'Dairy', 85, 4.99, '2024-09-29', 10),
  (11, 'Lettuce', 'Vegetables', 90, 1.79, '2024-09-18', 10),
  (12, 'Rice (1kg)', 'Grains', 160, 3.99, '2025-06-01', 20);

-- Create the sales table
CREATE TABLE sales (
  sale_id INT PRIMARY KEY,
  product_id INT,
  date DATE,
  quantity_sold INT,
  total_sale_value DECIMAL(10, 2),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert data into the sales table
INSERT INTO sales (sale_id, product_id, date, quantity_sold, total_sale_value)
VALUES
  (1001, 1, '2024-09-01', 20, 39.8),
  (1002, 2, '2024-09-06', 50, 29.5),
  (1003, 3, '2024-09-03', 15, 89.85),
  (1004, 4, '2024-09-07', 50, 149.5),
  (1005, 5, '2024-09-04', 30, 29.7),
  (1006, 6, '2024-09-09', 25, 32.25),
  (1007, 7, '2024-09-12', 40, 31.6);
  (1008, 8, '2024-09-08', 40, 59.6),
  (1009, 9, '2024-09-10', 50, 99.5),
  (1010, 10, '2024-09-05', 25, 124.75),
  (1011, 11, '2024-09-07', 30, 53.7),
  (1012, 12, '2024-09-11', 45, 179.55);
