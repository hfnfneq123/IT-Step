import math

try:
    result = math.square(5)
    print("Результат:", result)
except AttributeError:
    print("Помилка: функція 'square' не знайдена в модулі 'math'.")
