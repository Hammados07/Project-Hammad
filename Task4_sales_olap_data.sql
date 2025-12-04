-- Database: sales_olap

CREATE DATABASE sales_olap;

-- 1. TABLE CREATION
CREATE TABLE sales_sample (
    product_id    INT,
    region        VARCHAR(50),
    date          DATE,
    sales_amount  NUMERIC(10,2)
);

-- 2. INSERT SAMPLE DATA

INSERT INTO sales_sample (product_id, region, date, sales_amount) VALUES
(101, 'East',  '2025-01-01', 1000.00),
(101, 'East',  '2025-01-02', 1200.00),
(102, 'East',  '2025-01-01',  800.00),
(102, 'West',  '2025-01-01',  900.00),
(103, 'West',  '2025-01-02', 1100.00),
(103, 'North', '2025-01-01', 1500.00),
(101, 'South', '2025-01-03',  700.00),
(102, 'South', '2025-01-03',  650.00),
(103, 'East',  '2025-01-03',  950.00),
(101, 'West',  '2025-01-02', 1300.00);

-- 3. OLAP OPERATIONS

-- (3a) DRILL DOWN: Analyze sales data at a more detailed level

SELECT
    region,
    product_id,
    SUM(sales_amount) AS total_sales
FROM sales_sample
GROUP BY region, product_id
ORDER BY region, product_id;

-- (3b) ROLLUP: To summarize sales data at different levels of granularity

SELECT
    region,
    product_id,
    SUM(sales_amount) AS total_sales
FROM sales_sample
GROUP BY ROLLUP (region, product_id)
ORDER BY region NULLS LAST, product_id NULLS LAST;

-- (3c) CUBE: To analyze sales data from multiple dimensions simultaneously

SELECT
    region,
    product_id,
    date,
    SUM(sales_amount) AS total_sales
FROM sales_sample
GROUP BY CUBE (region, product_id, date)
ORDER BY region NULLS LAST, product_id NULLS LAST, date NULLS LAST;

-- (3d) SLICE:  To extract a subset of data based on specific criteria
-- for particular region
SELECT
    product_id,
    region,
    date,
    sales_amount
FROM sales_sample
WHERE region = 'East'
ORDER BY date, product_id;

-- for particular date range
SELECT
    product_id,
    region,
    date,
    sales_amount
FROM sales_sample
WHERE date BETWEEN '2025-01-01' AND '2025-01-02'
ORDER BY date, region, product_id;

-- (3e) DICE: To extract data based on multiple criteria
SELECT
    product_id,
    region,
    date,
    sales_amount
FROM sales_sample
WHERE product_id IN (101, 102)
  AND region IN ('East', 'West')
  AND date BETWEEN '2025-01-01' AND '2025-01-03'
ORDER BY date, region, product_id;