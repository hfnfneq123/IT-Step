class Tvarina:
    def __init__(self, imya):
        self.imya = imya

    def zvuk(self):
        print("Тварина видає звук")


class Sobaka(Tvarina):
    def zvuk(self):
        print("Гав-гав!")


class Kit(Tvarina):
    def zvuk(self):
        print("Мяу!")


# Приклади використання
sobaka = Sobaka("Бім")
kit = Kit("Мурчик")

sobaka.zvuk()
kit.zvuk()
