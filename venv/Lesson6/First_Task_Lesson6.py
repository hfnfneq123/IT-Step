users = {
    "Артем": "підліток",
    "Оля": "дитина",
    "Іван": "дорослий",
    "Марія": "пенсіонер"
}

name = input("Введіть ім'я користувача: ")

try:
    if name not in users:
        raise KeyError(f"Користувача з ім'ям '{name}' не знайдено.")

    group = users[name]
    print(f"{name} належить до групи: {group}")

except KeyError as e:
    print("Попередження:", e)