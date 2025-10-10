class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print("Створено новий об’єкт машини!")
        print(self.brand, self.color)


car1 = Car("BMW", "black")
