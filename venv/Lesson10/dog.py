import cv2
from PIL import Image


image_path = 'Sobaka.png'
cascade_path = 'cascade.xml'
hat_path = 'Hat.png'


dog_cascade = cv2.CascadeClassifier(cascade_path)

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = dog_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

dog = Image.open(image_path).convert("RGBA")
hat = Image.open(hat_path).convert("RGBA")


for (x, y, w, h) in faces:
    resized_hat = hat.resize((w, int(h/3)))
    hat_y = y - int(h/3)
    dog.paste(resized_hat, (x, hat_y), resized_hat)

dog.save("dog_new.png")

dog_new = cv2.imread("dog_new.png")
cv2.imshow("Dog with Hat", dog_new)
cv2.waitKey()


