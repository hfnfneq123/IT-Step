import sqlite3

connection = sqlite3.connect("FruitBasket.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE Fruits (name, color);")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Яблуко', 'Червоне');")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Банан', 'Жовтий');")
cur.execute("INSERT INTO Fruits (name, color) VALUES ('Апельсин', 'Помаранчевий');")
cur.execute("UPDATE Fruits SET color = 'Зелене' WHERE name = 'Яблуко';")


connection.commit()
print("\nВсі фрукти жовтого кольору:")
for row in cur.execute("SELECT * FROM Fruits WHERE color = 'Жовтий';"):
    print(row)


print("\nВсі записи про фрукти:")
for row in cur.execute("SELECT * FROM Fruits;"):
    print(row)

connection.close()