import sqlite3
from random import randint
from datetime import datetime

import faker


STUDENTS = ['David Ross', 'Susan Bradshaw', 'Cynthia Shaw', 'Kathryn Waller', 'Jonathan Serrano',
                     'Kathleen Brown', 'Ann Richardson', 'Samuel Gutierrez', 'Matthew White', 'Austin Harris',
                     'Joshua Payne', 'Danielle Craig', 'Cory Martinez', 'Michael Bradley', 'Christina Jackson',
                     'Heather Lamb', 'Gina Rivera', 'Michael Bray', 'Misty Church', 'Michael Ross', 'Gabriel Bryant',
                     'Scott Weaver', 'Johnny Howe', 'Henry Dodson', 'James Carter', 'Gene Johnson', 'Brandon Morrison',
                     'Sandy Smith', 'Joshua Gibson', 'Jeanne Pacheco', 'Catherine Charles', 'Kim Cummings',
                     'Kenneth Armstrong', 'Joseph Matthews', 'Angela Jordan', 'Marissa Brooks', 'William Haynes',
                     'Troy Smith', 'Sean Hamilton', 'Scott Jennings', 'David Brown', 'Abigail Leblanc',
                     'Christine Perez', 'Kelly Johnston', 'Robert Smith']
NUMBER_GROUPS = [101, 102, 103]
TEACHERS = ["Gabrielle Curtis", "Brandy Bradford", "Jessica Jones", "Lucas Fletcher"]
NUMBER_GRADES = 20
SUBJECTS = ["Introduction to Computer Science", "Principles of Economics", "Introduction to Psychology",
            "World History Since", "Introduction to Sociology", "Mathematics", "Biology", "Physics"]


def generate_data(students, groups, teachers, grades, subjects):

    fake_students = students
    fake_groups = groups
    fake_teachers = teachers
    fake_grades = grades
    fake_subjects = subjects

    return fake_students, fake_groups, fake_teachers, fake_grades, fake_subjects


def prepare_date(students, groups, teachers, grades, subjects):
    fake_data = faker.Faker()

    for_students = []
    new_students = students
    for i in range(1, len(groups) + 1):
        for_students.extend([(x, i) for x in new_students[:15]])
        new_students = new_students[15:]


    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []
    for i, sub in enumerate(subjects, 1):
        for_subjects.append((sub, i % 4 if i % 4 != 0 else 4))

    for_grades = []
    for _ in range(3):
        for i in range(1, len(subjects) + 1):
            for j in range(1, len(groups) + 1):
                random_date = fake_data.date_between(start_date=datetime(2024, 1, 1))
                for i, student in enumerate(for_students, 1):
                    _, group = student
                    if j == group:
                        for_grades.append((i, randint(1,len(subjects)), randint(1, 12), random_date))

    return for_students, for_groups, for_teachers, for_grades, for_subjects


def insert_into_db(students, groups, teachers, grades, subjects):
    with sqlite3.connect("dz_6.db") as conn:
        cur = conn.cursor()

        sql_to_groups = """INSERT INTO groups (group_number)
        VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students (student_name, group_id)
        VALUES(?, ?)
        """
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers (teacher_name)
        VALUES (?)
        """
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects (subject_name, teacher_id)
        VALUES (?, ?)
        """
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, date_of)
        VALUES (?, ?, ?, ?)
        """
        cur.executemany(sql_to_grades, grades)

        conn.commit()


if __name__ == '__main__':

    students, groups, teachers, grades, subjects = prepare_date(STUDENTS, NUMBER_GROUPS, TEACHERS, NUMBER_GRADES, SUBJECTS)

    insert_into_db(students, groups, teachers, grades, subjects)
