-- 1.Database Setup
-- Database: student_database
CREATE DATABASE student_database;

CREATE TABLE student_table (
    student_id     INT PRIMARY KEY,
    stu_name       TEXT NOT NULL,
    department     TEXT,
    email_id       TEXT,
    phone_no       NUMERIC(15,0),
    address        TEXT,
    date_of_birth  DATE,
    gender         TEXT,
    major          TEXT,
    gpa            NUMERIC(3,2),
    grade          TEXT
);

-- 2.Data Entry

INSERT INTO student_table (student_id, stu_name, department, email_id, phone_no, address, date_of_birth, gender, major, gpa, grade) VALUES
(1,  'Amit Kumar',   'CSE', 'amit.s@uni.com',   9876543001, 'Chennai',   '2001-05-12', 'Male',   'AI',          8.50, 'A'),
(2,  'Priya Singh',  'CSE', 'priya.s@uni.com',  9876543002, 'Bangalore', '2002-09-23', 'Female', 'Data Science',7.90, 'A'),
(3,  'Rahul Sharma', 'ECE', 'rahul.s@uni.com',  9876543003, 'Hyderabad', '2000-01-15', 'Male',   'VLSI',        4.80, 'C'),
(4,  'Anita Verma',  'EEE', 'anita.v@uni.com',  9876543004, 'Delhi',     '2001-11-30', 'Female', 'Power',       6.20, 'B'),
(5,  'Mohammed Ali', 'MECH','ali.m@uni.com',    9876543005, 'Chennai',   '1999-07-19', 'Male',   'Thermal',     5.40, 'B'),
(6,  'Sneha Rao',    'CSE', 'sneha.r@uni.com',  9876543006, 'Pune',      '2002-02-10', 'Female', 'AI',          9.10, 'A'),
(7,  'Vikas Gupta',  'IT',  'vikas.g@uni.com',  9876543007, 'Jaipur',    '2001-03-25', 'Male',   'Networks',    4.30, 'C'),
(8,  'Neha Jain',    'IT',  'neha.j@uni.com',   9876543008, 'Mumbai',    '2000-12-05', 'Female', 'Security',    6.80, 'B'),
(9,  'Kiran R',      'ECE', 'kiran.r@uni.com',  9876543009, 'Chennai',   '1999-08-14', 'Male',   'Embedded',    3.90, 'D'),
(10, 'Riya Das',     'CSE', 'riya.d@uni.com',   9876543010, 'Kolkata',   '2001-06-01', 'Female', 'Data Science',8.20, 'A');

--3.Student Information Retrieval

SELECT *
FROM student_table
ORDER BY grade DESC;

--4.Query for Male Students:

SELECT *
FROM student_table
WHERE gender ILIKE 'male';

--5.Query for Students with GPA less than 5.0

SELECT *
FROM student_table
WHERE gpa < 5.0
ORDER BY gpa;

--6.Update Student Email and Grade

UPDATE student_table
SET email_id = 'rahul.sharma.updated@uni.com',
    grade    = 'B'
WHERE student_id = 3;

-- Verify update:
SELECT * FROM student_table WHERE student_id = 3;


-- 7. 7.Query for Students with Grade "B"

SELECT
    stu_name,
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, date_of_birth)) AS age_years
FROM student_table
WHERE grade = 'B';

--8.Grouping and Calculation

SELECT
    department,
    gender,
    AVG(gpa) AS avg_gpa
FROM student_table
GROUP BY department, gender
ORDER BY department, gender;

--9.Table Renaming

ALTER TABLE student_table
RENAME TO student_info;


--10.Retrieve Student with Highest GPA

SELECT
    stu_name,
    gpa
FROM student_info
ORDER BY gpa DESC
LIMIT 1;