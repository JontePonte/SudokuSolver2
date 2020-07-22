import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

# c.execute("""CREATE TABLE test (
#     first text,
#     last text,
#     pay integer
#     )""")

# c.execute("INSERT INTO test VALUES ('John!', 'Piff', '1000000000')")

c.execute("SELECT * FROM test WHERE last = 'Piff'")

print(c.fetchall())

conn.commit()

conn.close()