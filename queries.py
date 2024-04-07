import sqlite3
import pprint


database = "dz_6.db"


def get_sql_response(file):
    with open(file, "r") as f:
        sql_query = f.read()

    with sqlite3.connect(database) as conn:
        cur = conn.cursor()
        cur.execute(sql_query)

        return cur.fetchall()


if __name__ == '__main__':
    response = get_sql_response("queries/query_10.sql")
    pprint.pp(response)
