import sqlite3
import requests
from bs4 import BeautifulSoup
import os

DB_NAME = "sites.db"  # назва файлу БД


# Функція створює базу та таблицю, якщо вони не існують
def create_db_and_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Функція додає посилання у таблицю, якщо їх ще немає
def add_links():
    links_to_add = [
        "https://wikipedia.org",
        "https://www.nationalarchives.gov.uk/"
    ]
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for link in links_to_add:
        # перевіряємо, чи такого посилання ще немає
        cursor.execute("SELECT id FROM links WHERE url=?", (link,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO links (url) VALUES (?)", (link,))

    conn.commit()
    conn.close()


# Функція зчитує всі посилання з БД
def get_links_from_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM links")
    links = [row[0] for row in cursor.fetchall()]
    conn.close()
    return links


# Пошук тексту на сторінці
def search_in_page(url, query):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ').lower()
        query = query.lower()
        return query in text
    except Exception:
        return False


def main():
    # 1. Створюємо БД та таблицю
    create_db_and_table()

    # 2. Додаємо посилання
    add_links()

    # 3. Пошук
    user_query = input("Введіть текст для пошуку: ")
    links = get_links_from_db()

    print("Перевіряю сторінки...")
    found = []
    for link in links:
        if search_in_page(link, user_query):
            found.append(link)

    if found:
        print("\nЗнайдено на таких сайтах:")
        for f in found:
            print(f)
    else:
        print("\nНічого не знайдено.")


if __name__ == "__main__":
    main()

