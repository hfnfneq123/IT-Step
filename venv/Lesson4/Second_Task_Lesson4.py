class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Age: {self.age}, Name: {self.name}")

class Driver(Person):
    def __init__(self, name, age, Number_Of_Driver):
        super().__init__(name, age)
        self.Number_Of_Driver = Number_Of_Driver

    def info(self):
        print(f"Age: {self.age}, Name: {self.name}, Number_Of_Driver: {self.Number_Of_Driver}")

person1 = Person("Artem", 17)
person2 = Driver("Cola", 12, "UA001")

person1.info()
person2.info()