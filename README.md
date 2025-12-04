---
## 📝 Project Overview

This capstone contains **four independent SQL projects**, each demonstrating great understanding over database design, relationships, querying, aggregation, analytics, and OLAP operations.
---

# ✅ **TASK 1 — Academic Management System**

**Database:** `academic_management`  
**Tables:**
- `StudentInfo`
- `CoursesInfo`
- `EnrollmentInfo` (with 2 foreign keys)

### Includes:
- Database schema creation  
- Sample data insertion  
- Student/course retrieval queries  
- Join-based reporting  
- Analytics:
  - students per course  
  - students enrolled in multiple courses  
  - instructors with highest enrollments  
  - top courses by enrollment  

📸 *Screenshots available under:*  
`/screenshots/task1/`

---

# ✅ **TASK 2 — Student Database Management System**

**Database:** `student_database`  
**Table:** `student_table` → renamed to `student_info`

### Includes:
- 10 sample records
- Sorting by grade
- Filtering male students
- GPA < 5.0 query
- Update statements
- Name + age retrieval for Grade B students
- Grouping by department & gender (avg GPA)
- Highest GPA student retrieval

📸 *Screenshots available under:*  
`/screenshots/task2/`

---

# ✅ **TASK 3 — Event Management System**

**Database:** `events_management`  
**Tables:** `Events`, `Attendees`, `Registrations`

### Includes:
- CRUD for events
- CRUD for attendees
- Registering attendees for events
- Event analytics:
  - Attendee list per event  
  - Total attendees per event  
  - Revenue per event  
  - Attendee distribution by city  

📸 *Screenshots available under:*  
`/screenshots/task3/`

---

# ✅ **TASK 4 — OLAP Operations (Redshift/PostgreSQL)**

**Database:** `sales_olap`  
**Table:** `sales_sample`

### OLAP Operations:
- **Drill Down** (region → product)
- **Rollup** (product → region totals)
- **Cube** (multi-dimensional)
- **Slice** (filter by region/date)
- **Dice** (filter by multiple dimensions)

📸 *Screenshots available under:*  
`/screenshots/task4/`

---

## 🚀 How to Run This Project

1. Install **PostgreSQL** and **pgAdmin** (or use VS Code SQL extensions).
2. Create each database manually or from scripts.
3. Open each `.sql` file and execute in order:
   - Schema → Insert Data → Queries
4. Compare outputs with screenshot folders.

---

## 👤 Author

**Mohammed Hammad**  
SQL Capstone Project Submission
Year: 2025

---

## ⭐ Acknowledgements
- Course-provided problem statement  
- PostgreSQL Documentation  
