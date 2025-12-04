-- Database: Event Management System

CREATE DATABASE events_management;

-- 1. TABLE CREATION

CREATE TABLE Events (
    Event_Id          INT PRIMARY KEY,
    Event_Name        VARCHAR(100) NOT NULL,
    Event_Date        DATE NOT NULL,
    Event_Location    VARCHAR(100),
    Event_Description TEXT
);

CREATE TABLE Attendees (
    Attendee_Id    INT PRIMARY KEY,
    Attendee_Name  VARCHAR(100) NOT NULL,
    Attendee_Phone VARCHAR(20),
    Attendee_Email VARCHAR(100),
    Attendee_City  VARCHAR(100)
);

CREATE TABLE Registrations (
    Registration_Id     INT PRIMARY KEY,
    Event_Id            INT NOT NULL,
    Attendee_Id         INT NOT NULL,
    Registration_Date   DATE NOT NULL,
    Registration_Amount NUMERIC(10,2) NOT NULL,
    CONSTRAINT fk_reg_event
        FOREIGN KEY (Event_Id) REFERENCES Events(Event_Id),
    CONSTRAINT fk_reg_attendee
        FOREIGN KEY (Attendee_Id) REFERENCES Attendees(Attendee_Id)
);

-- 2. DATA INSERTION

INSERT INTO Events (Event_Id, Event_Name, Event_Date, Event_Location, Event_Description) VALUES
(1, 'Tech Conference',  '2025-01-15', 'Chennai',   'Annual technology conference'),
(2, 'Data Summit',      '2025-02-10', 'Bangalore', 'Data analytics and AI summit'),
(3, 'Career Fair',      '2025-03-05', 'Hyderabad', 'Campus career opportunities'),
(4, 'Workshop on SQL',  '2025-01-25', 'Online',    'Hands-on SQL workshop');

INSERT INTO Attendees (Attendee_Id, Attendee_Name, Attendee_Phone, Attendee_Email, Attendee_City) VALUES
(101, 'Amit Kumar',   '9876500001', 'amit.event@example.com',   'Chennai'),
(102, 'Priya Singh',  '9876500002', 'priya.event@example.com',  'Bangalore'),
(103, 'Rahul Sharma', '9876500003', 'rahul.event@example.com',  'Hyderabad'),
(104, 'Anita Verma',  '9876500004', 'anita.event@example.com',  'Delhi'),
(105, 'Mohammed Ali', '9876500005', 'ali.event@example.com',    'Chennai'),
(106, 'Sneha Rao',    '9876500006', 'sneha.event@example.com',  'Pune');

INSERT INTO Registrations (Registration_Id, Event_Id, Attendee_Id, Registration_Date, Registration_Amount) VALUES
(1, 1, 101, '2024-12-20', 1500.00),
(2, 1, 102, '2024-12-21', 1500.00),
(3, 2, 103, '2024-12-22', 2000.00),
(4, 2, 104, '2024-12-23', 2000.00),
(5, 3, 105, '2025-02-10',  500.00),
(6, 4, 101, '2025-01-10',  800.00),
(7, 4, 106, '2025-01-11',  800.00);

-- 3. MANAGE EVENT DETAILS

-- (3a) Inserting a new event
INSERT INTO Events (Event_Id, Event_Name, Event_Date, Event_Location, Event_Description) VALUES
(5, 'Cloud Computing Meetup', '2025-04-01', 'Mumbai', 'Meetup on cloud technologies');

-- (3b) Updating an event's information
UPDATE Events
SET Event_Location = 'Online - Mumbai'
WHERE Event_Id = 5;

-- (3c) Deleting an event
DELETE FROM Events
WHERE Event_Id = 5;

-- 4. MANAGE ATTENDEES & REGISTRATIONS

-- (4a) Inserting a new attendee
INSERT INTO Attendees (Attendee_Id, Attendee_Name, Attendee_Phone, Attendee_Email, Attendee_City) VALUES
(107, 'Kiran R', '9876500007', 'kiran.event@example.com', 'Chennai');

-- (4b) Registering an attendee for an event
INSERT INTO Registrations (Registration_Id, Event_Id, Attendee_Id, Registration_Date, Registration_Amount) VALUES
(8, 1, 107, '2024-12-25', 1500.00);

-- 5. QUERIES FOR EVENT INFO & STATISTICS
-- List all events
SELECT * FROM Events ORDER BY Event_Date;
-- Attendee list for a specific event
SELECT
    e.Event_Id,
    e.Event_Name,
    a.Attendee_Id,
    a.Attendee_Name,
    a.Attendee_Email
FROM Events e
JOIN Registrations r ON e.Event_Id = r.Event_Id
JOIN Attendees a    ON r.Attendee_Id = a.Attendee_Id
WHERE e.Event_Id = 1
ORDER BY a.Attendee_Name;

-- Total number of attendees per event
SELECT
    e.Event_Id,
    e.Event_Name,
    COUNT(r.Attendee_Id) AS total_attendees
FROM Events e
LEFT JOIN Registrations r ON e.Event_Id = r.Event_Id
GROUP BY e.Event_Id, e.Event_Name
ORDER BY total_attendees DESC;

-- Total revenue (Registration_Amount) per event
SELECT
    e.Event_Id,
    e.Event_Name,
    COALESCE(SUM(r.Registration_Amount), 0) AS total_revenue
FROM Events e
LEFT JOIN Registrations r ON e.Event_Id = r.Event_Id
GROUP BY e.Event_Id, e.Event_Name
ORDER BY total_revenue DESC;

-- Attendee statistics by city
SELECT
    a.Attendee_City,
    COUNT(*) AS total_attendees
FROM Attendees a
GROUP BY a.Attendee_City
ORDER BY total_attendees DESC;