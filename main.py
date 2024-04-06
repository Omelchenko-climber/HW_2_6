import sqlite3


database = 'dz_6.db'


def create_db(sql_file, db_file):
    with open(sql_file, "r") as f:
        sql_commands = f.read()

    with sqlite3.connect(db_file) as conn:
        cur = conn.cursor()
        cur.executescript(sql_commands)


if __name__ == '__main__':
    create_db("create_db.sql", database)

    subjects = ["Introduction to Computer Science", "Principles of Economics", "Introduction to Psychology",
            "World History Since", "Introduction to Sociology"]

    for_subjects = [(sub, ind) for ind, sub in enumerate(subjects, 1)]

    print(for_subjects)

