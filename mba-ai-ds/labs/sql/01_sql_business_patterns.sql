-- Lab SQL-01 · The 12 SQL patterns every analyst uses (Module M7) · PostgreSQL
-- 🧒 SQL = asking the librarian for exactly the books you want.
-- Self-contained: creates its own small tables. Run the whole file in pgAdmin / psql, then re-run
-- one pattern at a time and change something.
--   CREATE DATABASE sql_lab;   then connect to sql_lab and run this file.

DROP TABLE IF EXISTS orders, customers, agents, interval_stats CASCADE;

CREATE TABLE customers (
    customer_id  INT PRIMARY KEY,
    name         VARCHAR(50) NOT NULL,
    city         VARCHAR(30) NOT NULL,
    signup_date  DATE NOT NULL
);

CREATE TABLE orders (
    order_id     INT PRIMARY KEY,
    customer_id  INT REFERENCES customers(customer_id),
    order_date   DATE NOT NULL,
    amount_inr   NUMERIC(10,2) NOT NULL
);

CREATE TABLE agents (
    agent_id     INT PRIMARY KEY,
    agent_name   VARCHAR(50) NOT NULL,
    team_leader_id INT REFERENCES agents(agent_id)   -- self-reference: TLs are agents too
);

CREATE TABLE interval_stats (
    stat_date    DATE NOT NULL,
    agent_id     INT REFERENCES agents(agent_id),
    calls        INT NOT NULL,
    aht_sec      INT NOT NULL
);

INSERT INTO customers VALUES
(1,'Aarav','Mumbai','2025-01-10'),(2,'Diya','Pune','2025-01-22'),(3,'Kabir','Mumbai','2025-02-05'),
(4,'Meera','Delhi','2025-02-18'),(5,'Rohan','Delhi','2025-03-02'),(6,'Sana','Hyderabad','2025-03-15');

INSERT INTO orders VALUES
(101,1,'2025-01-12',1200),(102,1,'2025-02-15',800),(103,2,'2025-01-25',450),(104,3,'2025-02-07',2300),
(105,3,'2025-03-09',1500),(106,3,'2025-03-28',700),(107,4,'2025-02-20',950),(108,5,'2025-03-05',300),
(109,1,'2025-03-20',1100),(110,4,'2025-03-22',1250),(111,2,'2025-03-25',600),(112,1,'2025-03-20',1100);

INSERT INTO agents VALUES (1,'Priya (TL)',NULL),(2,'Imran',1),(3,'Neha',1),(4,'Arjun',1),(5,'Farah',1);

INSERT INTO interval_stats VALUES
('2025-03-01',2,52,310),('2025-03-01',3,61,285),('2025-03-01',4,47,340),('2025-03-01',5,58,300),
('2025-03-02',2,49,305),('2025-03-02',3,66,290),('2025-03-02',4,55,320),('2025-03-02',5,51,330),
('2025-03-03',2,60,298),('2025-03-03',3,58,282),('2025-03-03',4,62,315),('2025-03-03',5,57,295);

-- P1 · Filter + sort + limit: the 3 biggest orders
SELECT order_id, customer_id, amount_inr FROM orders ORDER BY amount_inr DESC LIMIT 3;

-- P2 · GROUP BY + HAVING: cities with total sales above ₹2,000 (WHERE filters rows, HAVING filters groups)
SELECT c.city, SUM(o.amount_inr) AS sales
FROM orders o JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING SUM(o.amount_inr) > 2000
ORDER BY sales DESC;

-- P3 · LEFT JOIN to find what's MISSING: customers who never ordered
SELECT c.name
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

-- P4 · CASE WHEN: bucket values (like Excel IF)
SELECT order_id, amount_inr,
       CASE WHEN amount_inr >= 1500 THEN 'Large'
            WHEN amount_inr >= 800  THEN 'Medium'
            ELSE 'Small' END AS order_size
FROM orders;

-- P5 · Top-N per group: best order per customer (ROW_NUMBER + PARTITION BY)
SELECT * FROM (
    SELECT o.*, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount_inr DESC) AS rn
    FROM orders o
) t WHERE rn = 1;

-- P6 · Running total (cumulative sales by date)
SELECT order_date, SUM(amount_inr) AS daily_sales,
       SUM(SUM(amount_inr)) OVER (ORDER BY order_date) AS running_total
FROM orders GROUP BY order_date ORDER BY order_date;

-- P7 · Month-over-month change with LAG (CTE keeps it readable)
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date)::date AS month, SUM(amount_inr) AS sales
    FROM orders GROUP BY 1
)
SELECT month, sales,
       LAG(sales) OVER (ORDER BY month) AS prev_month,
       ROUND(100.0 * (sales - LAG(sales) OVER (ORDER BY month)) / LAG(sales) OVER (ORDER BY month), 1) AS mom_pct
FROM monthly ORDER BY month;

-- P8 · Share of total (% contribution) with a window over everything
SELECT c.city, SUM(o.amount_inr) AS sales,
       ROUND(100.0 * SUM(o.amount_inr) / SUM(SUM(o.amount_inr)) OVER (), 1) AS pct_of_total
FROM orders o JOIN customers c USING (customer_id)
GROUP BY c.city ORDER BY sales DESC;

-- P9 · Find duplicates (order 112 is a copy of 109)
SELECT customer_id, order_date, amount_inr, COUNT(*) AS copies
FROM orders GROUP BY customer_id, order_date, amount_inr HAVING COUNT(*) > 1;

-- P10 · Cohort: customers grouped by signup month, and their total spend
SELECT DATE_TRUNC('month', c.signup_date)::date AS cohort, COUNT(DISTINCT c.customer_id) AS customers,
       SUM(o.amount_inr) AS cohort_sales,
       ROUND(SUM(o.amount_inr) / COUNT(DISTINCT c.customer_id), 0) AS sales_per_customer
FROM customers c LEFT JOIN orders o USING (customer_id)
GROUP BY 1 ORDER BY 1;

-- P11 · Self-join: each agent with their team leader
SELECT a.agent_name, tl.agent_name AS team_leader
FROM agents a LEFT JOIN agents tl ON tl.agent_id = a.team_leader_id
WHERE a.team_leader_id IS NOT NULL;

-- P12 · Weighted average + rank: AHT must be weighted by calls, then rank agents
SELECT a.agent_name,
       SUM(s.calls) AS calls,
       ROUND(SUM(s.calls * s.aht_sec)::numeric / SUM(s.calls), 1) AS weighted_aht,
       RANK() OVER (ORDER BY SUM(s.calls * s.aht_sec)::numeric / SUM(s.calls)) AS aht_rank
FROM interval_stats s JOIN agents a USING (agent_id)
GROUP BY a.agent_name ORDER BY aht_rank;

-- Your turn
-- a) P5 variant: the 2 most recent orders per customer.
-- b) P12: why is AVG(aht_sec) wrong here? Compare it with the weighted average.
-- c) Load labs/data/call_centre_intervals.csv with pgAdmin's Import tool and rewrite P6 and P7 for daily calls.
