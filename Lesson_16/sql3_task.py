import sqlite3

print('======================= N 1 ====================')
# Подключить готовую базу с актёрами и режиссёрами использую SQLite3.
# При помощи “сырого” запроса вывести все фильмы,
# которые были сняты с 2015 по 2020 год.

con = sqlite3.connect("cinema.db")
cur = con.cursor()

cur.execute("""
SELECT name_movie, release
FROM movies
WHERE release BETWEEN 2015 AND 2020
""")
result = cur.fetchall()

print("Фильмы, которые были сняты с 2015 по 2020 год:")
for row in result:
    print(row[0], "-", row[1])

# Закрыть соединение с базой данных
con.close()

print('=================== N 2 ===================')

# Использую SQLite3 при помощи “сырого”  запроса вывести актёров и режиссёров,
# которые не участвовали не в одном из фильмов.

conn = sqlite3.connect('cinema.db')
cur = conn.cursor()

cur.execute("""
    SELECT name
    FROM actors
    WHERE name NOT IN (
        SELECT DISTINCT name
        FROM movies
                    ) 
""")
result = cur.fetchall()

print("Актеры и режиссеры, которые не участвовали ни в одном фильме:")
for row in result:
    print(row[0])

con.close()

print('=================== N 3 ===================')

# Использую SQLite3 при помощи “сырого”  запроса
# вывести все фильмы  которые были сняты после 2000 года
# и в которых приняло участие более 1 актёра

conn = sqlite3.connect('cinema.db')
cur = conn.cursor()

cur.execute("SELECT * FROM movies WHERE release > 2000 AND actors_name > 1")
rows = cur.fetchall()

conn.close()

print('=================== N 4 ===================')
# Использую SQLite3 при помощи “сырого”  запроса вывести первых
# 5 самых высокооплачиваемых актёров.
cur.execute("SELECT name, finance FROM actors ORDER BY finance DESC LIMIT 5")
result = cur.fetchall()

con.close()
print('=================== N 5 ===================')

# Использую SQLite3 при помощи “сырого”  запроса вывести всех режиссёров
# и актёров которые были задействованы только в 1 фильме.

conn = sqlite3.connect('cinema.db')
cur = conn.cursor()

cur.execute('''
    SELECT name
    FROM (
        SELECT director AS name
        FROM movies
        GROUP BY director
        HAVING COUNT(*) = 1
        UNION
        SELECT actor AS name
        FROM movies
        GROUP BY actor
        HAVING COUNT(*) = 1
    ) t
''')

results = cur.fetchall()
for row in results:
    print(row[0])

conn.close()
