Create database academics_database;
use academics_database;
# 1. TABLE CREATION
Create table StudentInfo (
STU_ID int PRIMARY KEY,
STU_NAME varchar(100) NOT NULL,
DOB Date,
PHONE_NO varchar(20),
EMAIL_ID varchar(100),
ADDRESS varchar(250)
);

create table CoursesInfo (
COURSE_ID int PRIMARY KEY,
COURSE_NAME varchar(100) NOT NULL,
COURSE_INSTRUCTOR_NAME varchar(100) NOT NULL
);

Create table EnrollmentInfo (
ENROLLMENT_ID int PRIMARY KEY,
STU_ID int NOT NULL,
COURSE_ID int NOT NULL,
ENROLL_STATUS varchar(20) NOT NULL check (ENROLL_STATUS IN ('Enrolled','Not Enrolled')),
constraint fk_enroll_student FOREIGN KEY (STU_ID) REFERENCES StudentInfo(STU_ID),
constraint fk_enroll_course FOREIGN KEY (COURSE_ID) REFERENCES CoursesInfo(COURSE_ID)
);

# 2. DATA INSERTION
insert into StudentInfo (STU_ID, STU_NAME, DOB, PHONE_NO, EMAIL_ID, ADDRESS) values
(1, 'Amit Kumar','2001-05-12', '9876543210', 'amit@yahoo.com','Chennai'),
(2, 'Priya Singh','2002-09-23', '9876543211', 'priya@gmail.com','Bangalore'),
(3, 'Rahul Sharma','2000-01-15', '9876543212', 'rahul@outlook.com','Hyderabad'),
(4, 'Anita Verma','2001-11-30', '9876543213', 'anita@outlook.com','Delhi'),
(5, 'Mohammed Hammad','2002-03-05', '9876543214', 'hammad@gmail.com','Mumbai');

insert into CoursesInfo (COURSE_ID, COURSE_NAME, COURSE_INSTRUCTOR_NAME) values
(101, 'Database Management', 'Dr. Rao'),
(102, 'Data Structures', 'Dr. Ali'),
(103, 'Operating Systems', 'Prof. Iyer'),
(104, 'Computer Networks', 'Prof. Kapoor'),
(105, 'Statistics for Data Science', 'Dr. Nair');

insert into EnrollmentInfo (ENROLLMENT_ID, STU_ID, COURSE_ID, ENROLL_STATUS) values
(1, 1, 101, 'Enrolled'),
(2, 1, 102, 'Enrolled'),
(3, 2, 101, 'Enrolled'),
(4, 2, 103, 'Enrolled'),
(5, 3, 104, 'Enrolled'),
(6, 4, 101, 'Enrolled'),
(7, 4, 105, 'Enrolled'),
(8, 5, 103, 'Not Enrolled'),
(9, 4, 104, 'Not Enrolled'),
(10, 3, 101, 'Not Enrolled');

# 3. DATA Retrieval
# a) Write a query to retrieve student details, such as student name, contact informations, and Enrollment status.
SELECT
    s.STU_ID,
    s.STU_NAME,
    s.PHONE_NO,
    s.EMAIL_ID,
    s.ADDRESS,
    e.COURSE_ID,
    c.COURSE_NAME,
    e.ENROLL_STATUS
FROM StudentInfo s
LEFT JOIN EnrollmentInfo e ON s.STU_ID = e.STU_ID
LEFT JOIN CoursesInfo c ON e.COURSE_ID = c.COURSE_ID
ORDER BY s.STU_ID, c.COURSE_ID;

# b)  Write a query to retrieve a list of courses in which a specific student is enrolled.
SELECT
    s.STU_NAME,
    c.COURSE_ID,
    c.COURSE_NAME,
    e.ENROLL_STATUS
FROM StudentInfo s
JOIN EnrollmentInfo e ON s.STU_ID = e.STU_ID
JOIN CoursesInfo c ON e.COURSE_ID = c.COURSE_ID
WHERE s.STU_ID = 1 AND e.ENROLL_STATUS = 'Enrolled';

# c) Write a query to retrieve course information, including course name, instructor information.
SELECT
    COURSE_ID,
    COURSE_NAME,
    COURSE_INSTRUCTOR_NAME
FROM CoursesInfo
ORDER BY COURSE_ID;

# d) Write a query to retrieve course information for a specific course .
SELECT
    COURSE_ID,
    COURSE_NAME,
    COURSE_INSTRUCTOR_NAME
FROM CoursesInfo
WHERE COURSE_ID = 101;

# e) Write a query to retrieve course information for multiple courses.
SELECT
    COURSE_ID,
    COURSE_NAME,
    COURSE_INSTRUCTOR_NAME
FROM CoursesInfo
WHERE COURSE_ID IN (101,102,103)
ORDER BY COURSE_ID;

# 4. Reporting and Analytics (Using joining queries)
# a) Write a query to retrieve the number of students enrolled in each course
SELECT
    c.COURSE_ID,
    c.COURSE_NAME,
    COUNT(*) AS total_enrolled
FROM CoursesInfo c
JOIN EnrollmentInfo e
    ON c.COURSE_ID = e.COURSE_ID
WHERE e.ENROLL_STATUS = 'Enrolled'
GROUP BY c.COURSE_ID, c.COURSE_NAME
ORDER BY total_enrolled DESC;

# b) Write a query to retrieve the list of students enrolled in a specific course
SELECT
    c.COURSE_ID,
    c.COURSE_NAME,
    s.STU_ID,
    s.STU_NAME
FROM EnrollmentInfo e
JOIN StudentInfo s ON e.STU_ID = s.STU_ID
JOIN CoursesInfo c ON e.COURSE_ID = c.COURSE_ID
WHERE e.COURSE_ID = 101
  AND e.ENROLL_STATUS = 'Enrolled'
ORDER BY s.STU_NAME;

# c) Write a query to retrieve the count of enrolled students for each instructor.
SELECT c.COURSE_INSTRUCTOR_NAME,
    COUNT(DISTINCT e.STU_ID) AS total_students
FROM CoursesInfo c
JOIN EnrollmentInfo e
    ON c.COURSE_ID = e.COURSE_ID
WHERE e.ENROLL_STATUS = 'Enrolled'
GROUP BY c.COURSE_INSTRUCTOR_NAME
ORDER BY total_students DESC;

# d) Write a query to retrieve the list of students who are enrolled in multiple courses
SELECT
    s.STU_ID,
    s.STU_NAME,
    COUNT(*) AS course_count
FROM EnrollmentInfo e
JOIN StudentInfo s ON e.STU_ID = s.STU_ID
WHERE e.ENROLL_STATUS = 'Enrolled'
GROUP BY s.STU_ID, s.STU_NAME
HAVING COUNT(*) > 1
ORDER BY course_count DESC;

# e) Write a query to retrieve the courses that have the highest number of enrolled students(arranging from highest to lowest)
SELECT
    c.COURSE_ID,
    c.COURSE_NAME,
    COUNT(*) AS total_enrolled
FROM CoursesInfo c
JOIN EnrollmentInfo e
    ON c.COURSE_ID = e.COURSE_ID
WHERE e.ENROLL_STATUS = 'Enrolled'
GROUP BY c.COURSE_ID, c.COURSE_NAME
ORDER BY total_enrolled DESC, c.COURSE_NAME;