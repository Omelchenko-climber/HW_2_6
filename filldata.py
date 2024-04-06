import sqlite3
from random import randint
from datetime import datetime
import pprint

import faker


NUMBER_STUDENTS = 45
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 4
NUMBER_MARKS = 20
SUBJECTS = ["Introduction to Computer Science", "Principles of Economics", "Introduction to Psychology",
            "World History Since", "Introduction to Sociology", "Mathematics", "Biology", "Physics"]


def generate_data(students, groups, teachers, marks, subjects):
    fake_data = faker.Faker()

    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_marks = NUMBER_MARKS
    fake_subjects = subjects

    for _ in range(students):
        fake_students.append(f"{fake_data.first_name()} {fake_data.last_name()}")

    for i in range(101, 101 + groups):
        fake_groups.append(i)

    for _ in range(teachers):
        fake_teachers.append(f"{fake_data.first_name()} {fake_data.last_name()}")

    return fake_students, fake_groups, fake_teachers, fake_marks, fake_subjects


def prepare_date(students, groups, teachers, marks, subjects):
    fake_data = faker.Faker()

    for_students = []
    new_students = students
    for group in groups:
        for_students.extend([(x, group) for x in new_students[:15]])
        new_students = new_students[15:]


    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = [(sub, randint(1, len(teachers))) for sub in subjects]

    for_marks = []
    for i in range(1, len(students) + 1):
        for _ in range(marks):
            for_marks.append((i, randint(1,len(subjects)), randint(1, 12), fake_data.date_between(start_date=datetime(2024, 1, 1))))

    return for_students, for_groups, for_teachers, for_marks, for_subjects


def insert_into_db(students, groups, teachers, marks, subjects):
    with sqlite3.connect("dz_6.db") as conn:
        cur = conn.cursor()




if __name__ == '__main__':
    students, groups, teachers, marks, subjects = generate_data(
        NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_MARKS, SUBJECTS)

    students, groups, teachers, marks, subjects = prepare_date(students, groups, teachers, marks, subjects)

    print(students, groups, teachers, marks, subjects, sep="\n")
