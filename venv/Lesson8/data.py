import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# cur.execute("INSERT INTO first_table (name) VALUES ('Anna');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Max');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Alex');")
# cur.execute("SELECT rowid, name FROM first_table;")
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# cur.execute("UPDATE first_table SET name='Ivan' WHERE rowid=3;")
# cur.execute("DELETE FROM first_table WHERE rowid=4;")
# cur.execute("SELECT rowid, name FROM first_table;")
cur.execute("DROP TABLE first_table")
connection.commit()

# res = cur.fetchall()
# print(res)

connection.close()