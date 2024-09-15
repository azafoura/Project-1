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
  -- ... (previous rows)
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
  -- ... (previous rows)
  (1008, 8, '2024-09-08', 40, 59.6),
  (1009, 9, '2024-09-10', 50, 99.5),
  (1010, 10, '2024-09-05', 25, 124.75),
  (1011, 11, '2024-09-07', 30, 53.7),
  (1012, 12, '2024-09-11', 45, 179.55);
