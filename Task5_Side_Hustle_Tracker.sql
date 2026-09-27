-- TASK 5 — Side Hustle Tracker (PostgreSQL)
-- Tracks time invested, content published, income and expenses
-- for the growth plan in /growth-plan. All sample data is illustrative.

-- Run once (in psql / pgAdmin), then connect to the database:
-- CREATE DATABASE side_hustle_tracker;
-- \c side_hustle_tracker

-- 1. TABLE CREATION
DROP TABLE IF EXISTS income, expenses, content, time_log, ventures CASCADE;

CREATE TABLE ventures (
    venture_id   SERIAL PRIMARY KEY,
    venture_name VARCHAR(100) NOT NULL UNIQUE,
    category     VARCHAR(30)  NOT NULL CHECK (category IN ('Content','Book','Freelance','Upskill','Investment')),
    start_date   DATE NOT NULL,
    status       VARCHAR(20)  NOT NULL DEFAULT 'Active' CHECK (status IN ('Planned','Active','Paused','Done'))
);

CREATE TABLE time_log (
    log_id     SERIAL PRIMARY KEY,
    venture_id INT NOT NULL REFERENCES ventures(venture_id),
    log_date   DATE NOT NULL,
    minutes    INT  NOT NULL CHECK (minutes > 0),
    activity   VARCHAR(150) NOT NULL
);

CREATE TABLE content (
    content_id   SERIAL PRIMARY KEY,
    venture_id   INT NOT NULL REFERENCES ventures(venture_id),
    platform     VARCHAR(20) NOT NULL CHECK (platform IN ('YouTube','YouTube Shorts','Instagram','LinkedIn','Book','Blog')),
    title        VARCHAR(200) NOT NULL,
    publish_date DATE NOT NULL,
    views        INT NOT NULL DEFAULT 0,
    likes        INT NOT NULL DEFAULT 0,
    new_followers INT NOT NULL DEFAULT 0
);

CREATE TABLE income (
    income_id   SERIAL PRIMARY KEY,
    venture_id  INT NOT NULL REFERENCES ventures(venture_id),
    income_date DATE NOT NULL,
    source      VARCHAR(100) NOT NULL,
    amount_inr  NUMERIC(10,2) NOT NULL CHECK (amount_inr >= 0)
);

CREATE TABLE expenses (
    expense_id   SERIAL PRIMARY KEY,
    venture_id   INT NOT NULL REFERENCES ventures(venture_id),
    expense_date DATE NOT NULL,
    item         VARCHAR(150) NOT NULL,
    amount_inr   NUMERIC(10,2) NOT NULL CHECK (amount_inr >= 0),
    is_asset     BOOLEAN NOT NULL DEFAULT FALSE   -- equipment kept long-term (mic, tripod…)
);

-- 2. DATA INSERTION (sample data — replace with real entries every Sunday)
INSERT INTO ventures (venture_name, category, start_date, status) VALUES
('YouTube - Analyst Channel',   'Content',    '2026-10-01', 'Active'),
('Instagram - Poetry',          'Content',    '2026-10-01', 'Active'),
('Explanatory eBook',           'Book',       '2026-12-01', 'Planned'),
('Freelance Dashboards',        'Freelance',  '2026-12-01', 'Planned'),
('Upskilling (Excel/SQL/PBI)',  'Upskill',    '2026-10-01', 'Active'),
('Index Fund SIP',              'Investment', '2026-10-05', 'Active');

INSERT INTO time_log (venture_id, log_date, minutes, activity) VALUES
(5, '2026-10-05', 60,  'Power Query basics'),
(5, '2026-10-06', 60,  'Cleaned messy interval report'),
(2, '2026-10-06', 30,  'Wrote 1 poem'),
(1, '2026-10-07', 45,  'Outlined video #1'),
(5, '2026-10-08', 60,  'Automated report refresh'),
(1, '2026-10-10', 120, 'Recorded video #1'),
(1, '2026-10-10', 120, 'Edited video #1'),
(1, '2026-10-11', 60,  'Thumbnail + upload + 2 Shorts'),
(2, '2026-10-11', 30,  'Scheduled 3 poetry posts'),
(5, '2026-10-12', 60,  'XLOOKUP and dynamic arrays'),
(5, '2026-10-13', 60,  'Rebuilt lookup sheet'),
(1, '2026-10-17', 240, 'Recorded + edited video #2'),
(2, '2026-10-18', 45,  'Wrote 2 poems'),
(4, '2026-12-13', 180, 'Fiverr Excel cleanup gig'),
(4, '2026-12-27', 300, 'Sales dashboard for local shop'),
(3, '2026-12-06', 240, 'Wrote chapters 1-2'),
(3, '2026-12-20', 240, 'Wrote chapters 3-4');

