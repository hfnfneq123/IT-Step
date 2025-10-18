file_path = input("Введіть шлях до файлу: ")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print("\nВміст файлу:\n")
        print(content)

except FileNotFoundError:
    print(f"Помилка: файл за шляхом '{file_path}' не існує.")
