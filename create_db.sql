-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id integer PRIMARY KEY AUTOINCREMENT,
    group_number integer NOT NULL
);


-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name text NOT NULL,
    group_id integer NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);


-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id integer PRIMARY KEY AUTOINCREMENT,
    teacher_name text NOT NULL
);


-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id integer PRIMARY KEY AUTOINCREMENT,
    subject_name text NOT NULL,
    teacher_id integer NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);


--Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    student_id integer NOT NULL,
    subject_id integer NOT NULL,
    grade integer NOT NULL,
    date_of DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);