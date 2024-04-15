import sqlite3

DB_NAME = "cinema.db"
with sqlite3.connect("DB_NAME") as sqlite_conn:
    cur = sqlite_conn.cursor()
    sqlite_request = cur.execute("""
        SELECT name_movie, release
        FROM movies
        WHERE release BETWEEN 2015 AND 2020;
        """)
    result = sqlite_request.fetchall()

# Вывод результатов
print("Фильмы, которые были сняты с 2015 по 2020 год:")
for row in result:
    print(row[0], "-", row[1])


