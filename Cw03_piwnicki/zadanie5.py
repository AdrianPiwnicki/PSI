# Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide.
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

a = Calculator(-7, -4)
print(a.add())
print(a.difference())
print(a.multiply())
print(a.divide())

