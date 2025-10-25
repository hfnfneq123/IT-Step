import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE Animals (name, type);")
cur.execute("DELETE FROM Animals WHERE rowid=1;")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Крокодил', 'Плазун');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Орел', 'Птах');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Морська черепаха', 'Плазун');")
cur.execute("INSERT INTO Animals (name, type) VALUES ('Мавпа', 'Ссавець');")
cur.execute("UPDATE Animals SET name = 'Сокіл' WHERE name = 'Орел';")


connection.commit()
print("\nСсавці: ")
for row in cur.execute("SELECT * FROM Animals WHERE type = 'Ссавець';"):
    print(row)

cur.execute("SELECT * FROM Animals;")
res = cur.fetchall()

print("\nУсі тварини: ")
for row in res:
    print(row)

connection.close()