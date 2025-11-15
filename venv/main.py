import cv2
from PIL import Image

# Шлях до зображень
image_path = 'Sobaka.png'
cascade_path = 'cascade.xml'
hat_path = 'Hat.png'

# Завантажуємо каскад
dog_cascade = cv2.CascadeClassifier(cascade_path)

# Завантажуємо зображення та переводимо у сірий формат
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Розпізнаємо "голову собаки"
faces = dog_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

# Відкриваємо через PIL
dog = Image.open(image_path).convert("RGBA")
hat = Image.open(hat_path).convert("RGBA")

# Додаємо капелюх
for (x, y, w, h) in faces:
    # Змінюємо розмір капелюха відповідно до ширини голови
    resized_hat = hat.resize((w, int(h/2)))  # половина висоти обличчя
    # Позиціонуємо трохи вище голови
    hat_y = y - int(h/3)
    dog.paste(resized_hat, (x, hat_y), resized_hat)

# Зберігаємо результат
dog.save("dog_new.png")

# Відображаємо
dog_new = cv2.imread("dog_new.png")
cv2.imshow("Dog with Hat", dog_new)
cv2.waitKey(0)
cv2.destroyAllWindows()