INSERT INTO content (venture_id, platform, title, publish_date, views, likes, new_followers) VALUES
(1, 'YouTube',        'My journey as a Real-Time Analyst',   '2026-10-11', 320, 28, 14),
(1, 'YouTube Shorts', 'What does an RTA actually do?',        '2026-10-11', 1450, 90, 22),
(1, 'YouTube Shorts', '3 Excel tricks for interval reports',  '2026-10-12', 2100, 140, 35),
(2, 'Instagram',      'Poem: Night Shift',                    '2026-10-08', 610, 75, 18),
(2, 'Instagram',      'Poem: Chai at 3 AM',                   '2026-10-11', 980, 130, 31),
(1, 'YouTube',        'XLOOKUP vs VLOOKUP for ops reports',   '2026-10-18', 540, 41, 26);

INSERT INTO income (venture_id, income_date, source, amount_inr) VALUES
(4, '2026-12-14', 'Fiverr - Excel cleanup gig',       1500.00),
(4, '2026-12-28', 'Local shop - sales dashboard',     4000.00),
(3, '2027-01-20', 'Amazon KDP royalties',              850.00);

INSERT INTO expenses (venture_id, expense_date, item, amount_inr, is_asset) VALUES
(1, '2026-10-02', 'Wireless lavalier mic',   2499.00, TRUE),
(1, '2026-10-02', 'Phone tripod',             899.00, TRUE),
(1, '2026-10-03', 'Softbox light',           2199.00, TRUE),
(5, '2026-10-04', 'Power BI course (sale)',   499.00, FALSE),
(3, '2026-12-05', 'Book cover design',       1500.00, FALSE),
(6, '2026-10-05', 'SIP instalment #1',       5000.00, TRUE);

-- 3. VIEWS & ANALYTICS

-- a) Hours invested per venture
SELECT v.venture_name,
       ROUND(SUM(t.minutes) / 60.0, 1) AS hours_invested
FROM ventures v
JOIN time_log t ON t.venture_id = v.venture_id
GROUP BY v.venture_name
ORDER BY hours_invested DESC;

-- b) Weekly hours (Sunday review: am I hitting ~15 hrs/week?)
SELECT DATE_TRUNC('week', log_date)::date AS week_start,
       ROUND(SUM(minutes) / 60.0, 1)       AS total_hours,
       ROUND(SUM(minutes) FILTER (WHERE venture_id = 5) / 60.0, 1) AS upskill_hours
FROM time_log
GROUP BY week_start
ORDER BY week_start;

-- c) Content performance: best posts by engagement rate
SELECT platform, title, views, likes,
       ROUND(100.0 * likes / NULLIF(views, 0), 2) AS engagement_pct,
       RANK() OVER (PARTITION BY platform ORDER BY views DESC) AS rank_in_platform
FROM content
ORDER BY platform, rank_in_platform;

-- d) Running follower growth per venture
SELECT v.venture_name, c.publish_date, c.title, c.new_followers,
       SUM(c.new_followers) OVER (PARTITION BY c.venture_id ORDER BY c.publish_date, c.content_id) AS cumulative_followers
FROM content c
JOIN ventures v ON v.venture_id = c.venture_id
ORDER BY v.venture_name, c.publish_date;

-- e) Profit & loss per venture (investments tracked separately)
CREATE OR REPLACE VIEW venture_pnl AS
SELECT v.venture_name,
       v.category,
       COALESCE(i.total_income, 0)   AS total_income,
       COALESCE(e.total_expense, 0)  AS total_expense,
       COALESCE(i.total_income, 0) - COALESCE(e.total_expense, 0) AS net_inr
FROM ventures v
LEFT JOIN (SELECT venture_id, SUM(amount_inr) AS total_income  FROM income   GROUP BY venture_id) i ON i.venture_id = v.venture_id
LEFT JOIN (SELECT venture_id, SUM(amount_inr) AS total_expense FROM expenses GROUP BY venture_id) e ON e.venture_id = v.venture_id
WHERE v.category <> 'Investment';

SELECT * FROM venture_pnl ORDER BY net_inr DESC;

-- f) Earnings per hour — which hustle is actually worth my time?
SELECT p.venture_name,
       p.net_inr,
       ROUND(SUM(t.minutes) / 60.0, 1) AS hours,
       ROUND(p.net_inr / NULLIF(SUM(t.minutes) / 60.0, 0), 2) AS net_inr_per_hour
FROM venture_pnl p
JOIN ventures v ON v.venture_name = p.venture_name
LEFT JOIN time_log t ON t.venture_id = v.venture_id
GROUP BY p.venture_name, p.net_inr
ORDER BY net_inr_per_hour DESC NULLS LAST;

-- g) Monthly cash flow (for tax records & monthly review)
SELECT month,
       SUM(income)  AS income_inr,
       SUM(expense) AS expense_inr,
       SUM(income) - SUM(expense) AS net_inr
FROM (
    SELECT DATE_TRUNC('month', income_date)::date AS month, amount_inr AS income, 0 AS expense FROM income
    UNION ALL
    SELECT DATE_TRUNC('month', expense_date)::date, 0, amount_inr
    FROM expenses e JOIN ventures v ON v.venture_id = e.venture_id
    WHERE v.category <> 'Investment'
) cash
GROUP BY month
ORDER BY month;
