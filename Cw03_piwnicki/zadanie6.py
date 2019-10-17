class Calculator:
    def __init__(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2

    def add(self):
        return self.liczba1 + self.liczba2

    def difference(self):
        return self.liczba1 - self.liczba2

    def multiply(self):
        return self.liczba1 * self.liczba2

    def divide(self):
        return self.liczba1 / self.liczba2


class ScienceCalculator(Calculator):
    def poteguj(self):
        return self.liczba1 ** self.liczba2


c = ScienceCalculator(2, 3)
print(c.divide())
print(c.poteguj())
