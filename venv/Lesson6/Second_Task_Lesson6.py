try:
    number = input("Введіть число: ")
    number = int(number)
    print("Ваше число:", number)
except ValueError:
    print("Помилка: введене значення не можна конвертувати в ціле число.")
