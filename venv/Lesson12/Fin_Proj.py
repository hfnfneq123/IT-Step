import sqlite3
import requests
from bs4 import BeautifulSoup

DB_NAME = "sites.db"  # назва файлу БД

# === Створення бази та таблиці ===
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
    print("Таблиця 'links' готова або вже існувала.")

# === Додавання посилань ===
def add_links():
    links_to_add = [
        "https://en.wikipedia.org/wiki/Animal",
        "https://en.wikipedia.org/wiki/Ecology",
        "https://en.wikipedia.org/wiki/Reproduction"
    ]
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for link in links_to_add:
        cursor.execute("SELECT id FROM links WHERE url=?", (link,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO links (url) VALUES (?)", (link,))
    conn.commit()
    conn.close()
    print("Посилання додані або вже існували.")

# === Отримання всіх посилань з БД ===
def get_links_from_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM links")
    links = [row[0] for row in cursor.fetchall()]
    conn.close()
    return links

# === Пошук ключових слів на сторінці ===
def search_in_page(url, query):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', class_='mw-parser-output')
        if not content:
            return []

        # Беремо всі абзаци, списки, заголовки та таблиці
        # Беремо всі абзаци, списки, заголовки та таблиці
        paragraphs = content.find_all(['p', 'li', 'h2', 'h3', 'h4', 'td'])
        text_paragraphs = []

        for p in paragraphs:
            # Отримуємо текст навіть зі спанів всередині заголовків
            text_paragraphs.append(' '.join(p.stripped_strings))

        # Ключові слова
        keywords = [k.strip().lower() for k in query.split(',')]

        # Перевіряємо наявність ключових слів
        found = []
        for para in text_paragraphs:
            para_lower = para.lower()
            for kw in keywords:
                if kw in para_lower:
                    found.append(para)
                    break  # не дублюємо абзац

        return found
    except (AttributeError, TypeError):
        return []

# === Головна функція ===
def main():
    # Створюємо БД та таблицю, додаємо посилання
    create_db_and_table()
    add_links()

    # Введення ключових слів
    user_query = input("Введіть ключові слова про тварин (через кому): ")
    links = get_links_from_db()

    print("\nПеревіряю сторінки...")
    any_found = False
    for link in links:
        results = search_in_page(link, user_query)
        if results:
            any_found = True
            print(f"\nЗнайдено на сайті: {link}")
            for r in results:
                print("-", r[:200] + ("..." if len(r) > 200 else ""))  # показуємо перші 200 символів абзацу

    if not any_found:
        print("\nНічого не знайдено.")

if __name__ == "__main__":
    main()
