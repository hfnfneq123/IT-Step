import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

DB_NAME = "books_search.db"

# === 1. Створення БД і таблиці ===
def create_db_and_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# === 2. Додавання сайту в БД ===
def add_site(url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM sites WHERE url = ?", (url,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO sites (url) VALUES (?)", (url,))
        conn.commit()
    conn.close()

# === 3. Отримання усіх сайтів з БД ===
def get_all_sites():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM sites")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

# === 4. Парсинг однієї сторінки каталогу (назва + URL) ===
def get_books_from_page(page_url, base_url):
    try:
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()
    except Exception:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book_tag in soup.select("article.product_pod"):
        title = book_tag.h3.a["title"]
        href = book_tag.h3.a["href"]
        full_url = urljoin(base_url, href)

        books.append({
            "title": title,
            "url": full_url
        })
    return books

# === 5. Парсинг структурованого Product Description ===
def get_book_description(book_url):
    try:
        response = requests.get(book_url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'  # правильне кодування
    except Exception:
        return ["Опис відсутній"]

    soup = BeautifulSoup(response.text, "html.parser")
    desc_tag = soup.select_one("#product_description")
    if desc_tag:
        p_tag = desc_tag.find_next_sibling("p")
        if p_tag:
            text = p_tag.text.strip()
            text = text.replace("\xa0", " ")  # прибираємо дивні символи
            paragraphs = [para.strip() for para in text.split('. ') if para.strip()]
            return paragraphs
    return ["Опис відсутній"]

# === 6. Пошук книги по всіх сайтах і сторінках ===
def search_books(query):
    query = query.lower()
    found_books = []

    sites = get_all_sites()
    for base_url in sites:
        page_num = 1
        while True:
            page_url = base_url if page_num == 1 else urljoin(base_url, f'catalogue/page-{page_num}.html')
            books = get_books_from_page(page_url, base_url)
            if not books:
                break

            for book in books:
                if query in book["title"].lower():
                    description = get_book_description(book["url"])
                    found_books.append({
                        "title": book["title"],
                        "url": book["url"],
                        "description": description
                    })

            page_num += 1

    return found_books

# === 7. Основний запуск ===
if __name__ == "__main__":
    create_db_and_table()
    add_site("http://books.toscrape.com/")  # додаємо сайт у БД

    search_query = input("Введіть назву для пошуку книги: ")
    results = search_books(search_query)

    if results:
        print(f"\nЗнайдено {len(results)} книг:\n")
        for b in results:
            print(f"Назва: {b['title']}")
            print(f"Посилання: {b['url']}")
            print(f"Product Description:\n")
            for para in b['description']:
                print(f"{para}.\n")
            print('-'*80 + '\n')
    else:
        print("Не знайдено жодної книги за цим запитом.")
